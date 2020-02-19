#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:07:52 2020

@author: daryamalafeeva
""" 

# almanac reading

str_1                   = open('Legacy_130122.agl').read().split('\n')[0]
str_1_massive           = str_1.split()
get_date            = float(str_1_massive[0])
alm_get_mounth          = float(str_1_massive[1])
alm_get_year            = float(str_1_massive[2])
alm_time_from_day_start = float(str_1_massive[3])

str_2                   = open('Legacy_130122.agl').read().split('\n')[1]
str_2_massive           = str_2.split()
alm_NKA_num             = float(str_2_massive[0])
alm_freq_sloth_num      = float(str_2_massive[1])
alm_health_sign         = float(str_2_massive[2])
alm_date                = float(str_2_massive[3])
alm_mounth              = float(str_2_massive[4])
alm_year                = float(str_2_massive[5])
alm_time_of_first_node  = float(str_2_massive[6])
alm_gln_utc_corr        = float(str_2_massive[7])
alm_gps_gln_corr        = float(str_2_massive[8])
alm_NKA_corr            = float(str_2_massive[9])

str_3                   = open('Legacy_130122.agl').read().split('\n')[2]
str_3_massive           = str_3.split()
alm_Lam                 = float(str_3_massive[0])
alm_dI                  = float(str_3_massive[1])
alm_w                   = float(str_3_massive[2])
alm_E                   = float(str_3_massive[3])
alm_dT                  = float(str_3_massive[4])
alm_dTT                 = float(str_3_massive[5])
