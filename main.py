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

def crear_receta():
    root = tb.Window(themename="cosmo")
    root.title("Receta Médica")
    root.geometry("900x450")

    lbl_doctor = ttk.Label(root, text="Dr. YVAN ACATZIN RAMIREZ DEL PILAR", font=("Arial", 14, "bold"), style="primary.TLabel")
    lbl_doctor.pack(pady=10)

    frame_info = ttk.Frame(root)
    frame_info.pack(fill="x", padx=20)

    tb.Label(frame_info, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5)
    tb.Entry(frame_info, width=30).grid(row=0, column=1, padx=5)

    tb.Label(frame_info, text="Fecha:").grid(row=0, column=2, sticky="w", padx=5)
    entry_fecha = tb.Entry(frame_info, width=15)
    entry_fecha.grid(row=0, column=3, padx=5)
    boton_fecha = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_fecha), bootstyle="secondary-outline")
    boton_fecha.grid(row=0, column=4, padx=2)

    tb.Label(frame_info, text="Edad:").grid(row=0, column=5, sticky="w", padx=5)
    tb.Entry(frame_info, width=10).grid(row=0, column=6, padx=5)

    tb.Label(frame_info, text="Diagnóstico:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tb.Entry(frame_info, width=50).grid(row=1, column=1, columnspan=6, padx=5, pady=5)

    tb.Label(frame_info, text="Fecha de nacimiento:").grid(row=2, column=0, sticky="w", padx=5)
    entry_nacimiento = tb.Entry(frame_info, width=20)
    entry_nacimiento.grid(row=2, column=1, padx=5)
    fecha_hace_18_anios = date.today() - timedelta(days=18*365.25) # Aproximación de 18 años
    boton_nacimiento = tb.Button(frame_info, text="...", width=3, command=lambda: mostrar_calendario(entry_nacimiento, initial_date=fecha_hace_18_anios), bootstyle="secondary-outline")
    boton_nacimiento.grid(row=2, column=2, padx=2)

    frame_signos = ttk.Frame(root)
    frame_signos.pack(fill="x", padx=20, pady=10)

    tb.Label(frame_signos, text="SpO2:").grid(row=0, column=0, sticky="w", padx=5)
    tb.Entry(frame_signos, width=10).grid(row=0, column=1, padx=5)

    tb.Label(frame_signos, text="T/A:").grid(row=0, column=2, sticky="w", padx=5)
    tb.Entry(frame_signos, width=10).grid(row=0, column=3, padx=5)

    tb.Label(frame_signos, text="Fc:").grid(row=0, column=4, sticky="w", padx=5)
    tb.Entry(frame_signos, width=10).grid(row=0, column=5, padx=5)

    tb.Label(frame_signos, text="Fr:").grid(row=0, column=6, sticky="w", padx=5)
    tb.Entry(frame_signos, width=10).grid(row=0, column=7, padx=5)

    tb.Label(frame_signos, text="Temp:").grid(row=0, column=8, sticky="w", padx=5)
    tb.Entry(frame_signos, width=10).grid(row=0, column=9, padx=5)

    text_area = tk.Text(root)
    text_area.pack(fill="both", expand=True, pady=10, padx=10)

    root.mainloop()

crear_receta()

