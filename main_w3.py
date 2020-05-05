import numpy as np
import math
import read_codes


"""-------------------Параметры для моделирования---------------------------"""
f_0      = 1575.42 * 1e6  # несущая частота
A        = 1              # амплитуда каждой из компонент

delta_f  = 24.552 * 1e6   # ширина полосы       
f_d      = 4 * delta_f    # частота дисретизации               
T_d      = 1 / f_d        # период дискретизации                  
f_if     = f_d / 4        # промежуточная частота                 

mod_time = 20*1e-3        # время моделирования

amount_k = mod_time / T_d # количество отсчетов

"""---------------------------Дальномерные коды----=========----------------"""

G_E1_B_list_str  = list(format(int(read_codes.G_E1_B_16, 16), '4092b'))
G_E1_B_list_int  = [int(x) for x in G_E1_B_list_str]
G_E1_B_array     = np.array((G_E1_B_list_int))

G_E1_C_list_str  = list(format(int(read_codes.G_E1_C_16, 16), '4092b'))
G_E1_C_list_int  = [int(x) for x in G_E1_C_list_str]
G_E1_C_array     = np.array((G_E1_C_list_int))

