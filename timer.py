#!/usr/bin/env python
# This is a timer program in which we calcluate time difference between start and stop time in seconds 
import time

start_time = time.localtime()
print("Start Time : " + time.strftime("%X",start_time))
raw_input("press 'enter' to stop the timer")
stop_time= time.localtime()
print("Stop    Time : " + time.strftime("%X", stop_time))
elapsed_time=time.mktime(stop_time) - time.mktime(start_time)
print("Elapsed Time : " + str(elapsed_time))
