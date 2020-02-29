#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:39:25 2020

@author: daryamalafeeva
"""
import almanac_reading as alm
import math


"""------------------------------TIME CALCULATION---------------------------"""

# current UTC time
year_UTC             = 2013
mounth_UTC           = 1.0
day_UTC              = 22.0
hours_UTC            = 14.0
minutes_UTC          = 5.0
seconds_UTC          = 0.0

# current UTC_SU time
year_UTC_SU          = year_UTC
mounth_UTC_SU        = mounth_UTC
day_UTC_SU           = day_UTC
hours_UTC_SU         = hours_UTC 
minutes_UTC_SU       = minutes_UTC
seconds_UTC_SU       = seconds_UTC

UTC_TIME             = str(int(year_UTC)) + str('.') + str(int(mounth_UTC)) + str('.') + str(int(day_UTC)) + \
str('  ') + str(int(hours_UTC)) + str(':') + str(int(minutes_UTC)) + str(':') + str(int(seconds_UTC))
print('UTC time is ' + UTC_TIME)

# converting current UTC time to GLN system time
year_GLN             = year_UTC_SU
mounth_GLN           = mounth_UTC_SU
day_GLN              = day_UTC_SU
hours_GLN            = hours_UTC_SU + 3.0
minutes_GLN          = minutes_UTC_SU
seconds_GLN          = seconds_UTC_SU

GLN_TIME             = str(int(year_GLN)) + str('.') + str(int(mounth_GLN)) + str('.') + str(int(day_GLN)) + \
str('  ') + str(int(hours_GLN)) + str(':') + str(int(minutes_GLN)) + str(':') + str(int(seconds_GLN))
print('GLN time is ' + GLN_TIME)

N_4                  = int(5) #for 2013
N_t                  = int(366 * 1 + 22)
t                    = int((14 * 60 * 60) + (5 * 60))

print('GLONASST is ' + str(N_4) + str(':') + str(N_t) + str(':') + str(t))

# converting current UTC time to GPS system time
leap_sec_corr_GPS    = 16 #for 2013
year_GPS             = year_UTC
mounth_GPS           = mounth_UTC
day_GPS              = day_UTC
hours_GPS            = hours_UTC + 0.0
minutes_GPS          = minutes_UTC
seconds_GPS          = seconds_UTC + leap_sec_corr_GPS

GPS_TIME             = str(int(year_GPS)) + str('.') + str(int(mounth_GPS)) + str('.') + str(int(day_GPS)) + \
str('  ') + str(int(hours_GPS)) + str(':') + str(int(minutes_GPS)) + str(':') + str(int(seconds_GPS))
print('GPS time is ' + GPS_TIME)

WN_GPS               = int(1724)
TOW_5day_00_00_00    = int(172800) # for Tuesday
TOW_GPS              = int(TOW_5day_00_00_00 + (14 * 60 * 60) + (5 * 60))

print('GPST time is ' + str(WN_GPS) + str(':') + str(TOW_GPS))

# converting current UTC time to GALILEO system time
leap_sec_corr_GLL    = 16 #for 2013
year_GLL             = year_UTC
mounth_GLL           = mounth_UTC
day_GLL              = day_UTC
hours_GLL            = hours_UTC + 0.0
minutes_GLL          = minutes_UTC
seconds_GLL          = seconds_UTC + leap_sec_corr_GPS

GLL_TIME             = str(int(year_GLL)) + str('.') + str(int(mounth_GLL)) + str('.') + str(int(day_GLL)) + \
str('  ') + str(int(hours_GLL)) + str(':') + str(int(minutes_GLL)) + str(':') + str(int(seconds_GLL))
print('GALILEO time is ' + GLL_TIME)

WN_GLL               = int(700)
TOW_5day_00_00_00    = int(172800)
TOW_GLL              = int(TOW_5day_00_00_00 + (14 * 60 * 60) + (5 * 60))

print('GST time is ' + str(WN_GLL) + str(':') + str(TOW_GLL))


"""---------------SATELLITE COORDINATES AND VELOCITY CALCULATION------------"""

# интервал прогноза
N_A     = 388 # номер недели внутри 4-х летнего периода относительно даты полуения альманаха

if N_t != 27:
    delta_N_A = N_t - N_A - round((N_t - N_A) / 1461) * 1461
elif N_4 == 27:
    delta_N_A = N_t - N_A - round((N_t - N_A) / 1461) * 1461
    
delta_t_pr = float(delta_N_A ) * 86400 + (float(t) - alm.time_lambda)

# количество целых витков на интервале прогноза
T_sr                  = 43200 #[с] 

W                     = int(delta_t_pr /(T_sr + alm.dT))

# текущее наклонение
i_sr                  = 63 #[deg]

i                     = ((i_sr/180) + alm.dI) * math.pi

# сред. драконич. период на витке W+1 и сред. движение
T_dr                  = T_sr + alm.dT + (2*W + 1) * alm.dTT

n                     = 2* math.pi / T_dr

# большая полуось орбиты
# в рассчитанном примере в икд болшая полуось орбиты на три знака меньше (но вроде у меня правильно 25 тыс км)
a_e                   = 6378136 # [м]

J_2_0                 = (1082.62575) * 10 ** -6
 
GM                    = (398600441) * 10 ** 6

T_osk_new             = T_dr

a_new                 = 1

a                     = 0

while abs(a_new - a) >= 0.001:
    a                 = a_new
    
    T_osk             = T_osk_new
    
    a_new             = ((((T_osk) / (2 * math.pi)) ** 2) * GM) ** (1./3)
    
    p_new             = a_new * (1 - ((alm.E) ** 2))
    
    znam_p1           = ((3/2) * J_2_0 * ((a_e) / (p_new))) ** 2
    
    znam_p2_1         = (2 - (5/2) * (math.sin(i) ** (2))) * \
                        (((1 - (alm.E ** 2)) ** (3./2)) / ((1 + alm.E * math.cos(alm.w_a * math.pi)) ** 2))    
    
    znam_p2_2         = (((1 + alm.E * math.cos(alm.w_a * math.pi)) ** 3) / (1 - alm.E ** 2))
    
    T_osk_new         = (T_dr) / (1 - ((znam_p1) * ((znam_p2_1) + (znam_p2_2))))

# текущее значение долготы восх. узла орбиты
w_z                   = (7.2921150) * 10 ** -5 #[рад/с]
lam                   = alm.lam_a * math.pi - (w_z + 3/2 *  J_2_0 * n * ((a_e / p_new) ** 2) * math.cos(i)) * delta_t_pr

# текущее значение аргумента перигея 
w_arg_per             = alm.w_a * math.pi - (3/4 * J_2_0 * n * ((a_e / p_new) ** 2) * (1 - 5 * math.cos(i) ** 2)) * delta_t_pr

# значение средней долготы на момент прохождения текущего восходящего узла
E_0                   = -2 * math.atan((((1 - alm.E) / (1 + alm.E)) ** 1/2)  * math.tan(w_arg_per /2))
L_1                   = w_arg_per + E_0 - alm.E * math.sin(E_0)

# текущее значение средней долготы НКА
L                     = L_1 + n * (delta_t_pr - (T_sr + alm.dT) * W - alm.dTT * (W **2))

# эксцентрическая аномалия
E                     = L - w_arg_per
E_new                 = E * 1.01
while abs(E_new - E) >= 10 ** -9:
    E                 = E_new
    E_new             = L - w_arg_per + alm.E * math.sin(E)

#  истинная аномалия v и аргумент широты НКА u
v                     = 2 *  math.atan((((1 - alm.E) / (1 - alm.E)) ** 1/2) * math.tan(E_new /2))
u                     = v + w_arg_per

# координаты центра масс НКА в ECEF
p                     = a_new * (1 - (alm.E ** 2))
r                     = p / (1 + alm.E * math.cos(v))

x_ti                  = r * (math.cos(lam) * math.cos(u) - math.sin(lam) * math.sin(u) * math.cos(i))
y_ti                  = r * (math.sin(lam) * math.cos(u) + math.cos(lam) * math.sin(u) * math.cos(i))
z_ti                  = r * (math.sin(u) * math.sin(i))



# проверка через высоту орбиты и радиус Земли
R_ti                  = (((x_ti) ** 2) + ((y_ti) ** 2) + ((z_ti) ** 2)) ** (1./2)  
R_Earth            = (6400) * 10 ** 3 
H_orbit             = R_ti - R_Earth
print('Calculated orbit height is: ' + str(H_orbit) + ' meters')
