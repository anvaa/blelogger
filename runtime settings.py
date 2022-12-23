import datetime
from datetime import timedelta
import socket

class RunTimeSettings:
    def __init__(self):
        
        self._FileName = "fn_non"
        self._LocationName = "lc_non"
        self._ScanInterval = 30
        self._RunForMinutes = 43200
        self._WriteToJson = 0
        self._WriteToCsv = 0
        self._cfntMin = 0
        self._ChangeFileNameTime = datetime.datetime.now() + timedelta(minutes=1440)
        self._RunZipTime = datetime.datetime.now() + timedelta(minutes=10080)
        
    def get_ztm(self):
        return self._cfntMin
    def set_ztm(self,ztm: int):
        self._cfntMin = ztm
    ZipTimeMinutes = property(get_ztm,set_ztm)

    def get_cfntm(self):
        return self._cfntMin
    def set_cfntm(self,cfntm: int):
        self._cfntMin = cfntm
    CfntMin = property(get_cfntm,set_cfntm)
    
    def get_runZipTime(self):
        return self._RunZipTime
    def set_runZipTime(self,zt):
        if zt == None: zt = 10080 # 7 days
        self._RunZipTime = datetime.datetime.now() + timedelta(minutes=int(zt))
        ZipTimeMinutes = int(zt)
        print(f"Running ZIP on loggfiles every {zt} minutes.") 
    RunZipTime = property(get_runZipTime,set_runZipTime)
    
    def get_changeFileNameTime(self):
        return self._ChangeFileNameTime
    def set_changeFileNameTime(self,cfnt):
        if cfnt == None: cfnt = 1440 # one day
        self._ChangeFileNameTime = datetime.datetime.now() + timedelta(minutes=int(cfnt))
        self._cfntMin = int(cfnt)
        print(f"FileName is set to changes every {cfnt} minutes.") 
    ChangeFileNameTime = property(get_changeFileNameTime,set_changeFileNameTime)

    def get_locationName(self):
        return self._LocationName
    def set_locationName(self,ln):
        if ln == None:
            ln = socket.gethostname()
        self._LocationName = ln
    LocationName = property(get_locationName,set_locationName)

    def get_fileName(self):
        return self._FileName
    def set_fileName(self,fn):
        if fn == None:
            print('>> LocationName can`t be emty!')
            exit()
        self._FileName = fn
    FileName = property(get_fileName, set_fileName)

    def get_scanInterval(self):
        return self._ScanInterval
    def set_scanInterval(self,si: int):
        if si == None or si == 0:
            si = 30
            print(f">> Default: Scan interval set to {si} seconds.")
        self._ScanInterval = int(si)
    ScanInterval = property(get_scanInterval,set_scanInterval)

    def get_runForMin(self):
        return self._RunForMinutes
    def set_runForMin(self,rfm):
        if rfm != None:
            if rfm == 0:
                rfm = float(525600)
                self._RunForMinutes = float(525600)
                print(f">> RunForMin set to {self._RunForMinutes} minutes (1 year).")
        elif rfm == None:
            self._RunForMinutes = float(43200)
            print(f">> No Runforminutes Found! Set to {self._RunForMinutes} minute (30 days).")
        else: self._RunForMinutes = float(rfm)
    RunForMinutes = property(get_runForMin,set_runForMin)

    def get_writeToJson(self):
        return self._WriteToJson
    def set_writeToJson(self,wtj):
        if wtj == None:
            wtj = 0
        self._WriteToJson = int(wtj)
    WriteToJson = property(get_writeToJson,set_writeToJson)

    def get_writeToCsv(self):
        return self._WriteToCsv
    def set_writeToCsv(self,wtc):
        if wtc == None:
            wtc = 0
        self._WriteToCsv = int(wtc)
    WriteToCsv = property(get_writeToCsv,set_writeToCsv)

