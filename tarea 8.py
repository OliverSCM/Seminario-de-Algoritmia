# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:46:39 2023

@author: olive
"""
import cv2 as cv

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)

gorro = cv.imread("peloRosa.png",cv.IMREAD_UNCHANGED)

video_capture = cv.VideoCapture(0,cv.CAP_DSHOW)
video = cv.VideoCapture(0, cv.CAP_DSHOW)
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
exportable = cv.VideoWriter('video.avi',
						cv.VideoWriter_fourcc(*'MJPG'),
						10, size)

anterior = 0
if not video_capture.isOpened():
        print('No se pudo acceder a la camara')
else:
    while True:
        ret, frame = video_capture.read()
        frame=cv.flip(frame,1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame,cv.COLOR_BGR2BGRA)
    
        faces = faceCascade.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )
        for (x, y, w, h) in faces:
            y-=int(y/1.125)
            gorro_copia=cv.resize(gorro,(w,h))
            for i in range(gorro_copia.shape[0]):
                for j in range(gorro_copia.shape[1]):
                    if(gorro_copia[i,j][3]!=0):
                        frame[i+y,j+x]=gorro_copia[i,j]

        cv.imshow('Video', frame)
        frame = cv.cvtColor(frame,cv.COLOR_BGRA2BGR)
        exportable.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break    
    video_capture.release()
    exportable.release()
    cv.destroyAllWindows()