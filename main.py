import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk
import calendar
from datetime import date, timedelta

class CalendarioWidget(tk.Toplevel):
    def __init__(self, master=None, callback_seleccion_fecha=None, initial_date=None):
        super().__init__(master)
        self.callback = callback_seleccion_fecha
        self.hoy = date.today()
        if initial_date:
            self.mes_actual = initial_date.month
            self.anio_actual = initial_date.year
        else:
            self.mes_actual = self.hoy.month
            self.anio_actual = self.hoy.year
        self.title("Seleccionar Fecha")
        self.geometry("+%d+%d" % (master.winfo_rootx()+50, master.winfo_rooty()+50))
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cerrar_calendario)
        self.botones_dia = {}

        self.crear_interfaz()
        self.actualizar_calendario()

    def crear_interfaz(self):
        frame_header = ttk.Frame(self)
        frame_header.pack(pady=5)

        self.btn_anio_anterior = ttk.Button(frame_header, text="<<", command=self.anio_anterior, width=3)
        self.btn_anio_anterior.pack(side=tk.LEFT, padx=2)

        self.btn_mes_anterior = ttk.Button(frame_header, text="<", command=self.mes_anterior, width=3)
        self.btn_mes_anterior.pack(side=tk.LEFT, padx=2)

        self.label_mes_anio = ttk.Label(frame_header, text="", font=("Arial", 12, "bold"))
        self.label_mes_anio.pack(side=tk.LEFT, padx=5)

        self.btn_mes_siguiente = ttk.Button(frame_header, text=">", command=self.mes_siguiente, width=3)
        self.btn_mes_siguiente.pack(side=tk.LEFT, padx=2)

        self.btn_anio_siguiente = ttk.Button(frame_header, text=">>", command=self.anio_siguiente, width=3)
        self.btn_anio_siguiente.pack(side=tk.LEFT, padx=2)

        self.frame_dias = ttk.Frame(self)
        self.frame_dias.pack(padx=5, pady=5)

        dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for col, dia in enumerate(dias_semana):
            ttk.Label(self.frame_dias, text=dia, width=3).grid(row=0, column=col, padx=2, pady=2)

    def actualizar_calendario(self):
        for widget in self.frame_dias.winfo_children()[7:]:
            widget.destroy()
        self.botones_dia.clear()

        self.label_mes_anio.config(text=f"{calendar.month_name[self.mes_actual]} {self.anio_actual}")

        primer_dia_semana, num_dias = calendar.monthrange(self.anio_actual, self.mes_actual)

        fila = 1
        columna = primer_dia_semana
        for dia in range(1, num_dias + 1):
            btn_dia = ttk.Button(self.frame_dias, text=str(dia), width=3,
                                 command=lambda d=dia: self.seleccionar_fecha(d))
            btn_dia.grid(row=fila, column=columna, padx=2, pady=2)
            self.botones_dia[(self.anio_actual, self.mes_actual, dia)] = btn_dia
            columna += 1
            if columna > 6:
                columna = 0
                fila += 1

        # Resaltar la fecha actual (o la fecha inicial si se proporciona)
        fecha_a_resaltar = date(self.anio_actual, self.mes_actual, self.hoy.day)
        if hasattr(self, 'initial_date_highlight') and self.initial_date_highlight:
            fecha_a_resaltar = self.initial_date_highlight

        if fecha_a_resaltar.year == self.anio_actual and fecha_a_resaltar.month == self.mes_actual:
            if (self.anio_actual, self.mes_actual, fecha_a_resaltar.day) in self.botones_dia:
                self.botones_dia[(self.anio_actual, self.mes_actual, fecha_a_resaltar.day)].config(bootstyle="success")

    def mes_anterior(self):
        self.mes_actual -= 1
        if self.mes_actual < 1:
            self.mes_actual = 12
            self.anio_actual -= 1
        self.actualizar_calendario()

    def mes_siguiente(self):
        self.mes_actual += 1
        if self.mes_actual > 12:
            self.mes_actual = 1
            self.anio_actual += 1
        self.actualizar_calendario()

    def anio_anterior(self):
        self.anio_actual -= 1
        self.actualizar_calendario()

    def anio_siguiente(self):
        self.anio_actual += 1
        self.actualizar_calendario()

    def seleccionar_fecha(self, dia):
        fecha_seleccionada = f"{dia:02}-{self.mes_actual:02}-{self.anio_actual}"
        if self.callback:
            self.callback(fecha_seleccionada)
        self.destroy()

    def cerrar_calendario(self):
        self.grab_release()
        self.destroy()

def mostrar_calendario(entry, initial_date=None):
    def set_date(fecha):
        entry.delete(0, tk.END)
        entry.insert(0, fecha)

    CalendarioWidget(entry, callback_seleccion_fecha=set_date, initial_date=initial_date)

def mostrar_calendario(entry, initial_date=None):
    def set_date(fecha):
        entry.delete(0, tk.END)
        entry.insert(0, fecha)

    CalendarioWidget(entry, callback_seleccion_fecha=set_date, initial_date=initial_date)

def prueba_campos():
    nombre = nombre_paciente.get()
    edad = edad_paciente.get()
    fecha_nac = entry_nacimiento.get()
    peso = peso_paciente.get()
    altura = talla_paciente.get()
    diagnosis = diagnostico.get()
    spO2 = saturacion.get()
    t_a = presion.get()
    fc = frec_cardiaca.get()
    fr = frec_respiratoria.get()
    temp = temperatura.get()
    tx = tratamiento_txt.get('1.0', tk.END)
    print(f"Paciente: {nombre} nacido en {fecha_nac} de {edad} años \npesando {peso}kg y midiendo {altura}cm \
        presenta {diagnosis} con los siguientes signos vitales: \
            spO2:{spO2} || T/A:{t_a}  || FC: {fc}  || FR: {fr}  || Temp:{temp}° \n Para lo cual se prescribe: {tx}")

def crear_receta():
    root = tb.Window(themename="cosmo")
    root.title("Receta Médica")
    root.geometry("900x700")

    lbl_doctor = ttk.Label(root, text="Dr. YVAN ACATZIN RAMIREZ DEL PILAR", font=("Arial", 14, "bold"), style="primary.TLabel")
    lbl_doctor.pack(pady=10)

    frame_info = ttk.Frame(root)
    frame_info.pack(fill="x", padx=20)

    tb.Label(frame_info, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5)
    global nombre_paciente
    nombre_paciente = tb.Entry(frame_info, width=20)  # Create the Entry widget
    nombre_paciente.grid(row=0, column=1, sticky="w", padx=5)  # Place it using grid

    tb.Label(frame_info, text="Fecha:").grid(row=0, column=2, sticky="w", padx=5)
    global entry_fecha
    entry_fecha = tb.Entry(frame_info, width=15)
    entry_fecha.grid(row=0, column=3, padx=5)
    boton_fecha = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_fecha), bootstyle="secondary-outline")
    boton_fecha.grid(row=0, column=4, padx=2)

    tb.Label(frame_info, text="Edad:").grid(row=0, column=6, sticky="w", padx=5)
    global edad_paciente
    edad_paciente = tb.Entry(frame_info, width=10)
    edad_paciente.grid(row=0, column=7, padx=1)

    tb.Label(frame_info, text="Fecha de nacimiento:").grid(row=1, column=0, sticky="w", padx=5)
    global entry_nacimiento
    entry_nacimiento = tb.Entry(frame_info, width=20)
    entry_nacimiento.grid(row=1, column=1, padx=5)
    fecha_hace_18_anios = date.today() - timedelta(days=18*365.25) # Aproximación de 18 años
    boton_nacimiento = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_nacimiento, initial_date=fecha_hace_18_anios), bootstyle="secondary-outline")
    boton_nacimiento.grid(row=1, column=2, padx=2)

    tb.Label(frame_info, text="Peso:").grid(row=1, column=6, sticky="w", padx=5)
    global peso_paciente
    peso_paciente = tb.Entry(frame_info, width=10)
    peso_paciente.grid(row=1, column=7, sticky="w", padx=5)
    tb.Label(frame_info, text="Kg").grid(row=1, column=8, sticky="w")

    tb.Label(frame_info, text="Alergias:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    global alergias_paciente
    alergias_paciente = tb.Entry(frame_info, width=50)
    alergias_paciente.grid(row=2, column=1, columnspan=4, padx=5, pady=5)

    tb.Label(frame_info, text="Talla:").grid(row=2, column=6, sticky="w", padx=5, pady=5)
    global talla_paciente
    talla_paciente = tb.Entry(frame_info, width=10)
    talla_paciente.grid(row=2, column=7, padx=5, pady=5)
    tb.Label(frame_info, text="cm").grid(row=2, column=8, sticky="w")

    tb.Label(frame_info, text="Diagnóstico:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    global diagnostico
    diagnostico = tb.Entry(frame_info, width=50)
    diagnostico.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

    frame_signos = ttk.Frame(root)
    frame_signos.pack(fill="x", padx=20, pady=10)

    tb.Label(frame_signos, text="SpO2:").grid(row=0, column=0, sticky="w", padx=5)
    global saturacion
    saturacion = tb.Entry(frame_signos, width=10)
    saturacion.grid(row=0, column=1, padx=5)

    tb.Label(frame_signos, text="T/A:").grid(row=0, column=2, sticky="w", padx=5)
    global presion
    presion = tb.Entry(frame_signos, width=10)
    presion.grid(row=0, column=3, padx=5)

    tb.Label(frame_signos, text="Fc:").grid(row=0, column=4, sticky="w", padx=5)
    global frec_cardiaca
    frec_cardiaca = tb.Entry(frame_signos, width=10)
    frec_cardiaca.grid(row=0, column=5, padx=5)

    tb.Label(frame_signos, text="Fr:").grid(row=0, column=6, sticky="w", padx=5)
    global frec_respiratoria
    frec_respiratoria = tb.Entry(frame_signos, width=10)
    frec_respiratoria.grid(row=0, column=7, padx=5)

    tb.Label(frame_signos, text="Temp:").grid(row=0, column=8, sticky="w", padx=5)
    global temperatura
    temperatura = tb.Entry(frame_signos, width=10)
    temperatura.grid(row=0, column=9, padx=5)

    tratamiento_lbl = tb.Label(root, text="Tratamiento:")
    tratamiento_lbl.pack(fill="x", expand=True, padx=5)
    global tratamiento_txt
    tratamiento_txt = tk.Text(root, height=16)
    tratamiento_txt.pack(fill="both", expand=True, pady=2, padx=5)

    frame_guardado = ttk.Frame(root)
    frame_guardado.pack(fill="x", padx=10, pady=20)

    tb.Button(frame_guardado, text="Regresar", style="danger.Outline.TButton").grid(row=0, column=1, sticky="w", padx=5)
    ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=2, sticky="e", padx=100)
    ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=3, sticky="s", padx=150)
    ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=4, sticky="w", padx=100)
    tb.Button(frame_guardado, text="Imprimir", style='success.Outline.TButton', command=prueba_campos).grid(row=0, column=40, sticky="e", padx=5)

    root.mainloop()

crear_receta()
















































# import ttkbootstrap as tb
# import tkinter as tk
# from tkinter import ttk
# import calendar
# from datetime import date, timedelta

# class CalendarioWidget(tk.Toplevel):
#     def __init__(self, master=None, callback_seleccion_fecha=None, initial_date=None):
#         super().__init__(master)
#         self.callback = callback_seleccion_fecha
#         self.hoy = date.today()
#         if initial_date:
#             self.mes_actual = initial_date.month
#             self.anio_actual = initial_date.year
#         else:
#             self.mes_actual = self.hoy.month
#             self.anio_actual = self.hoy.year
#         self.title("Seleccionar Fecha")
#         self.geometry("+%d+%d" % (master.winfo_rootx()+50, master.winfo_rooty()+50))
#         self.resizable(False, False)
#         self.focus_set()
#         self.grab_set()
#         self.protocol("WM_DELETE_WINDOW", self.cerrar_calendario)
#         self.botones_dia = {}

#         self.crear_interfaz()
#         self.actualizar_calendario()

#     def crear_interfaz(self):
#         frame_header = ttk.Frame(self)
#         frame_header.pack(pady=5)

#         self.btn_anio_anterior = ttk.Button(frame_header, text="<<", command=self.anio_anterior, width=3)
#         self.btn_anio_anterior.pack(side=tk.LEFT, padx=2)

#         self.btn_mes_anterior = ttk.Button(frame_header, text="<", command=self.mes_anterior, width=3)
#         self.btn_mes_anterior.pack(side=tk.LEFT, padx=2)

#         self.label_mes_anio = ttk.Label(frame_header, text="", font=("Arial", 12, "bold"))
#         self.label_mes_anio.pack(side=tk.LEFT, padx=5)

#         self.btn_mes_siguiente = ttk.Button(frame_header, text=">", command=self.mes_siguiente, width=3)
#         self.btn_mes_siguiente.pack(side=tk.LEFT, padx=2)

#         self.btn_anio_siguiente = ttk.Button(frame_header, text=">>", command=self.anio_siguiente, width=3)
#         self.btn_anio_siguiente.pack(side=tk.LEFT, padx=2)

#         self.frame_dias = ttk.Frame(self)
#         self.frame_dias.pack(padx=5, pady=5)

#         dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
#         for col, dia in enumerate(dias_semana):
#             ttk.Label(self.frame_dias, text=dia, width=3).grid(row=0, column=col, padx=2, pady=2)

#     def actualizar_calendario(self):
#         for widget in self.frame_dias.winfo_children()[7:]:
#             widget.destroy()
#         self.botones_dia.clear()

#         self.label_mes_anio.config(text=f"{calendar.month_name[self.mes_actual]} {self.anio_actual}")

#         primer_dia_semana, num_dias = calendar.monthrange(self.anio_actual, self.mes_actual)

#         fila = 1
#         columna = primer_dia_semana
#         for dia in range(1, num_dias + 1):
#             btn_dia = ttk.Button(self.frame_dias, text=str(dia), width=3,
#                                  command=lambda d=dia: self.seleccionar_fecha(d))
#             btn_dia.grid(row=fila, column=columna, padx=2, pady=2)
#             self.botones_dia[(self.anio_actual, self.mes_actual, dia)] = btn_dia
#             columna += 1
#             if columna > 6:
#                 columna = 0
#                 fila += 1

#         # Resaltar la fecha actual (o la fecha inicial si se proporciona)
#         fecha_a_resaltar = date(self.anio_actual, self.mes_actual, self.hoy.day)
#         if hasattr(self, 'initial_date_highlight') and self.initial_date_highlight:
#             fecha_a_resaltar = self.initial_date_highlight

#         if fecha_a_resaltar.year == self.anio_actual and fecha_a_resaltar.month == self.mes_actual:
#             if (self.anio_actual, self.mes_actual, fecha_a_resaltar.day) in self.botones_dia:
#                 self.botones_dia[(self.anio_actual, self.mes_actual, fecha_a_resaltar.day)].config(bootstyle="success")

#     def mes_anterior(self):
#         self.mes_actual -= 1
#         if self.mes_actual < 1:
#             self.mes_actual = 12
#             self.anio_actual -= 1
#         self.actualizar_calendario()

#     def mes_siguiente(self):
#         self.mes_actual += 1
#         if self.mes_actual > 12:
#             self.mes_actual = 1
#             self.anio_actual += 1
#         self.actualizar_calendario()

#     def anio_anterior(self):
#         self.anio_actual -= 1
#         self.actualizar_calendario()

#     def anio_siguiente(self):
#         self.anio_actual += 1
#         self.actualizar_calendario()

#     def seleccionar_fecha(self, dia):
#         fecha_seleccionada = f"{dia:02}-{self.mes_actual:02}-{self.anio_actual}"
#         if self.callback:
#             self.callback(fecha_seleccionada)
#         self.destroy()

#     def cerrar_calendario(self):
#         self.grab_release()
#         self.destroy()

# def mostrar_calendario(entry, initial_date=None):
#     def set_date(fecha):
#         entry.delete(0, tk.END)
#         entry.insert(0, fecha)

#     CalendarioWidget(entry, callback_seleccion_fecha=set_date, initial_date=initial_date)

# def prueba_campos():
#     nombre = nombre_paciente.get()
#     edad = edad_paciente.get()
#     fecha_nac = entry_nacimiento.get()
#     peso = peso_paciente.get()
#     altura = talla_paciente.get()
#     diagnosis = diagnostico.get()
#     spO2 = saturacion.get()
#     t_a = presion.get()
#     fc = frec_cardiaca.get()
#     fr = frec_respiratoria.get()
#     temp = temperatura.get()
#     tx = tratamiento_txt.get()
#     print(f"Paciente: {nombre} nacido en {fecha_nac} de {edad} años \npesando {peso}kg y midiendo {altura}cm \
#             presenta {diagnosis} con los siguientes signos vitales: \
#             spO2:{spO2} || T/A:{t_a}  || FC: {fc}  || FR: {fr}  || Temp:{temp}° \
#             Para lo cual se prescribe: {tx}")

# def crear_receta():
#     root = tb.Window(themename="cosmo")
#     root.title("Receta Médica")
#     root.geometry("900x700")

#     lbl_doctor = ttk.Label(root, text="Dr. YVAN ACATZIN RAMIREZ DEL PILAR", font=("Arial", 14, "bold"), style="primary.TLabel")
#     lbl_doctor.pack(pady=10)

#     frame_info = ttk.Frame(root)
#     frame_info.pack(fill="x", padx=20)

#     tb.Label(frame_info, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5)
#     global nombre_paciente
#     nombre_paciente = tb.Entry(frame_info, width=20).grid(row=0, column=1, sticky="w", padx=5)

#     tb.Label(frame_info, text="Fecha:").grid(row=0, column=2, sticky="w", padx=5)
#     global entry_fecha
#     entry_fecha = tb.Entry(frame_info, width=15)
#     entry_fecha.grid(row=0, column=3, padx=5)
#     boton_fecha = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_fecha), bootstyle="secondary-outline")
#     boton_fecha.grid(row=0, column=4, padx=2)

#     tb.Label(frame_info, text="Edad:").grid(row=0, column=6, sticky="w", padx=5)
#     global edad_paciente
#     edad_paciente = tb.Entry(frame_info, width=10).grid(row=0, column=7, padx=1)

#     tb.Label(frame_info, text="Fecha de nacimiento:").grid(row=1, column=0, sticky="w", padx=5)
#     global entry_nacimiento
#     entry_nacimiento = tb.Entry(frame_info, width=20)
#     entry_nacimiento.grid(row=1, column=1, padx=5)
#     fecha_hace_18_anios = date.today() - timedelta(days=18*365.25) # Aproximación de 18 años
#     boton_nacimiento = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_nacimiento, initial_date=fecha_hace_18_anios), bootstyle="secondary-outline")
#     boton_nacimiento.grid(row=1, column=2, padx=2)
    
#     tb.Label(frame_info, text="Peso:").grid(row=1, column=6, sticky="w", padx=5)
#     global peso_paciente
#     peso_paciente = tb.Entry(frame_info, width=10).grid(row=1, column=7, sticky="w", padx=5)
#     tb.Label(frame_info, text="Kg").grid(row=1, column=8, sticky="w")
    
#     tb.Label(frame_info, text="Alergias:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
#     global alergias_paciente
#     alergias_paciente = tb.Entry(frame_info, width=50).grid(row=2, column=1, columnspan=4, padx=5, pady=5)
    
#     tb.Label(frame_info, text="Talla:").grid(row=2, column=6, sticky="w", padx=5, pady=5)
#     global talla_paciente
#     talla_paciente = tb.Entry(frame_info, width=10).grid(row=2, column=7, padx=5, pady=5)
#     tb.Label(frame_info, text="cm").grid(row=2, column=8, sticky="w")

#     tb.Label(frame_info, text="Diagnóstico:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
#     global diagnostico
#     diagnostico = tb.Entry(frame_info, width=50).grid(row=3, column=1, columnspan=4, padx=5, pady=5)

#     frame_signos = ttk.Frame(root)
#     frame_signos.pack(fill="x", padx=20, pady=10)

#     tb.Label(frame_signos, text="SpO2:").grid(row=0, column=0, sticky="w", padx=5)
#     global saturacion
#     saturacion = tb.Entry(frame_signos, width=10).grid(row=0, column=1, padx=5)

#     tb.Label(frame_signos, text="T/A:").grid(row=0, column=2, sticky="w", padx=5)
#     global presion
#     presion = tb.Entry(frame_signos, width=10).grid(row=0, column=3, padx=5)

#     tb.Label(frame_signos, text="Fc:").grid(row=0, column=4, sticky="w", padx=5)
#     global frec_cardiaca
#     frec_cardiaca = tb.Entry(frame_signos, width=10).grid(row=0, column=5, padx=5)

#     tb.Label(frame_signos, text="Fr:").grid(row=0, column=6, sticky="w", padx=5)
#     global frec_respiratoria
#     frec_respiratoria = tb.Entry(frame_signos, width=10).grid(row=0, column=7, padx=5)

#     tb.Label(frame_signos, text="Temp:").grid(row=0, column=8, sticky="w", padx=5)
#     global temperatura
#     temperatura = tb.Entry(frame_signos, width=10).grid(row=0, column=9, padx=5)
    
#     tratamiento_lbl = tb.Label(root, text="Tratamiento:")
#     tratamiento_lbl.pack(fill="x", expand=True, padx=5)
#     global tratamiento_txt
#     tratamiento_txt = tk.Text(root, height=16)
#     tratamiento_txt.pack(fill="both", expand=True, pady=2, padx=5)
    
#     frame_guardado = ttk.Frame(root)
#     frame_guardado.pack(fill="x", padx=10, pady=20)
    
#     tb.Button(frame_guardado, text="Regresar", style="danger.Outline.TButton").grid(row=0, column=1, sticky="w", padx=5)
#     ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=2, sticky="e", padx=100)
#     ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=3, sticky="s", padx=150)
#     ttk.Separator(frame_guardado, orient='vertical').grid(row=0, column=4, sticky="w", padx=100)
#     ttk.Button(frame_guardado, text="Imprimir", style='success.Outline.TButton', command=prueba_campos).grid(row=0, column=40, sticky="e", padx=5)
    

#     root.mainloop()

# crear_receta()

