
getble.py [-h] sitename runfor writejson writecsv

usage: getble.py [-h] [-l] [-r] [-j] [-c] [-s] [-n] [-z]

optional arguments:
  -h, --help            show this help message and exit
  -l, -locationName 
  -r, -runForMinutes 
  -j, -writeToJson 
  -c, -writeToCsv 
  -s, -scanIntervalInSeconds 
  -n, -ChangeFileNameInMinutes 
  -z, -RunZipOnLoggFiles

    ex: getble.py -l home -r 2 -c 1 
        #runs for 2 minutes and write to home_<timestamp>.csv

Dataoutput ->   time, #datetime as yy-mm-dd hh:mm:ss (sqltime) 
                addr, #c2:45:56:49:ef:78
                rssi, #in db -0 = strong signal
                name  #name of device if any

Install:
    - sudo apt install python3-pip libglib2.0-dev git
    - sudo pip install bluepy
    - git clone https://github.com/anvaa/blelogger.git

Read this for more documentation on bluepy: http://ianharvey.github.io/bluepy-doc/

License:
This project uses code from the bluez project, which is available under the Version 2 of the GNU Public License. 
The Python files are released into the public domain by their author, Ian Harvey. https://github.com/IanHarvey/bluepy
