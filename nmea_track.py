#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:03:07 2020

@author: daryamalafeeva
"""

import codecs
import math
import functions2use
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

line_list      = []
lattitude_list = []
longitude_list = []
height_list    = []

x_ecef_list    = []
y_ecef_list    = []
z_ecef_list    = []


with codecs.open("/Users/daryamalafeeva/Desktop/SN_6703/rgfile_20191008_122907.txt", "r",encoding='utf-8', errors='ignore') as NMEA_log:
    for line in NMEA_log:
        if line.startswith('$PORZX'):
            str_massive_porzx     = line.split(',')
            
            
        if line.startswith('$GNGGA') or line.startswith('$GPGGA') or\
           line.startswith('$GLGGA') or line.startswith('$GAGGA'):
            str_massive     = line.split(',')
            get_latitude    = float(str_massive[2])
            get_longitude   = float(str_massive[4])
            get_height      = float(str_massive[9])
            
            # преобразуем формат ddmm в радианны
            lat = functions2use.ddmm2rad(get_latitude)
            lon = functions2use.ddmm2rad(get_longitude)
            
            # WGS-84 to ECEF
            
            ecef = functions2use.wgs84_2ecef(lat, lon, get_height)
            
            x_ecef = ecef[0]
            x_ecef_list.append(x_ecef)
            
            y_ecef = ecef[1]
            y_ecef_list.append(y_ecef)
            
            z_ecef = ecef[2]
            z_ecef_list.append(z_ecef)
            
            
#            get_latitude_ns = str_massive[3]
#            if get_latitude_ns == 'N':
            lattitude_list.append(lat)
#           elif get_latitude_ns == 'S':
            longitude_list.append(lon)
            height_list.append(get_height)
                
            
# построение трека НМ

fig_1 = plt.figure(1)
ax    = fig_1.add_subplot(projection=f'3d')
ax.plot(x_ecef_list, y_ecef_list, z_ecef_list, '*-', color = 'darkblue')

ax.set_xlabel('X, м')
ax.set_ylabel('Y, м')
ax.set_zlabel('Z, м')
plt.show()
