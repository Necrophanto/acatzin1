import tkinter as tk
import calendar
from datetime import date

class DatePickerPersonalizado:
    def __init__(self, master):
        self.master = master
        self.entry_fecha = tk.Entry(master)
        self.entry_fecha.pack()
        self.entry_fecha.bind("<Button-1>", self.mostrar_calendario)

    def mostrar_calendario(self, event):
        self.ventana_calendario = tk.Toplevel(self.master)
        self.calendario = CalendarioWidget(self.ventana_calendario, self.actualizar_fecha_entry)

    def actualizar_fecha_entry(self, fecha_seleccionada):
        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(0, fecha_seleccionada)
        self.ventana_calendario.destroy()

class CalendarioWidget:
    def __init__(self, master, callback_seleccion_fecha):
        self.master = master
        self.callback = callback_seleccion_fecha
        self.hoy = date.today()
        self.mes_actual = self.hoy.month
        self.anio_actual = self.hoy.year
        self.crear_interfaz()
        self.actualizar_calendario()

    def crear_interfaz(self):
        # Etiquetas para mes y año, botones de navegación
        self.label_mes_anio = tk.Label(self.master, text="")
        self.label_mes_anio.pack()

        frame_botones = tk.Frame(self.master)
        tk.Button(frame_botones, text="<", command=self.mes_anterior).pack(side=tk.LEFT)
        tk.Button(frame_botones, text=">", command=self.mes_siguiente).pack(side=tk.RIGHT)
        frame_botones.pack()

        self.frame_dias = tk.Frame(self.master)
        self.frame_dias.pack()

    def actualizar_calendario(self):
        # Limpiar los botones de días anteriores
        for widget in self.frame_dias.winfo_children():
            widget.destroy()

        self.label_mes_anio.config(text=f"{calendar.month_name[self.mes_actual]} {self.anio_actual}")

        primer_dia_semana, num_dias = calendar.monthrange(self.anio_actual, self.mes_actual)

        # Encabezados de los días de la semana
        dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for col, dia in enumerate(dias_semana):
            tk.Label(self.frame_dias, text=dia).grid(row=0, column=col)

        fila = 1
        columna = primer_dia_semana
        for dia in range(1, num_dias + 1):
            boton_dia = tk.Button(self.frame_dias, text=str(dia), width=3,
                                  command=lambda d=dia: self.seleccionar_fecha(d))
            boton_dia.grid(row=fila, column=columna, padx=2, pady=2)
            columna += 1
            if columna > 6:
                columna = 0
                fila += 1

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

    def seleccionar_fecha(self, dia):
        fecha_seleccionada = f"{self.anio_actual}-{self.mes_actual:02}-{dia:02}"
        self.callback(fecha_seleccionada)

root = tk.Tk()
app = DatePickerPersonalizado(root)
root.mainloop()