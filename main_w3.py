import numpy as np
import math
import numpy.matlib
import read_codes
import matplotlib.pyplot as plt


# функция преобразования модулирующей последовательности к виду +1,-1
def convert_val(mod_sequence, mod_sequence_new):
#    mod_sequence_new = []
    for item in mod_sequence:
        if item == 0:
            mod_sequence_new.append(1)
        else:
            mod_sequence_new.append(-1)



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
G_E1_B_list_str  = list(format(int(read_codes.G_E1_B_16, 16), '04092b'))
G_E1_B_list_int  = [int(x) for x in G_E1_B_list_str]

# преобразуем к виду +1,-1
G_E1_B_list_int_new = []
convert_val(G_E1_B_list_int, G_E1_B_list_int_new)

G_E1_B_array     = np.array((G_E1_B_list_int_new))
# повторение элементов ДК на время моделирования (5 периодов ДК за 20 мс)
G_E1_B_full      = np.transpose(numpy.matlib.repmat(G_E1_B_array, 1, int(mod_time /T_dk)))
# согласовываем чипы последовательностей
G_E1_B           = np.repeat(G_E1_B_full, math.ceil(amount_k/ len(G_E1_B_full)))


G_E1_C_list_str  = list(format(int(read_codes.G_E1_C_16, 16), '04092b'))
G_E1_C_list_int  = [int(x) for x in G_E1_C_list_str]

G_E1_C_list_int_new = []
convert_val(G_E1_C_list_int, G_E1_C_list_int_new)

G_E1_C_array     = np.array((G_E1_C_list_int))
G_E1_C_full      = np.transpose(np.matlib.repmat(G_E1_C_array,1, int(mod_time /T_dk)))
G_E1_C           = np.repeat(G_E1_C_full, math.ceil(amount_k/ len(G_E1_C_full)))

""""---------------------------Оверлейный код-------------------------------"""
# параметры оверлейного кода
T_ok             = 100 * 1e-3 # период ОК
tau_ok           = 4 * 1e-3   # длительность элементарного символа ОК

G_OK_list_str  = list(format(int(read_codes.G_OK_16, 16), '028b'))

# за время 20 мс пройдет 5 бит ОК, тогда нам надо их достать и растянуть
del(G_OK_list_str[5::])
G_OK_list_int  = [int(x) for x in G_OK_list_str]

G_OK_list_int_new = []
convert_val(G_OK_list_int, G_OK_list_int_new)

G_OK_array     = np.array((G_OK_list_int))
G_OK_full      = np.transpose(G_OK_array)
G_OK           = np.repeat(G_OK_full, math.ceil(amount_k/ len(G_OK_full)))

"""-----------------------Навигационное сообщение---------------------------"""
tau_nd = 4 * 1e-3        # длительность одного символа

G_nd_list = []
for j in range(int(mod_time / tau_nd)):
    if j % 2 == 0: 
        G_nd_list.append(1)
    else:
        G_nd_list.append(0)
        
G_nd_list_new = []
convert_val(G_nd_list, G_nd_list_new)       
        
G_nd_array = np.array(G_nd_list)
G_nd       = np.repeat(G_nd_array, math.ceil(amount_k/ len(G_nd_array)))

"""------------------------Цифровые поднесущие-----------------------------"""
# параметры для формирования
alpha  = math.sqrt(10/11)
beta   = math.sqrt(1/11)

R_sc_1 = 1.023 * 1e6     # частота sc1
R_sc_6 = 6.138 * 1e6     # частота sc6


"""-------------------Формирование поднесущих и сигнала---------------------"""

# # фунция прямоугольника
# def rect(x):
#     if x == 0:
#         return 1
#     elif x <= tau_dk:
#         return 0

S_E1_BC_list  = []
sc_1_list     = []
sc_6_list     = []
pilot_list    = []
data_list     = []

sc_plus_list  = []
sc_minus_list = []

s_e1_bc_list  = []

amount_k_list = [i for i in range(0,amount_k)]
for k in amount_k_list:
    
 # e1_b = G_E1_B[k] * G_nd[k] * rect(k * T_d - T_dk)
    
 # e1_c = G_E1_B[k] * rect(k * T_d - T_dk)
    
 # sc_1 = np.sign(math.sin(2 * math.pi * R_sc_1) * k *T_d)
    
 # sc_6 = np.sign(math.sin(2 * math.pi * R_sc_6) * k *T_d)  
 
 # s_e1_bc = (A/(math.sqrt(2)))  * e1_b * (alpha * sc_1 + beta * sc_6) -\
 # e1_c * (alpha * sc_1 - beta * sc_6)
  
 # s_e1_bc_list.append(s_e1_bc)      
    
       
    # формируем цифровые поднесущие
    sc_1 = np.sign(math.sin(2 * math.pi * R_sc_1 * k * T_d))
    sc_1_list.append(sc_1)
    
    sc_6 = np.sign(math.sin(2 * math.pi * R_sc_6 * k * T_d))
    sc_6_list.append(sc_6)
    
    # для проверки правильности цифровой поднесущей
    sc_plus = (alpha * sc_1) + (beta * sc_6) 
    sc_plus_list.append(sc_plus)    
    
    sc_minus = (alpha * sc_1) - (beta * sc_6) 
    sc_minus_list.append(sc_minus)    
    
    
    # формируем сигнал
    data = G_E1_B[k] * G_nd[k] * sc_plus
    data_list.append(data)
    
    pilot  = G_E1_C[k] * G_OK[k] * sc_minus
    pilot_list.append(pilot)
    
    S_E1_BC = (A/(math.sqrt(2))) * (data - pilot) * (math.cos(2* math.pi * f_if * k * T_d))
    S_E1_BC_list.append(S_E1_BC)


"""------------------------------АКФ и графики------------------------------"""


# амплитудный спектр
S   = np.fft.fft(np.array(S_E1_BC_list))
ss  = S * S.conj()

# график энергетического спектра
fig = plt.figure(6)
plt.plot (ss,'r')
plt.grid()
plt.show()   

# акф
akf        = np.real(np.fft.ifft(ss))
akf2       = akf[::-1]
akf2_short = np.delete(akf2,-1)
akf_full   = np.concatenate((akf2_short, akf))
#samples    = np.arange(-10229, 10230, 1)

# график АКФ
fig = plt.figure(4)
plt.plot (akf_full,'r')
plt.grid()
plt.show()   

# цифровая поднесущая
fig = plt.figure(1)
plt.plot(amount_k_list, sc_plus_list,'r')
plt.xlabel ('k')
plt.ylabel('s_c_plus')
plt.grid()
plt.show() 

# цифровая поднесущая
fig = plt.figure(2)
plt.plot(amount_k_list, sc_minus_list,'r')
plt.xlabel ('k')
plt.ylabel('s_c_minus')
plt.grid()
plt.show() 


fig = plt.figure(3)
plt.plot(amount_k_list,G_OK,'r')
plt.xlabel ('k')
plt.ylabel('S_E1_BC')
plt.grid()
plt.show() 
