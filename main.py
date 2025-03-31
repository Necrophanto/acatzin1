import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Probably should create a better abstraction for DB connection
db_connection = sqlite3.connect("my_database_pypika.db")

root = ttk.Window(themename="superhero")

b1 = ttk.Button(root, text="Submit", bootstyle="success")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Submit", bootstyle="info-outline")
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()

"""
ToDo:
Create DB and tables
Launch GUI
Capture pacient
Create folder
Save to file
…
"""


# #  TTK CLASSIC
# import tkinter as tk
# from tkinter import ttk

# ventana = tk.Tk()

# etiqueta = ttk.Label(ventana, text="¡Hola, ttk!")
# etiqueta.pack()

# boton = ttk.Button(ventana, text="Clic aquí")
# boton.pack()

# ventana.mainloop()
