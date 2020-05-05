import numpy as np
import math
import numpy.matlib
import read_codes


"""-------------------Параметры для моделирования---------------------------"""
f_0      = 1575.42 * 1e6  # несущая частота
A        = 1              # амплитуда каждой из компонент

delta_f  = 24.552 * 1e6   # ширина полосы       
f_d      = 4 * delta_f    # частота дисретизации               
T_d      = 1 / f_d        # период дискретизации                  
f_if     = f_d / 4        # промежуточная частота                 

mod_time = 20*1e-3        # время моделирования

amount_k = int(mod_time / T_d) # количество отсчетов

"""---------------------------Дальномерные коды-----------------------------"""
# параметры дальномерных кодов
T_dk   = 4 * 1e-3        # период ДК
tau_dk = (1/1023) * 1e-3 # длительность элементарного символа ДК

# перевод в двоичную систему
G_E1_B_list_str  = list(format(int(read_codes.G_E1_B_16, 16), '4092b'))
G_E1_B_list_int  = [int(x) for x in G_E1_B_list_str]
G_E1_B_array     = np.array((G_E1_B_list_int))
# повторение элементов ДК на время моделирования
G_E1_B_full      = numpy.matlib.repmat(G_E1_B_array, 1, int(mod_time /T_dk))

G_E1_C_list_str  = list(format(int(read_codes.G_E1_C_16, 16), '4092b'))
G_E1_C_list_int  = [int(x) for x in G_E1_C_list_str]
G_E1_C_array     = np.array((G_E1_C_list_int))
G_E1_C_full      = numpy.matlib.repmat(G_E1_C_array, 1, int(mod_time /T_dk))



#G_E1_C = np.repeat(G_E1_C_full, math.ceil(amount_k/ len(G_E1_C_full)))


""""---------------------------Оверлейный код-------------------------------"""
# параметры оверлейного кода
T_ok   = 100 * 1e-3 # период ОК
tau_ok = 4 * 1e-3   # длительность элементарного символа ОК

G_OK_list_str  = list(format(int(read_codes.G_OK_16, 16), '028b'))
del(G_OK_list_str[25::])
G_OK_list_int  = [int(x) for x in G_OK_list_str]
G_OK_array     = np.array((G_OK_list_int))

# повторение элементов ДК на время моделирования
if int(mod_time /T_ok) == 0:
    num_of_repeat_ok = 1
else:
    num_of_repeat_ok = int(mod_time /T_ok)
G_OK_full      = numpy.matlib.repmat(G_OK_array, 1, num_of_repeat_ok)


"""------------------------Цифровые поднесущие-----------------------------"""
# параметры для формирования
alpha = math.sqrt(10/11)
beta  = math.sqrt(1/11)

T_sc_1 = (1/1023) *1e-6  # период sc1
R_sc_1 = 1 / T_sc_1      # частота sc1

T_sc_6 = (1/6138) *1e-6  # период sc6
R_sc_6 = 1 / T_sc_6      # частота sc6


amount_k_list = [i for i in range(0,amount_k)]

"""-----------------------Навигационное сообщение---------------------------"""
tau_nd = 4 * 1e-3        # длительность одного символа
G_nd_list = []
for j in range(int(mod_time / tau_nd)):
    if j % 2 == 0: 
        G_nd_list.append(1)
    else:
        G_nd_list.append(0)
G_nd_array = np.array(G_nd_list)

for k in amount_k_list:
     
    # формируем цифровые поднесущие
    sc_1 = np.sign(math.sin(2* math.pi * R_sc_1 * (k-1) * T_d))
    
    sc_6 = np.sign(math.sin(2* math.pi * R_sc_6 * (k-1) * T_d))
    







