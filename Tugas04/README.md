# SistemPakar-NurulKamila-1184038-
# Kode program ini diambil dari https://gist.github.com/mvidalgarcia/5a157afa6b275d058126
# Kode program dibawah ini menggunakan algoritma fuzzy sugeno 

# mengimport library numpy,skfuzzy
import numpy as np
import skfuzzy as fuzz
# Generate semua variabel
x_temp = np.arange(-20, 41, 1)
x_hum = np.arange(0, 101, 1)
x_sys = np.arange(12, 36, 1)
 
print("x_temp: " + str(x_temp))
print("x_hum: " + str(x_hum))
print("x_sys: " + str(x_sys))

# Hasilkan fungsi keanggotaan fuzzy
temp_lo = fuzz.trimf(x_temp, [-20, -20, 5])
print("temp_lo: " + str(temp_lo))
temp_md = fuzz.trimf(x_temp, [0, 10, 20])
print("temp_md: " + str(temp_md))
temp_hi = fuzz.trimf(x_temp, [15, 40, 40])
print("temp_hi: " + str(temp_hi))
 
hum_lo = fuzz.trimf(x_hum, [0, 0, 50])
print("hum_lo: " + str(hum_lo))
hum_md = fuzz.trimf(x_hum, [30, 45, 60])
print("hum_md: " + str(hum_md))
hum_hi = fuzz.trimf(x_hum, [55, 100, 100])
print("hum_hi: " + str(hum_hi))
 
 
sys_cool2 = fuzz.trimf(x_sys, [12, 12, 15])
print("sys_cool2: " + str(sys_cool2))
sys_cool1 = fuzz.trimf(x_sys, [14, 15.5, 17])
print("sys_cool1: " + str(sys_cool1))
sys_off = fuzz.trimf(x_sys, [16, 18.5, 21])
print("sys_off: " + str(sys_off))
sys_heat1 = fuzz.trimf(x_sys, [20, 24, 28])
print("sys_heat1: " + str(sys_heat1))
sys_heat2 = fuzz.trimf(x_sys, [26, 35, 35])
print("sys_heat2: " + str(sys_heat2))

# saya membutuhkan aktivasi fungsi keanggotaan fuzzy saya pada nilai-nilai ini.
# Nilai pasti temp = 36 dan hum = 7.2 tidak ada di alam semesta kita ...
# Untuk itulah fuzz.interp_membership ada!
temp_level_lo = fuzz.interp_membership(x_temp, temp_lo, CURRENT_TEMP)
print("temp_level_lo: " + str(temp_level_lo))
temp_level_md = fuzz.interp_membership(x_temp, temp_md, CURRENT_TEMP)
print("temp_level_md: " + str(temp_level_md))
temp_level_hi = fuzz.interp_membership(x_temp, temp_hi, CURRENT_TEMP)
print("temp_level_hi: " + str(temp_level_hi))
 
hum_level_lo = fuzz.interp_membership(x_hum, hum_lo, CURRENT_HUM)
print("hum_level_lo: " + str(hum_level_lo))
hum_level_md = fuzz.interp_membership(x_hum, hum_md, CURRENT_HUM)
print("hum_level_md: " + str(hum_level_md))
hum_level_hi = fuzz.interp_membership(x_hum, hum_hi, CURRENT_HUM)
print("hum_level_hi: " + str(hum_level_hi))
 
results = dict()

# Sekarang saya mengambil aturan saya dan menerapkannya.
# Aturan 1: temp_lo -> heat2
sys_activation_heat2 = np.fmin(temp_level_lo, sys_heat2)
active_rule1 = temp_level_lo
print("\nactive_rule1: " + str(active_rule1))
print("sys_activation_heat2: " + str(sys_activation_heat2))
results['active_rule1'] = active_rule1

# Aturan 2: temp_md & hum_hi -> heat1
active_rule2 = np.fmin(temp_level_md, hum_level_hi)
print("\nactive_rule2: " + str(active_rule2))
 
sys_activation_heat1 = np.fmin(active_rule2, sys_heat1)
print("sys_activation_heat1: " + str(sys_activation_heat1))
results['active_rule2'] = active_rule2

# Aturan 3: temp_md & (hum_md || hum_lo) -> mati
hum_combined = np.fmax(hum_level_md, hum_level_lo) 
# atau
print("\nhum_combined: " + str(hum_combined))
active_rule3 = np.fmin(temp_level_md, hum_combined) 
# dan
print("active_rule3: " + str(active_rule3))
sys_activation_off = np.fmin(active_rule3, sys_off)
print("sys_activation_off: " + str(sys_activation_off))
results['active_rule3'] = active_rule3

# Aturan 4: temp_hi & hum_lo -> cool1
active_rule4 = np.fmin(temp_level_hi, hum_level_lo) 
# dan
print("\nactive_rule4: " + str(active_rule4))
 
sys_activation_cool1 = np.fmin(active_rule4, sys_cool1)
print("sys_activation_cool1: " + str(sys_activation_cool1))
results['active_rule4'] = active_rule4

# Aturan 5: temp_hi & (hum_md || hum_hi) -> cool2
hum_combined = np.fmax(hum_level_md, hum_level_hi) 
# atau
print("\nhum_combined: " + str(hum_combined))
active_rule5 = np.fmin(temp_level_hi, hum_combined) 
# dan
print("active_rule5: " + str(active_rule5))
sys_activation_cool2 = np.fmin(active_rule5, sys_cool2)
print("sys_activation_cool2: " + str(sys_activation_cool2))
results['active_rule5'] = active_rule5
 
sys0 = np.zeros_like(x_sys)
print("sys0: " + str(sys0))

# Gabungkan kelima fungsi keanggotaan keluaran bersama-sama
aggregated = np.fmax(sys_activation_cool2, np.fmax(sys_activation_cool1, np.fmax(sys_activation_heat2,
 np.fmax(sys_activation_heat1, sys_activation_off))))
print("\naggregated: " + str(aggregated))

# Hitung hasil defuzzifikasi
sys_temp = fuzz.defuzz(x_sys, aggregated, 'centroid')
print("\nsys_temp: " + str(sys_temp))
 
print(results)
