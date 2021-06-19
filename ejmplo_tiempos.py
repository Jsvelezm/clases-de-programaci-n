# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:23:43 2021

@author: USUARIO
"""


import numpy as np

n = 1000

A = np.random.randint(0, 15, size=(n,1))

B = np.random.randint(0, 15, size =(1,n))



import time

tini = time.process_time()

for i in range(n):
    aux =[]
    for j in range(n):
        aux = A[i][0]*B[0].tolist()
        #print(aux)
        
tfin = time.process_time()


print(1000*(tfin - tini))  
 



tini = time.process_time()

      
res = np.matmul(A,B)

tfin = time.process_time()

print(1000*(tfin - tini))  
