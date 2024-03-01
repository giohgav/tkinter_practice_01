import tkinter as tk #importa tkinter
from tkinter import messagebox #importa messagebox 
import sqlite3


ventana = tk.Tk()
ventana.title("soy una ventana")
ventana.geometry("800x600")

etiqueta1 = tk.Label(ventana, text = "Escribe un numero")
etiqueta1.pack()
numero = tk.Entry()
numero.pack()


def abrir ():
    messagebox.showinfo(title="hola",message="Hola")


boton = tk.Button(command=abrir,text = "presiona")
boton.pack()


ventana.mainloop()# inicia root en un loop infinito
