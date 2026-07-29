"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

3. Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username. 
Usage : ProcInfoLog.py Demo 
Demo is name of Directory.
"""

import psutil
import sys
import os
import time

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])

        listprocess.append(info)

    return listprocess

# Process Information
def ProcessInfo(FolderName):
    Border = "-" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing nut its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets creted successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "ProcessInfo_%s.log" %timestamp)

    fObj = open(FileName, "w")

    print(f"Log file get successfully created with name {FileName}")

    fObj.write(Border + "\n")
    fObj.write("---- Marvellous Process Information System ----\n")
    fObj.write("Log file gets created at : " + timestamp + "\n")
    fObj.write(Border + "\n\n")

    fObj.write("---------------- System Report ----------------\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        fObj.write("Name : %s\n" %info.get("name"))
        fObj.write("PID : %s\n" %info.get("pid"))
        fObj.write("User Name : %s\n" %info.get("username"))
        fObj.write(Border + "\n")

    # Log file footer
    fObj.write(Border + "\n")
    fObj.write("--------------- End of log file ---------------\n")
    fObj.write(Border + "\n")

    fObj.close()

# Main Function
def main():

    Border = "-" * 50

    print(Border)
    print("----- Marvellous Platform Surveillance System -----")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print(f"Usage : python {sys.argv[0]} Folder_Name")
        return

    if sys.argv[1] == "--h" or sys.argv[1] == "--H":
        print("This automation script displays information of running processes")
        return

    if sys.argv[1] == "--u" or sys.argv[1] == "--U":
        print(f"Usage : python {sys.argv[0]} Folder_Name")
        return

    # Folder name
    ProcessInfo(sys.argv[1])

    print(Border)
    print("--- Thank you for using our Automation System ---")
    print(Border)

if __name__ == "__main__":
    main()