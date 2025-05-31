import os
import sys
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
from random import randint, random

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'assets', filename)
    else:
        return os.path.join(os.path.dirname(__file__), 'assets', filename)

# Función para crear el splash screen
def create_splash_screen():
    splash_root = tk.Tk()
    splash_root.title("App Médica")
    splash_root.geometry("900x700")  # "800x600")

    # Cargar la imagen
    logo_path = get_asset_path('caduceus-staff-hermes.jpg')
    image = Image.open(logo_path)
    image = image.resize((800,600))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(splash_root, image=photo)
    image_label.pack(pady=20)

    # Crear la barra de progreso
    progress_bar = ttk.Progressbar(splash_root, orient="horizontal", length=800, mode="determinate")
    progress_bar.pack(pady=10)
    progress_bar['maximum'] = 100

    # Simular una carga y actualizar la barra de progreso
    for i in range(1,120, 10):
        progress_bar['value'] = i
        splash_root.update()
        time.sleep(0.1)

    # Destruir el splash screen y mostrar la ventana principal
    time.sleep(random())
    splash_root.destroy()

create_splash_screen()