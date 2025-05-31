import ttkbootstrap as tb
import tkinter as tk
from tkinter import messagebox

def crear_login():
    root = tb.Window(themename="cosmo")
    root.title("Bienvenido")
    root.geometry("900x700")

    # --- Main Frame to Center Content ---
    main_frame = tb.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # --- Widgets ---
    title_label = tb.Label(main_frame, text="Inicio de Sesión", font=("Arial", 26, "bold"), style="Primary.TLabel")
    usuario_label = tb.Label(main_frame, text="Usuario:", font=("Arial", 14), style="Primary.TLabel")
    usuario_entry = tb.Entry(main_frame, font=("Arial", 14))
    contrasena_label = tb.Label(main_frame, text="Contraseña:", font=("Arial", 14), style="Primary.TLabel")
    contrasena_entry = tb.Entry(main_frame, show="*", font=("Arial", 14))

    ingresar_button = tb.Button(main_frame, text="Ingresar", bootstyle="success", command=login, width=15)
    registrar_button = tb.Button(main_frame, text="Registrar Médico", bootstyle="warning", command=registrar_medico, width=15)

    # --- Layout within the Main Frame ---
    title_label.pack(pady=(0, 30))  # Add some padding below the title
    usuario_label.pack(pady=(10, 5), fill="x", padx=20)
    usuario_entry.pack(pady=5, fill="x", padx=20)
    contrasena_label.pack(pady=(10, 5), fill="x", padx=20)
    contrasena_entry.pack(pady=5, fill="x", padx=20)
    ingresar_button.pack(pady=(20, 10), fill="x", padx=20)
    registrar_button.pack(pady=(5, 10), fill="x", padx=20)

    root.mainloop()

def login():
    # Replace this with your actual login logic
    messagebox.showinfo("Info", "Función de Ingresar")

def registrar_medico():
    # Replace this with your actual registration logic
    messagebox.showinfo("Info", "Función de Registrar Médico")

crear_login()
