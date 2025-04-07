import tkinter as tk
from tkcalendar import Calendar

def mostrar_calendario():
    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day', date_pattern='dd-mm-yyyy')
    cal.pack(padx=10, pady=10)

    def seleccionar_fecha():
        fecha_seleccionada = cal.get_date()
        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, fecha_seleccionada)
        top.destroy()

    boton_seleccionar = tk.Button(top, text="Seleccionar", command=seleccionar_fecha)
    boton_seleccionar.pack(pady=5)

root = tk.Tk()
root.title("Ejemplo Datepicker")

entry_fecha = tk.Entry(root)
entry_fecha.pack(padx=10, pady=10)

boton_mostrar = tk.Button(root, text="Mostrar Calendario", command=mostrar_calendario)
boton_mostrar.pack(pady=5)

root.mainloop()