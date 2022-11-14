getble.py [-h] sitename runfor writejson writecsv

    - sitename as string
    - runfor as float #runtime in minutes 0 = one year, 1.5 = 1min 30sec
    - writejson as int 0=no 1=yes #write to .json file(s)
    - writecsv as int 0=no 1=yes #write to .csv file. Appends pr. run.

    ex: getb.py athome 2 0 1 #run for 2 minutes and write to athome_<timestamp>.csv

Dataoutput ->   time, #datetime as ddmmyyhhmmss 
                addr, #c2:45:56:49:ef:78
                rssi, #in db -0 = strong signal
                name  #name of device if any

Read this for more documentation on bluepy: http://ianharvey.github.io/bluepy-doc/

License
This project uses code from the bluez project, which is available under the Version 2 of the GNU Public License. 
The Python files are released into the public domain by their author, Ian Harvey. https://github.com/IanHarvey/bluepy
