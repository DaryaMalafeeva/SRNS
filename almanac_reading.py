#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:07:52 2020

@author: daryamalafeeva
""" 

# almanac reading

str_1                   = open('Legacy_130122.agl').read().split('\n')[0]
str_1_massive           = str_1.split()
get_date                = float(str_1_massive[0])
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
time_lambda             = float(str_2_massive[6])
gln_utc_corr            = float(str_2_massive[7])
gps_gln_corr            = float(str_2_massive[8])
NKA_corr                = float(str_2_massive[9])

str_3                   = open('Legacy_130122.agl').read().split('\n')[2]
str_3_massive           = str_3.split()
lam_a                     = float(str_3_massive[0])
dI                      = float(str_3_massive[1])
w_a                       = float(str_3_massive[2])
E                       = float(str_3_massive[3])
dT                      = float(str_3_massive[4])
dTT                     = float(str_3_massive[5])


# из радиан в полуциклы: полуциклы умножить на пи получим радианы
# параметры в строке 3 заданы на момент времени из строки 2


## проверка по примеру икд
#time_lambda             = 33571.625
#
#lam_a                   = -0.293967247009277
#
#dI                      = -0.00012947082519531
#
#w_a                     = 0.57867431640625
#
#E                       = 0.000432968139648438
#
#dT                      =  0.01953124999975
#
#dTT                     =  6.103515625e-05
