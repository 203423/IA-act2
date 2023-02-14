import graf_aptos
import algoritmo_genetico
from tkinter import *
import tkinter as tk

def send_data():
  global total
  min_info = min.get()
  max_info = max.get()
  pobMax_info = pobMax.get()
  generaciones_info = generaciones.get()

 
  total = 3000
  algoritmo_genetico.main(pobMax_info,generaciones_info,min_info,max_info)
 
#  Delete data from previous event

# Create new instance - Class Tk()  
ventana = Tk()
ventana.geometry("1200x600")
ventana.title("Algoritmo génetico canonico")
ventana.resizable(False,False)
frame_izquierda = tk.Frame(ventana, width=700, height=750, pady=10, padx=5)
frame_derecha = tk.Frame(ventana, width=700, height=750, pady=10, padx=5)
frame_derecha.pack(side="right")
frame_izquierda.pack(side="left")
ventana.config(background = "#FFFFFF")
max_label = Label(frame_izquierda, text = "xmax")
max_label.place(x = 22, y = 190)
min_label = Label(frame_izquierda, text = "xmin")
min_label.place(x = 22, y = 250)
pobMax_label = Label(frame_izquierda, text = "POB MAX")
pobMax_label.place(x = 22, y = 310)
generaciones_label = Label(frame_izquierda, text = "Numero de generaciones")
generaciones_label.place(x = 22, y = 370)
max = StringVar()
min = StringVar()
pobMax = StringVar()
generaciones = StringVar()
max_entry = Entry(frame_izquierda, textvariable = max, width = 40,)
min_entry = Entry(frame_izquierda, textvariable = min, width = 40,)
pobMax_entry = Entry(frame_izquierda, textvariable = pobMax, width = 40)
generaciones_entry = Entry(frame_izquierda, textvariable = generaciones, width = 40)
max_entry.place(x = 22, y = 220)
min_entry.place(x = 22, y = 280)
pobMax_entry.place(x = 22, y = 340)
generaciones_entry.place(x = 22, y = 400)
submit_btn = Button(frame_izquierda, text="Continuar", command = send_data)
submit_btn.place(x = 22, y = 480)
ventana.mainloop()

