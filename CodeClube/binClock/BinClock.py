__author__ = 'Marva'
import time
from datetime import datetime


def main():
    while(True):
        ltime=gettime()
        bin_repr=time_to_bin_repr(ltime)
        print_clock_face(bin_repr)
        time.sleep(1)


def gettime():
    curr_time = datetime.now()
    timeHour = str(curr_time.hour)
    timeMinute = str(curr_time.minute)
    timeSec = str(curr_time.second)

    massiiv = [timeHour,timeMinute,timeSec]
    return massiiv

def _int_to_digits(time_int):
    if len(time_int)<2:
        time_tens = 0
        time_ones = int(time_int)
    else:
        time_tens = int(time_int[0])
        time_ones = int(time_int[1])
    massiiv = [time_tens,time_ones]
    return massiiv


def _digits_to_bin(digit):
    bin_time=bin(digit)[2:].zfill(4)
    massiiv =[int(bin_time[0]),int(bin_time[1]),int(bin_time[2]),int(bin_time[3])]
    return massiiv



def time_to_bin_repr(time):
    digits_time_hour = _int_to_digits(time[0])
    digits_time_minute = _int_to_digits(time[1])
    digits_time_sec = _int_to_digits(time[2])

    bin_time_hour_tens=_digits_to_bin(digits_time_hour[0])
    bin_time_hour_ones=_digits_to_bin(digits_time_hour[1])
    bin_time_minute_tens=_digits_to_bin(digits_time_minute[0])
    bin_time_minute_ones=_digits_to_bin(digits_time_minute[1])
    bin_time_sec_tens=_digits_to_bin(digits_time_sec[0])
    bin_time_sec_ones=_digits_to_bin(digits_time_sec[1])

    kell = {
            "hours_tens":bin_time_hour_tens,
            "hours_ones":bin_time_hour_ones,
            "minute_tens":bin_time_minute_tens,
            "minute_ones":bin_time_minute_ones,
            "sec_tens":bin_time_sec_tens,
            "sec_ones":bin_time_sec_ones
    }
    return kell

def print_clock_face(time):
    print(time)



main()

