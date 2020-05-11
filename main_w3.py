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

delta_f  = 14.322 * 1e6   # ширина полосы     
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


G_E1_C_list_str  = list(format(int(read_codes.G_E1_C_16, 16), '04092b'))
G_E1_C_list_int  = [int(x) for x in G_E1_C_list_str]

G_E1_C_list_int_new = []
convert_val(G_E1_C_list_int, G_E1_C_list_int_new)


""""---------------------------Оверлейный код-------------------------------"""
# параметры оверлейного кода
T_ok             = 100 * 1e-3 # период ОК
tau_ok           = 4 * 1e-3   # длительность элементарного символа ОК

G_OK_list_str    = list(format(int(read_codes.G_OK_16, 16), '028b'))

# за время 20 мс пройдет 5 бит ОК
del(G_OK_list_str[5::])
G_OK_list_int  = [int(x) for x in G_OK_list_str]

G_OK_list_int_new = []
convert_val(G_OK_list_int, G_OK_list_int_new)


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
        

"""------------------------Цифровые поднесущие-----------------------------"""
# параметры для формирования
alpha  = math.sqrt(10/11)
beta   = math.sqrt(1/11)

R_sc_1 = 1.023 * 1e6     # частота sc1
R_sc_6 = 6.138 * 1e6     # частота sc6


"""-------------------Формирование поднесущих и сигнала---------------------"""

S_E1_BC_list  = []
sc_1_list     = []
sc_6_list     = []
pilot_list    = []
data_list     = []

sc_plus_list  = []
sc_minus_list = []

s_e1_bc_list  = []

DKout_B_list  = []

DKout_C_list  = []

OKout_list    = []

NDout_list    = []

k = 0
t = 0
f = 0
N = round(f_d * mod_time)
tout = []
fout = []

while t < mod_time:
    
    
    
    # ДК
    Nchip_dk_B = int(abs((t/tau_dk) % len(G_E1_B_list_int_new))) 
    DKout_B = G_E1_B_list_int_new[Nchip_dk_B]
    DKout_B_list.append(DKout_B)
    
    Nchip_dk_C = int(abs((t/tau_dk) % len(G_E1_C_list_int_new))) 
    DKout_C = G_E1_C_list_int_new[Nchip_dk_C]
    DKout_C_list.append(DKout_C)
    
    # ОК
    Nchip_ok = int(abs((t/tau_ok) % len(G_OK_list_int_new))) 
    OKout = G_OK_list_int_new[Nchip_ok]
    OKout_list.append(OKout)
    
    # НС
    Nchip_nd = int(abs((t/tau_nd) % len(G_nd_list_new))) 
    NDout = G_nd_list_new[Nchip_nd]
    NDout_list.append(NDout)
    
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
    data = DKout_B * NDout * sc_plus
    data_list.append(data)
    
    pilot  = DKout_C * OKout * sc_minus
    pilot_list.append(pilot)
    
    S_E1_BC = (A/(math.sqrt(2))) * (data - pilot) * (math.cos(2* math.pi * f_if * k * T_d))
    S_E1_BC_list.append(S_E1_BC)
    
    t = k * T_d
    tout.append(t)
    
    f += 1/mod_time
    fout.append(f)
    
    k +=1

"""------------------------------АКФ и графики------------------------------"""


# амплитудный спектр всего сигнала
S   = np.fft.fft(np.array(S_E1_BC_list))
ss  = S * S.conj()
ss.transpose

# график энергетического спектра
fig = plt.figure(6)
plt.plot (fout, ss,'r')
plt.grid()
plt.show()   



# акф всего сигнала
akf        = np.real(np.fft.ifft(ss))
akf2       = akf[::-1]
akf2_short = np.delete(akf2,-1)
akf_full   = np.concatenate((akf2_short, akf))
#samples    = np.arange(-10229, 10230, 1)

# график АКФ всего сигнала
fig = plt.figure(4)
plt.plot (akf,'r')
plt.xlabel ('k')
plt.ylabel('АКФ S_E1_BC_list')
plt.grid()
plt.show()   

# амплитудный спектр ДК (B)
S_dk   = np.fft.fft(DKout_C_list)
ss_dk  = S_dk * S_dk.conj()

# акф ДК
akf_dk        = np.real(np.fft.ifft(ss_dk))
akf2_dk       = akf_dk[::-1]
akf2_short_dk = np.delete(akf2_dk,-1)
akf_full_dk   = np.concatenate((akf2_short_dk, akf_dk))
#samples    = np.arange(-10229, 10230, 1)

# график АКФ ДК
fig = plt.figure(7)
plt.plot (akf_full_dk,'r')
plt.xlabel ('k')
plt.ylabel('АКФ akf_full_dk')
plt.grid()
plt.show()  


# цифровая поднесущая
fig = plt.figure(1) 
plt.plot(sc_plus_list,'r')
plt.grid()
plt.show() 

# цифровая поднесущая
fig = plt.figure(2)
plt.plot(sc_minus_list,'r')

plt.grid()
plt.show() 

# сигнал
fig = plt.figure(3)
plt.plot(S_E1_BC_list,'r')
plt.grid()
plt.show() 

