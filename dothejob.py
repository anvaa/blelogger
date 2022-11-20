import datetime
import csv
import json

#Returns unformates datetime object
def getTimeNow():
    return datetime.datetime.now()

#Return formated datetime string
def getNowShortFormated():
    return datetime.datetime.today().strftime("%d%m%y%H%m%S")
    
#Return formated datetime string
def getNowLongFormated():
    return datetime.datetime.now().strftime("%d%m%y%H%m%s")

def formatDateTime(formatThis):
    return formatThis.strftime("%d.%m.%y %H:%m:%s")

def runToTime(runfor=0.0):
    from datetime import timedelta
    if runfor > 0:
        newRunTotime = datetime.datetime.today() + timedelta(minutes=runfor)
        print("Running for ${runfor} minutes.")
    return newRunTotime
    
#Format and write json/csv data from ble-scaning
def writeData(devices, fname="", writejson=0, writecsv=0, jcount=0):
    
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
        devices_m.append({'time': getNowLongFormated(), 'addr': dev.addr, 'rssi': dev.rssi, 'name': name})
        
    print("Scan "+str(jcount)+": "+str(len(devices_m)) + " devices found")
    devices_m.sort(key=lambda x: x["rssi"], reverse=True) #Sort in signalstrength(db)
    json_devices = json.dumps(devices_m) 
    
    if writejson > 0:
        with open(fname+"_"+str(jcount)+ ".json", "w") as outfile:
            outfile.write(json_devices)
        
    if writecsv > 0:
        data_file = open(fname + ".csv", 'a')
        csv_writer = csv.writer(data_file)
        
        for dev in devices_m:
            csv_writer.writerow(dev.values())
        
