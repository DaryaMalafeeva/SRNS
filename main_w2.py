import numpy as np
import matplotlib.pyplot as plt

# начальное состояние первого регистра
g_1   = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0] 
# начальное состояние второго регистра
g_2   = [1, 0, 0, 0, 0, 0, 1]
# длина ДК
N_prn = 10230
#массив элементов ДК
prn   = [0] * N_prn

for k in range(N_prn):
    # ДК
    prn[k]  = g_1[-1] ^ g_2[-1]  
    # формируем новый элемент первого регистра
    g_1_new = g_1[4-1] ^ g_1[8-1] ^ g_1[13-1] ^ g_1[14-1]
    # присоединям новый элемент массива и выкидываем последний
    g_1     = [g_1_new] + g_1[0:-1]
    g_2_new = g_2[6-1] ^ g_2[7-1]   
    g_2     = [g_2_new] + g_2[0:-1]  
    
# проверяем символы ДК с ИКД
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n    = int(num, from_base)
    else:
        n    = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    
first32_ikd = [int(item) for item in list(convert_base('9FB9299B', from_base=16, to_base=2))]
first32_got = prn[0:32]

last32_ikd  = [int(item) for item in list(convert_base('86EBE41A', from_base=16, to_base=2))]
last32_got  = prn[-32::]

# сравниваем два массива
if first32_got == first32_ikd:
    print( 'Первые 32 символа ДК совпадают с ИКД')
else:
    print('Ошибка: в первых 32 символах есть несовпадение с ИКД')

if last32_got == last32_ikd:
    print( 'Последние 32 символа ДК совпадают с ИКД')
else:
    print('Ошибка: в последних 32 символах есть несовпадение с ИКД')
    
# список элементов ДК в виде +1 и -1
prn_new = []
for item in prn:
    if item == 0:
        prn_new.append(1)
    else:
        prn_new.append(-1)
      
# амплитудный спектр
S          = np.fft.fft(np.array(prn_new))
ss         = S * S.conj()

# акф
akf        = np.real(np.fft.ifft(ss))
akf2       = akf[::-1]
akf2_short = np.delete(akf2,-1)
akf_full   = np.concatenate((akf2_short, akf))
samples    = np.arange(-10229, 10230, 1)
A_max      = np.amax(abs(akf_full))

# график АКФ
fig = plt.figure(1)
plt.plot(samples, akf_full,'r')
plt.xlabel ('τ')
plt.ylabel('ρ(τ)')
plt.grid()
plt.show()   

   
