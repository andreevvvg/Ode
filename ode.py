# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:17:55 2022

@author: andre
"""
import numpy as np

u0 = 1.7
v0 = 0
t_begin = 0
t_end = 20
f1 = open('de_data.txt','w')
f05 = open('de05_data.txt','w')
f01 = open('de01_data.txt','w')

f12 = open('de_data2.txt','w')
f052 = open('de05_data2.txt','w')
f012 = open('de01_data2.txt','w')

f11 = open('de_data1.txt','w')
f051 = open('de05_data1.txt','w')
f011 = open('de01_data1.txt','w')

f_error = open('de_error.txt','w')

# eu - во сколько раз шаг по схеме Эйлера меньше, чем шаг в схеме с перешагиванием
def solve (dt,f,eu):  
    N = int((t_end-t_begin)/dt) + 1
    
    u = np.zeros(N)
    v = np.zeros(N)
    
    epsilon = np.zeros(N)
    t = np.linspace(t_begin,t_end,N)
    
    u_eu = np.zeros(eu+1)
    v_eu = np.zeros(eu+1)
    
    # аналитическое решение
    u_a = np.zeros(N)
    u_a[:] = u0 * np.cos(t)
    
    u_eu[0] = u0
    v_eu[0] = v0
    
    # схема Эйлера
    for i in range(0,eu):
        u_eu[i+1] = u_eu[i] + v_eu[i]*dt/eu
        v_eu[i+1] = v_eu[i] - u_eu[i]*dt/eu
    
    u[0] = u_eu[0]
    v[0] = v_eu[0]
    u[1] = u_eu[-1]
    v[1] = v_eu[-1]
    
    # Схема с перешагиванием
    for i in range (1,N-1):
        u[i+1] = u[i-1] + v[i]*2*dt
        v[i+1] = v[i-1] - u[i]*2*dt
       
    # рассчет ошибки
    for i in range (0,N):
        epsilon[i] = u[i] - u_a[i]

    #ввывод в файл
    for i in range (0,N): 
        f.write(str(t[i]) + '\t' + str(u[i]) + '\t' + str(v[i]) + '\t' + str(u_a[i]) + '\n')
    
    return t,epsilon

t1,ep1 = solve(1,f1,1)
t2,ep2 = solve(0.5,f05,1)
t3,ep3 = solve(0.1,f01,1)

solve(1,f12,2)
solve(0.5,f052,2)
solve(0.1,f012,2)

solve(1,f11,10)
solve(0.5,f051,10)
solve(0.1,f011,10)

# ввывод ошибки в файл
for i in range (0,t3.size): 
    if i<t1.size:
        s1 = str(t1[i]) + '\t' + str(ep1[i]) + '\t'
    else:
        s1 = str(0) + '\t' + str(0) + '\t'
    if i<t2.size:
        s2 = str(t2[i]) + '\t' + str(ep2[i]) + '\t'
    else:
        s2 = str(0) + '\t' + str(0) + '\t'
    f_error.write(s1 + s2 + str(t3[i]) + '\t' + str(ep3[i]) + '\n')

f1.close()
f05.close()
f01.close()
f12.close()
f052.close()
f012.close()
f11.close()
f051.close()
f011.close()
f_error.close()










