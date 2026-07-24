"""
Module Name : Scheduler.py

Description :
This module schedules the duplicate file
removal process after every specified interval.
"""

import schedule
import time


#----------------------------------------------------------
# Function Name : StartScheduler
# Description   : Executes the given function periodically
# Input         : Interval (Minutes)
#                 Function Name
# Output        : None
#----------------------------------------------------------

def StartScheduler(TimeInterval, TaskFunction):

    # Schedule the task
    schedule.every(TimeInterval).minutes.do(TaskFunction)

    print("---------------------------------------------")
    print("Duplicate File Removal Scheduler Started...")
    print("Running every", TimeInterval, "minute(s)")
    print("Press Ctrl + C to stop.")
    print("---------------------------------------------")

    while True:

        schedule.run_pending()

        time.sleep(1)


#----------------------------------------------------------
# Testing
#----------------------------------------------------------
"""
def Demo():

    print("Task Executed...")


if __name__ == "__main__":

    StartScheduler(1, Demo)

"""