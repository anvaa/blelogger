import datetime
import csv, json
import os

#Returns unformates datetime object
def getTimeNow():
    return datetime.datetime.now()

#Return formated datetime string 
def getNowShortFormated():
    return datetime.datetime.today().strftime("%d%m%y%H%m%S")

#Return formated datetime string
def getNowSQLFormated():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")

def formatDateTime(formatThis):
    return formatThis.strftime("%Y.%m.%d %H:%m:%s")

def runToTime(runfor=0.0):
    from datetime import timedelta
    if runfor > 0:
        newRunTotime = datetime.datetime.today() + timedelta(minutes=runfor)
        print(f"Running for {runfor} minutes.")
    return newRunTotime

def checkJsonFileFolder(jname):
    if checkFolderEx():
      print(f'Writing -> {jname}_n.json')
    else:
      print("Not a folder!")  

def checkCsvFileFolder(cname):          
    if checkFolderEx():
      print(f'Appending -> {cname}.csv') 
    else:
      print("Not a folder!")  
        
def checkFolderEx():
    p = os.getcwd()+"/logg/"  
    if not os.path.exists(p):
        os.mkdir(p)
        print(f"First time run: Made <logg> folder: {p}")
        return True
    else: return True

#Format and write json/csv data from ble-scaning
def writeData(devices, fname, writejson=0, writecsv=0, jcount=0):

    devices_m = []

    if len(devices) < 5: #4=Null
        print("No data in devices dictionary! Terminating!")
        exit()

    for dev in devices:
        name = ""
        for (adtype, desc, value) in dev.getScanData():
            if (desc == "Complete Local Name"):
                name = str(value)

        # add device addr, addType and rssi to devices_m
        devices_m.append({'time': getNowSQLFormated(), 'addr': dev.addr, 'rssi': dev.rssi, 'name': name})

    print(f"Scan {jcount}: {len(devices_m)} devices found.")
    devices_m.sort(key=lambda x: x["rssi"], reverse=True) #Sort in signalstrength(db)
    json_devices = json.dumps(devices_m)

    if writejson > 0:
        newjf = f"logg/{fname}_{jcount}.json"
        with open(newjf, "w") as outfile:
            outfile.write(json_devices)

    if writecsv > 0:
        newcf = f"logg/{fname}.csv"
        data_file = open(newcf, 'a')
        csv_writer = csv.writer(data_file)

        for dev in devices_m:
            csv_writer.writerow(dev.values())
