#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 01:20:30 2020

@author: daryamalafeeva
"""

import math



"""---------------Функция перевода координат NMEA в радианы-----------------"""

def ddmm2rad(ddmm): 
    #coordinates ddmm.mm -> rad
    dd_only = math.floor(ddmm/100)
    mm_only = ddmm - dd_only*100
    degrees = dd_only + mm_only/60
    rad = math.radians(degrees)
    return(rad)


""""-------Функция преобразования координат в СК wgs-84 в СК ECEF-----------"""


#  Передаваемые в функцию параметры: lat - широта (РАД),
# lon - долгота (РАД), h - высота (м)
# функция возвращает координаты x,y,z в метрах, ECEF

# константы

a     = 6378137.0         # большая полуось Земли для WGS-84 (м)
b     = 6356752.314245    # малая полуось
f     = (a - b) / a       # Ellipsoid Flatness
f_inv = 1.0 / f           # WGS-84 Flattening Factor of the Earth

a_sq = a * a
b_sq = b * b
e_sq = f * (2 - f)        # Square of Eccentricity


def wgs84_2ecef(lat, lon, h):
    
    s = math.sin(lat)
    N = a / math.sqrt(1 - e_sq * s * s)
    
    sin_lambda = math.sin(lat)
    cos_lambda = math.cos(lat)
    
    sin_phi    = math.sin(lon)
    cos_phi    = math.cos(lon)
    
    x          = (h + N) * cos_lambda * cos_phi
    y          = (h + N) * cos_lambda * sin_phi
    z          = (h + (1 - e_sq) * N) * sin_lambda
    return([x, y, z])
    

