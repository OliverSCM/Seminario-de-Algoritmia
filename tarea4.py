# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:16:15 2023

@author: olive
"""

import pygame as pg
import numpy as np

class MapaNode:
    def __init__(self,position,parent=None):
        self.parent=parent
        self.position=position
    
    def __eq__(self,other):
        return self.position[0]==other.position[0] and self.position[1]==other.position[1]
    
class deepSearch(object):
    def run(self,mapa,start,end):
        mapa=mapa.astype(np.float)
        startNode=MapaNode(start[::-1])
        endNode=MapaNode(end[::-1])
        path=[]
        pila=[]
        pila.append(startNode)
        mapaRows,mapaCols=np.shape(mapa)
        visited=np.zeros(mapa.shape)
        while(len(pila)!=0 ):
            currentNode=pila.pop(0)
            if currentNode==endNode:
                break
            #-------------
            #|1.4| 1 |1.4|
            #| 1 | c | 1 |
            #|1.4| 1 |1.4|
            #-------------
            
            movements=[[-1,-1,1.4],
                       [0,-1,1],
                       [1,-1,1.4],
                       [-1,0,1],
                       [1,0,1],
                       [-1,1,1.4],
                       [0,1,1],
                       [1,1,1.4]
                       ]
            
            movements=[
                        [0,-1,1],
                        [-1,0,1],
                        [1,0,1],
                        [0,1,1]
                        ]
            
            
            for movement in movements:
#                creamos la posicion del adjacente
                newPosition=[currentNode.position[0]+movement[0],currentNode.position[1]+movement[1]]
#                REvisamos que este dentro del mapa, que no haya sido visitado y que no sea obstaculo
                if newPosition[0]<0 or newPosition[1]<0 or newPosition[1]>=mapaCols or newPosition[0]>=mapaRows:
                    continue
                elif visited[newPosition[0]][newPosition[1]]==1:
                    continue
                elif mapa[newPosition[0]][newPosition[1]]==0:
                    continue
                else:
#                    Agregamos el nodo a la pila y de padre queda el que acabamos de sacar
                    adjacentNode=MapaNode(newPosition,currentNode)
                    pila.append(adjacentNode)
                    visited[newPosition[0]][newPosition[1]]=1
#        De reversa mami para optener el camino
        while currentNode is not None:
            path.append(currentNode.position)
            currentNode=currentNode.parent
        return path,visited



pg.init()
#cargamos el archivo de numpy que contiene el mapa
mapaAlg=np.load('mapaProfundidad (1).npy')
#checamos el tamaño del mapa
width,height = mapaAlg.shape
#definimos los colores
BLACK = pg.Color('black')
WHITE = pg.Color('white')
GREEN = pg.Color('green')
RED   = pg.Color('red')
BLUE   = pg.Color('blue')
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the mapa
color_dark = (100,100,100)
smallfont = pg.font.SysFont('comicsans', 30)
text = smallfont.render('PICALE AQUI' , True , RED)
#tamaño en pixeles de la celda o el cuadro
tile_size = 10
#punto incial en formato columa,fila (x,y)
start= [50,15]
#punto final en formato columa,fila (x,y)
goal= [27,12]
#tamaño para el espacio para el boton
topPadding=50
#creo el objeto para la busqueda en profundidad
search=deepSearch()

#el tamaño del mapa debe tener la ventana por eso es el tamaño del mapa por el tamño de los cuadros
screen = pg.display.set_mode((width*tile_size, height*tile_size+topPadding))
clock = pg.time.Clock()



#Espacio para el mapa
background = pg.Surface((width*tile_size, height*tile_size))
#Espacio para el boton
buttons = pg.Surface((width*tile_size, 50))

#Dibujamos los cuadros del mapa
for y in range(0, height):
    for x in range(0, width):
        rect = (x*tile_size, y*tile_size, tile_size, tile_size)
        if(mapaAlg[y,x]==0):
            color=BLACK
        else:
            color=WHITE
        if x==start[0] and y==start[1]:
            color=GREEN
        if x==goal[0] and y==goal[1]:
            color=RED
        pg.draw.rect(background,color , rect)

#aqui es la ejecucion del "Juego"
game_exit = False
while not game_exit:
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if 10 <= mouse[0] <= 150 and 10 <= mouse[1] <= 40:
                camino,mapavisited=search.run(mapaAlg,start,goal)
                for point in camino:
                    rect = (point[1]*tile_size, point[0]*tile_size, tile_size, tile_size)
                    pg.draw.rect(background,BLUE , rect)


    
    #cuando el mouse esta sibre las coordenadas del boton le cambiamos el colo a uno gris bajito
    if 0 <= mouse[0] <= 140 and 10<= mouse[1] <= 40:
        pg.draw.rect(buttons,color_light,[10,10,140,30])
          
    else:
        pg.draw.rect(buttons,color_dark,[10,10,140,30])
        
    screen.fill((0, 0, 0))
    
    screen.blit(buttons, (0, 0))
    screen.blit(background, (0, 50))
    screen.blit(text , (10,10))
    pg.display.flip()
    clock.tick(30)
pg.display.quit()
