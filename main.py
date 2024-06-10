import tkinter as tk
from tkinter import ttk
from Tk_CerosFunciones import Tk_CerosFunciones
from Tk_EcuacionesDiferencial import Tk_EcuacionesDiferencial
from Tk_InterpolacionAjuste import Tk_InterpolacionAjuste
from Tk_SerieTaylor import Tk_SerieTaylor
from Tk_SistemasEcuacionesLineales import Tk_SistemasEcuacionesLineales
import sympy as sp
# Funciones para abrir nuevas ventanas



# Crear la ventana principal
root = tk.Tk()
root.title("Main Window")
root.geometry("1200x700")

# Crear los botones en la ventana principal
btn1 = ttk.Button(root, text="Ceros de Funciones", command=lambda: Tk_CerosFunciones(root))
btn1.pack(pady=10)

btn2 = ttk.Button(root, text="Ecuaciones Diferenciales", command=lambda:Tk_EcuacionesDiferencial(root))
btn2.pack(pady=10)

btn3 = ttk.Button(root, text="Interpolacion y Ajuste", command=lambda:Tk_InterpolacionAjuste(root))
btn3.pack(pady=10)

btn4 = ttk.Button(root, text="Series de Taylor", command=lambda:Tk_SerieTaylor(root))
btn4.pack(pady=10)

btn5 = ttk.Button(root, text="Sistemas de Ecuaciones Lineales", command=lambda:Tk_SistemasEcuacionesLineales(root))
btn5.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
