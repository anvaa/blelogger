import time
import io, sys
import argparse
from bluepy.btle import DefaultDelegate, Scanner
import dothejob as dtj

parser = argparse.ArgumentParser()
parser.add_argument('sitename', type=str)
parser.add_argument('runfor', type=float)
parser.add_argument('writejson', type=int)
parser.add_argument('writecsv', type=int)
args = parser.parse_args()

if args.sitename=="": sname = "site"
if args.runfor==0: 
    args.runfor=525600 #one year


count=0
startTime = dtj.getTimeNow()
endTime = dtj.runToTime(args.runfor) #0.16 = 10sec, 0.5 = 30sec, 1.0 = 1min ...
filename = args.sitename + "_" + dtj.getNowShortFormated()

print("Ctrl+c to exit")

if args.writejson == 1: print(f'Writing -> {filename}_n.json')
if args.writecsv == 1: print(f'Appending -> {filename}.csv')

while endTime > dtj.getTimeNow():
    count+=1
    try:
        scanner = Scanner()
        devices = scanner.scan(10, True)
        
        # write data to json
        #devicelist from scanner, write to filename(no extention in name), 
        # write to json-file, write to csv-file
        dtj.writeData(devices, filename, args.writejson, args.writecsv, count) 
        
    except Exception as ex:
        print ( "Unexpected error in BLE Scanner: %s" % ex )
        exit()
        
    time.sleep(1)
    
    

    
    