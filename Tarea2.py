# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:07:53 2023

@author: olive
"""
from tkinter import *
import tkinter as tk
import re
class aplication():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('600x600')
        self.ventana.resizable(width=False,height=False)
        self.ventana.title('Expresiones regulares')
        label = Label(self.ventana,text='Validacion de expresiones regulares',
                      font = ("Arial Black", 18), fg = "blue", bg = "black")
        label.pack(side=TOP)
        
        label = Label(self.ventana,text='Oliver Cruz Mortera')
        label.pack(side=BOTTOM)
       

        self.text = Frame(self.ventana)
        self.text.pack(side=TOP)
        self.frameDeAbajo=Frame(self.ventana)
        self.frameDeAbajo.pack(side=BOTTOM)


        self.t1 = Entry(self.text,width=40)
        self.t1.grid(row=0,column=0,padx=10,pady=10)
        
        self.t2 = Entry(self.text,width=40)
        self.t2.grid(row=1,column=0)
        
        self.t3 = Entry(self.text,width=40)
        self.t3.grid(row=2,column=0)
        
        self.t4 = Entry(self.text,width=40)
        self.t4.grid(row=3,column=0)

        self.b1 = Button(self.text,text='Validar direccion IPv4',command=lambda:self.validar(1))
        self.b1.grid(row=0,column=1,pady=10)
        
        self.b2 = Button(self.text,text='Validar correo',command=lambda:self.validar2(2))
        self.b2.grid(row=1,column=1,pady=10)
        
        self.b3 = Button(self.text,text='Validar fecha',command=lambda:self.validar3(3))
        self.b3.grid(row=2,column=1,pady=10)
        
        self.b4 = Button(self.text,text='Validar',command=lambda:self.validar(4))
        self.b4.grid(row=3,column=1,pady=10)

        self.l1 = Label(self.text,text=':)')
        self.l1.grid(row=0,column=2)
        
        self.l2 = Label(self.text,text=':)')
        self.l2.grid(row=1,column=2)
        
        self.l3 = Label(self.text,text=':)')
        self.l3.grid(row=2,column=2)
        
        self.l4 = Label(self.text,text=':)')
        self.l4.grid(row=3,column=2)
        
        self.bsalir = Button(self.frameDeAbajo,text='Salir',command=self.ventana.destroy)
        self.bsalir.pack(side=LEFT)
        
        self.blimpiar = Button(self.frameDeAbajo,text='Limpiar',command=self.limpiar)
        self.blimpiar.pack(side=LEFT)

        self.ventana.mainloop()
    def limpiar(self):
        self.t1.delete(first=0,last='end')
        self.l1.config(fg='black',text=':)')
        
        self.t2.delete(first=0,last='end')
        self.l2.config(fg='blue',text=':)')
        
        self.t3.delete(first=0,last='end')
        self.l3.config(fg='black',text=':)')
        
        self.t4.delete(first=0,last='end')
        self.l4.config(fg='black',text=':)')
        
    def validar(self,numero):
        if(numero == 1):
            textAvalidar = self.t1.get()
            esValido = re.match("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$", textAvalidar)
            if (esValido):
                self.l1.config(fg="blue",text='IPv4 valida')
            else:
                self.l1.config(fg="orange",text='IPv4 invalida')
   
    def validar2(self, numero):
        if(numero == 2):
           email = self.t2.get() 
           regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
          self.l2.config(fg="blue",text='correo valido')
        else:
          self.l2.config(fg="red",text='correo invalida')

    def validar3(self, numero):
        if(numero == 3):
            fecha = self.t3.get() 
            regex = r"^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$"
            fechaValida = re.search(regex, fecha)
        if(fechaValida):
           self.l3.config(fg="blue",text='fecha valida')
        else:
           self.l3.config(fg="red",text='fecha invalida')
           
               
    def Mostrar():
        if seleccion.get() == 1:
            mensaje = "Has seleccionado Python"
        if seleccion.get() == 2:
            mensaje = "Has seleccionado HTML"
        if seleccion.get() == 3:
            mensaje = "Has seleccionado C/C++"
            
        lblMensaje.config(text = mensaje)
        
    ventana = tk.Tk()
    seleccion =tk.IntVar()
    
    rbnPython = tk.Radiobutton(ventana, text = "Python", variable = seleccion, value = 1,
                               command = Mostrar).pack (anchor = tk.W)
    
    rbnPython = tk.Radiobutton(ventana, text = "HTML", variable = seleccion, value = 2,
                               command = Mostrar).pack (anchor = tk.W)
    
    rbnPython = tk.Radiobutton(ventana, text = "C/C++", variable = seleccion, value = 3,
                               command = Mostrar).pack (anchor = tk.W)
       
app = aplication()