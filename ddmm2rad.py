#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 01:20:30 2020

@author: daryamalafeeva
"""

import math
def func(ddmm): 
    #coordinates ddmm.mm -> rad
    dd_only = math.floor(ddmm/100)
    mm_only = ddmm - dd_only*100
    degrees = dd_only + mm_only/60
    rad = math.radians(degrees)
    return(rad)
    
