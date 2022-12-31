import time, datetime
import argparse
from bluepy.btle import DefaultDelegate, Scanner
import dothejob as dtj
from rts import RunTimeSettings
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-l','-locationName')
parser.add_argument('-r','-runForMinutes')
parser.add_argument('-j','-writeToJson')
parser.add_argument('-c','-writeToCsv')
parser.add_argument('-s','-scanIntervalInSeconds')
parser.add_argument('-n','-ChangeFileNameInMinutes')
parser.add_argument('-z','-RunZipOnLoggFiles')
args = parser.parse_args()

print("Ctrl+c to exit")
rts = RunTimeSettings()
rts.LocationName = args.l
rts.ScanInterval = args.s
rts.RunForMinutes = args.r
rts.WriteToJson = args.j
rts.WriteToCsv = args.c
rts.RunZipTime = args.z
rts.ChangeFileNameTime = args.n
rts.FileName = dtj.genFileName(rts.LocationName)

rts.getset_json(0)
# print(f"{rts.LocationName} {rts.FileName} {rts.ScanInterval} {rts.RunForMinutes} {rts.WriteToJson} {rts.WriteToCsv}")

count=0
endTime = dtj.runToTime(rts.RunForMinutes)
dtj.checkFileAndFolder(rts.LocationName,rts.FileName,rts.WriteToJson,rts.WriteToCsv)
dtj.writeRunScript(rts.LocationName,rts.RunForMinutes,rts.ScanInterval,rts.WriteToJson,rts.WriteToCsv,rts.CfntMin,rts.RztMinutes)

print(" ")
while endTime > datetime.datetime.now():
    count+=1
    try:
        scanner = Scanner()
        devices = scanner.scan(10, True)
        
        dtj.writeData(devices, rts.LocationName, rts.FileName, rts.WriteToJson, rts.WriteToCsv, count)
        
        if rts.ChangeFileNameTime < datetime.datetime.now():
             rts.FileName = dtj.genFileName(rts.FileName)
             rts.ChangeFileNameTime = args.n

        if rts.RunZipTime < datetime.datetime.now():
            if rts.RztMinutes > 0:
                _ = subprocess.run([f"./logg/{rts.LocationName}/runzip.sh",""], shell=True)
                rts.RunZipTime = rts.RztMinutes
 

    except Exception as ex:
        print ( "Unexpected error in blecanner: %s" % ex )
        exit()

    time.sleep(rts.ScanInterval)
