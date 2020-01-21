import time
import os
import sys

def create_reminder_entry():

    print("null")

def find_time():
    local_time = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", local_time)
    print(time_string)
    print("I work!")

def reminder():

    print("I work too!")

def help():

    print("help")

def main():
    #(future) Usage reminder.py [-h][-t][-i]   
    # (help, find time, remind input,)
    find_time()


main()