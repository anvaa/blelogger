import datetime
import csv, json
import os
from os.path import exists
from runtimesettings import RunTimeSettings

rts = RunTimeSettings()

def getNowShortFormated():
    return datetime.datetime.now().strftime("%d%m%y_%H%M%S")

def getNowSQLFormated():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def formatDateTime(formatThis):
    return formatThis.strftime("%Y.%m.%d %H:%M:%S")

def runToTime(runfor: float):
    from datetime import timedelta
    if runfor == 0 or runfor < 0:
        runfor = 43200 # 30 days as default
    newRunTotime = datetime.datetime.now() + timedelta(minutes=runfor)
    print(f"Running for {runfor} minutes until {formatDateTime(newRunTotime)}.")
    return newRunTotime

def genFileName(locName):
    return  f"{locName}_{getNowShortFormated()}"

def checkFileAndFolder(locname, filename, wtj=0, wtc=0):
    if not checkFolderEx(locname):
        print("Not a folder!")
        exit()            
    if wtj == 1:
            print(f'Writing -> {filename}_n.json')
    if wtc == 1:    
        print(f'Appending -> {filename}.csv')  
          
def checkFolderEx(locname):
    p = f"{os.getcwd()}/logg/{locname}/"
    if not os.path.exists(p):
        os.mkdir(p)
        print(f"First time run: Made <logg> folder: {p}")
        makeZipScript(p,locname)
        return True
    else: return True

def makeZipScript(loggPath,locname):
    zipPath = loggPath + "runzip.sh"
    with open(zipPath, "w") as outfile:
        outfile.write(f"#bin/bash\n\ncd logg/{locname}\nsudo zip -m -u {locname}_loggfiles.zip *.csv") 
    os.chmod(zipPath, 0o755)
    print("First time run: Made runzip.sh script in logg folder.")

def writeRunScript(l,r,s,j,c,n,z):
    runm = "runme.sh"
    if exists(runm):
        os.remove(runm)
    with open(runm, "w") as outfile:
        outfile.write(f"#bin/bash\n\nsudo mount -a\nsudo python3 getble.py -l {l} -r {r} -s {s} -j {j} -c {c} -n {n} -z {z}")
    os.chmod(runm, 0o755)

def writeData(devices, locname, fname, writejson: int, writecsv: int, jcount: int):
    
    devices_m = []

    if len(devices) < 5: #4=Null
        print("No data in devices dictionary! Terminating!")
        exit()

    for dev in devices:
        name = ""
        for (adtype, desc, value) in dev.getScanData():
            if (desc == "Complete Local Name"):
                name = str(value)
                
        devaddr = dev.addr.replace(':','')
        devices_m.append({'location': locname, 'time': getNowSQLFormated(), 'addr': devaddr, 'rssi': dev.rssi, 'name': name})

    print(f"Scan {jcount}: {len(devices_m)} devices found {formatDateTime(datetime.datetime.now())}")
    json_devices = json.dumps(devices_m)

    if writejson > 0:
        newjf = f"logg/{locname}/{fname}_{jcount}.json"
        with open(newjf, "w") as outfile:
            outfile.write(json_devices)

    if writecsv > 0:
        newcf = f"logg/{locname}/{fname}.csv"
        data_file = open(newcf, 'a')
        csv_writer = csv.writer(data_file)

        for dev in devices_m:
            csv_writer.writerow(dev.values())
