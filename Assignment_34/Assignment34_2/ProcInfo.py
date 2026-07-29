"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

2. Design automation script which accept process name and display information of that process if it is running. 
Usage : ProcInfo.py Notepad
"""

import psutil
import logging
import os
import sys
import logging

# ----------------------------------------------------------
def CreateLog():
    if not os.path.exists("Log"):
        os.mkdir("Log")

    LogFile = os.path.join("Log", "ProcessLog.log")

    logging.basicConfig(
        filename=LogFile,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s",
        force=True
    )

# ----------------------------------------------------------
def ValidateProcessName(ProcessName):
    if ProcessName.strip() == "":
        return False
    return True

# ----------------------------------------------------------
def DisplayProcessInfo(ProcessName):
    Found = False

    try:
        for proc in psutil.process_iter(['pid', 'name', 'username']):

            try:
                if proc.info['name'] and proc.info['name'].lower() == ProcessName.lower():

                    logging.info("-" * 60)
                    logging.info("Process Found")
                    logging.info(f"Process Name : {proc.info['name']}")
                    logging.info(f"PID          : {proc.info['pid']}")
                    logging.info(f"User         : {proc.info['username']}")
                    logging.info("-" * 60)

                    Found = True

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

        if Found == False:
            logging.info(f"Process '{ProcessName}' is not running.")

    except Exception as e:
        logging.exception(e)


# ----------------------------------------------------------
def main():

    CreateLog()

    try:

        if len(sys.argv) != 2:
            logging.info(f"Usage : ProcInfo.py {ProcessName}")
            return

        ProcessName = sys.argv[1]

        if ValidateProcessName(ProcessName) == False:
            logging.info("Invalid Process Name")
            return

        DisplayProcessInfo(ProcessName)

    except Exception as e:
        logging.exception(e)

# ----------------------------------------------------------
if __name__ == "__main__":
    main()