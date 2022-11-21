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
def getNowLongFormated():
    return datetime.datetime.now().strftime("%d%m%y%H%m%s")

def formatDateTime(formatThis):
    return formatThis.strftime("%d.%m.%y %H:%m:%s")

def runToTime(runfor=0.0):
    from datetime import timedelta
    if runfor > 0:
        newRunTotime = datetime.datetime.today() + timedelta(minutes=runfor)
        print(f"Running for {runfor} minutes.")
    return newRunTotime

def checkJsonFileFolder(jfilename):
    p=os.getcwd()+'/jsonf/'
    if not os.path.exists(p):
        os.mkdir(p)
        print(f"First time run: Made JSON folder: {p}")
        return False
    print(f'Writing -> {jfilename}_n.json')


def checkCsvFileFolder(cfilename):  # check if folder exists
    p=os.getcwd()+"/csvf/"          # program workdir + filedir
    if not os.path.exists(p):       # if not exists,
        os.mkdir(p)                 # make dir
        print(f"First time run: Made CSV folder: {p}")  # user info
    print(f'Appending -> {cfilename}.csv')              # user info

#Format and write json/csv data from ble-scaning
def writeData(devices, fname="wdname", writejson=0, writecsv=0, jcount=0):

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

    print(f"Scan {jcount}: {len(devices_m)} devices found.")
    devices_m.sort(key=lambda x: x["rssi"], reverse=True) #Sort in signalstrength(db)
    json_devices = json.dumps(devices_m)

    if writejson > 0:
        newjf = f"jsonf/{fname}_{jcount}.json"
        with open(newjf, "w") as outfile:
            outfile.write(json_devices)

    if writecsv > 0:
        newcf = f"csvf/{fname}.csv"
        data_file = open(newcf, 'a')
        csv_writer = csv.writer(data_file)

        for dev in devices_m:
            csv_writer.writerow(dev.values())
