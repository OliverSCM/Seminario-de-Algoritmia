# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:14:41 2023

@author: olive
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as manimation

import os

print(os.getcwd(),"-------")
#matplotlib.use('TkAgg')
random.seed(10)
np.random.seed(10)

def burbuja(lista):
    global contador1 
    lista1 = []
    tamanio = len(lista)
    sort = False
    lista1 = lista 
    for n in range(0, tamanio):
        # contador1 = 0
        if sort == True:
            break
        for b in range(0, tamanio-1):
            sort = True
            contador1 = contador1+1
            if lista1[b] > lista[b+1]:
                sort = False
                auxiliar = lista1[b]
                lista1[b] = lista1[b+1]
                lista1[b+1] = auxiliar 
    return lista1

def merge(array):
    global contador2
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge(L)
        merge(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                contador2+=1
            else:
                array[k] = M[j]
                j += 1
                contador2+=1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            contador2+=1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            contador2+=1
    return array

elementNumArray=np.arange(0, 1000, 1)
tiemposBurbuja=[]
iteracionesBurbujas=[]

tiemposMerge=[]
iteracionesMerge=[]

FFMpegWriter = manimation.writers['ffmpeg']

metadata = dict(title='tarea3', artist='Oliver Cruz',comment='tengo suenio')
writer = FFMpegWriter(fps=124, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,8))
ax1.title.set_text('Burbuja')
ax2.title.set_text('Merge')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")
               
with writer.saving(fig, "BubbleVsMerge.mp4", 100):

  plt.ion()
  for idx,elementNum in enumerate(elementNumArray):

    lista=[random.randint(1,1000) for i in range(elementNum)]
    #lista=[1,2,3,4,5,6,7,8,9]

    
    contador1 = 0
    contador2 = 0
          
    Burbuja = burbuja(lista)    
    iteracionesBurbujas.append(contador1)
          
    Merge = merge(lista) 
    iteracionesMerge.append(contador2)
    
    ax1.plot(elementNumArray[:idx+1], iteracionesBurbujas, 'r',label='Burbuja')
    ax2.plot(elementNumArray[:idx+1], iteracionesMerge, 'b',label='Merge')

    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show(block=False)
    time.sleep(0.5)
    for i in range(24):
      writer.grab_frame()

