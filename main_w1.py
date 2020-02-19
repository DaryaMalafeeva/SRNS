#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:39:25 2020

@author: daryamalafeeva
"""
import almanac_reading as alm

# current UTC time
year_UTC       = 2013
mounth_UTC     = 1.0
day_UTC        = 22.0
hours_UTC      = 14.0
minutes_UTC    = 5.0
seconds_UTC    = 0.0

# current UTC_SU time
year_UTC_SU    = year_UTC
mounth_UTC_SU  = mounth_UTC
day_UTC_SU     = day_UTC
hours_UTC_SU   = hours_UTC 
minutes_UTC_SU = minutes_UTC
seconds_UTC_SU = seconds_UTC

UTC_TIME       = str(int(year_UTC)) + str('.') + str(int(mounth_UTC)) + str('.') + str(int(day_UTC)) + \
str('  ') + str(int(hours_UTC)) + str('.') + str(int(minutes_UTC)) + str('.') + str(int(seconds_UTC))
print('UTC time is ' + UTC_TIME)

# converting current UTC time to GLN system time
year_GLN       = year_UTC_SU
mounth_GLN     = mounth_UTC_SU
day_GLN        = day_UTC_SU
hours_GLN      = hours_UTC_SU + 3.0
minutes_GLN    = minutes_UTC_SU
seconds_GLN    = seconds_UTC_SU

GLN_TIME       = str(int(year_GLN)) + str('.') + str(int(mounth_GLN)) + str('.') + str(int(day_GLN)) + \
str('  ') + str(int(hours_GLN)) + str('.') + str(int(minutes_GLN)) + str('.') + str(int(seconds_GLN))
print('GLN time is ' + GLN_TIME)

N_4 = int(5) #for 2013
N_t = int(366 * 1 + 22)
t   = int((14 * 60 * 60) + (5 * 60))

print('GLONASST is ' + str(N_4) + str(':') + str(N_t) + str(':') + str(t))

# converting current UTC time to GPS system time
leap_sec_corr_GPS = 16 #for 2013
year_GPS          = year_UTC
mounth_GPS        = mounth_UTC
day_GPS           = day_UTC
hours_GPS         = hours_UTC + 0.0
minutes_GPS       = minutes_UTC
seconds_GPS       = seconds_UTC + leap_sec_corr_GPS

GPS_TIME          = str(int(year_GPS)) + str('.') + str(int(mounth_GPS)) + str('.') + str(int(day_GPS)) + \
str('  ') + str(int(hours_GPS)) + str('.') + str(int(minutes_GPS)) + str('.') + str(int(seconds_GPS))
print('GPS time is ' + GPS_TIME)

WN_GPS               = int(1724)
TOW_5day_00_00_00    = int(172800)
TOW_GPS              = int(TOW_5day_00_00_00 + (5 * 60 * 60))

print('GPST time is ' + str(WN_GPS) + str(':') + str(TOW_GPS))

#print(alm.get_date)

# converting current UTC time to GALILEO system time
leap_sec_corr_GLL = 16 #for 2013
year_GLL          = year_UTC
mounth_GLL        = mounth_UTC
day_GLL           = day_UTC
hours_GLL         = hours_UTC + 0.0
minutes_GLL       = minutes_UTC
seconds_GLL       = seconds_UTC + leap_sec_corr_GPS

GLL_TIME          = str(int(year_GLL)) + str('.') + str(int(mounth_GLL)) + str('.') + str(int(day_GLL)) + \
str('  ') + str(int(hours_GLL)) + str('.') + str(int(minutes_GLL)) + str('.') + str(int(seconds_GLL))
print('GALILEO time is ' + GLL_TIME)

WN_GLL               = int(1024)
TOW_5day_00_00_00    = int(172800)
TOW_GLL              = int(TOW_5day_00_00_00 + (5 * 60 * 60))

print('GST time is ' + str(WN_GLL) + str(':') + str(TOW_GLL))

