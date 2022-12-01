import time
import argparse
from bluepy.btle import DefaultDelegate, Scanner
import dothejob as dtj

parser = argparse.ArgumentParser()
parser.add_argument('-l','-locationName')
parser.add_argument('-r','-runForMin')
parser.add_argument('-j','-writeToJson')
parser.add_argument('-c','-writeToCsv')
parser.add_argument('-s','-scanIntSec')
args = parser.parse_args()

if args.l == None:
    print('>> LocationName can`t be emty!')
    exit()
    
if args.r != None:  
  if float(args.r) == 0:
    args.r = 525600
    print(f">> RunForMin set to {args.r} minutes (One Year!)")
else:
  args.r = float(1.0)
  print(f">> Runformin can`t be 0! Set to {args.r} minute.")
    
if args.s == None or args.s == 0:
    args.s = 30
    print(f">> Default: Scan interval set to {args.s} seconds.")

if args.j == None: 
    args.j = 0

if args.c == None: 
    args.c = 0    

#print(f"-l {args.l}, -r {args.r}, -s {args.s}, -j {args.j}, -c {args.c}")

count=0
startTime = dtj.getTimeNow()
endTime = dtj.runToTime(float(args.r)) #0.16 = 10sec, 0.5 = 30sec, 1.0 = 1min ...
tmpFname = f"{args.l}_{dtj.getNowShortFormated()}"

print("Ctrl+c to exit")

if args.j == '1':
    dtj.checkJsonFileFolder(tmpFname, args.l)

if args.c == '1':
    dtj.checkCsvFileFolder(tmpFname, args.l)


while endTime > dtj.getTimeNow():
    count+=1
    try:
        scanner = Scanner()
        devices = scanner.scan(10, True) # Scan for 10 seconds, be passive

        dtj.writeData(devices, args.l, tmpFname, int(args.j), int(args.c), count)

    except Exception as ex:
        print ( "Unexpected error in BLE Scanner: %s" % ex )
        exit()

    time.sleep(int(args.s)) # wait n seconds before next scan
    
