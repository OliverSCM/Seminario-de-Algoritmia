# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:52:22 2023

@author: olive
"""
#opencv
import cv2 as cv
import numpy as np

imagenOriginal = cv.imread(r'C:\Users\olive\OneDrive\Documentos\TAREA\tarea5.1.jpg')
imagenGris = cv.imread(r'C:\Users\olive\OneDrive\Documentos\TAREA\tarea5.1.jpg',0) 

cv.imshow('Imagen gris', imagenGris)
cv.imshow('Imagen Original', imagenOriginal)

filas, columnas,canales = np.shape(imagenOriginal)
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
kernel = kernel / np.sum(kernel) # Normalizar kernel

# Crear una copia de la imagen en escala de grises
imagenGrisCopia = imagenGris.copy()

# Aplicar el filtro Gaussiano
for fila in range(1, filas-1):
    for columna in range(1, columnas-1):
        suma = 0
        for filak in range(fila-1, fila+2):
            for columnak in range(columna-1, columna+2):
                suma += kernel[filak-fila+1, columnak-columna+1] * imagenGris[filak, columnak]
        imagenGrisCopia[fila, columna] = suma
        
cv.imshow('Imagen con filtro', imagenGrisCopia)
cv.waitKey()
