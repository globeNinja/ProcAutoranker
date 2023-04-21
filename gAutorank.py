import os
import psutil
import sys
import time

class wingameAutoranker:
    def __init__(self):
        while True:
            self.procAutoranker()
            time.sleep(600)
            
        # self.find_procs_by_name(["FlightSimulator"])
        
    
    def procAutoranker(self):
        #checks if the os is on windows
        windowsChecker = self.isWindows()

        checkedProcDict = self.find_procs_by_name( ["FlightSimulator"])
        
        if windowsChecker:
            import win32api,win32process,win32con
            #pass pid as integer here
            for k,v in checkedProcDict.items():
                if "HIGH_PRIORITY" not in str(v[1]):
                    pidNow = v[0]
                    handleNow = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pidNow)

                    #high prio class returns integer 128 if you were curious
                    win32process.SetPriorityClass(handleNow, win32process.HIGH_PRIORITY_CLASS)
                else:
                    print("already high, skipping!")
        else:
            #untested here because I do not have linux os, feel free to edit the nice value
            for k,v in checkedProcDict.items():
                #we want to make sure that the nice value is < neg 10 here
                if int(v[1]) > (-10):
                    psutil.Process(v).nice(-16)



        return 0
    
    def find_procs_by_name(self, inName):
        """
        inName(list), expecting a list of names here to match
        returns a dictionary with a list value. index 0 = pid, index 1 = nice value

        """
        hitProc = {}
        abc = psutil.process_iter()
        for i in psutil.process_iter():
            for check in inName:
                if check in str(i.name()):
                    #we are matching the hit proc names with an int pid
                    hitProc[i.name()] = [i.pid, i.nice()]
                    #print(str(i.nice()))

        #print(dir(abc))
        return hitProc

    def isWindows(self):
        try:
            sys.getwindowsversion()
        except AttributeError:
            winBool = False
        else:
            winBool = True
        return winBool

if __name__ == "__main__":
    wingameAutoranker()