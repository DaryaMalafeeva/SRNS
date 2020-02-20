#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:07:52 2020

@author: daryamalafeeva
""" 

# almanac reading

str_1                   = open('Legacy_130122.agl').read().split('\n')[0]
str_1_massive           = str_1.split()
get_date                    = float(str_1_massive[0])
get_mounth              = float(str_1_massive[1])
get_year                = float(str_1_massive[2])
time_from_day_start     = float(str_1_massive[3])

str_2                   = open('Legacy_130122.agl').read().split('\n')[1]
str_2_massive           = str_2.split()
NKA_num                 = float(str_2_massive[0])
freq_sloth_num          = float(str_2_massive[1])
health_sign             = float(str_2_massive[2])
date                    = float(str_2_massive[3])
mounth                  = float(str_2_massive[4])
year                    = float(str_2_massive[5])
time_of_first_node      = float(str_2_massive[6])
gln_utc_corr            = float(str_2_massive[7])
gps_gln_corr            = float(str_2_massive[8])
NKA_corr                = float(str_2_massive[9])

str_3                   = open('Legacy_130122.agl').read().split('\n')[2]
str_3_massive           = str_3.split()
Lam                     = float(str_3_massive[0])
dI                      = float(str_3_massive[1])
w                       = float(str_3_massive[2])
E                       = float(str_3_massive[3])
dT                      = float(str_3_massive[4])
dTT                     = float(str_3_massive[5])
