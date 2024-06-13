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
root.configure(bg="#0050ee")


frame_inputs = ttk.Frame(root, padding="10", style="My.TFrame")
frame_inputs.pack(pady=10)

# Crear los botones en la ventana principal
btn1 = ttk.Button(frame_inputs, text="Ceros de Funciones", style="Accent.TButton", command=lambda: Tk_CerosFunciones(root))
btn1.grid(row=1, column=1, pady=20)

btn2 = ttk.Button(frame_inputs, text="Ecuaciones Diferenciales", style="Accent.TButton", command=lambda:Tk_EcuacionesDiferencial(root))
btn2.grid(row=2, column=1, pady=20)

btn3 = ttk.Button(frame_inputs, text="Interpolacion y Ajuste", style="Accent.TButton", command=lambda:Tk_InterpolacionAjuste(root))
btn3.grid(row=3, column=1, pady=20)

btn4 = ttk.Button(frame_inputs, text="Series de Taylor", style="Accent.TButton", command=lambda:Tk_SerieTaylor(root))
btn4.grid(row=4, column=1, pady=20)

btn5 = ttk.Button(frame_inputs, text="Sistemas de Ecuaciones Lineales", style="Accent.TButton", command=lambda:Tk_SistemasEcuacionesLineales(root))
btn5.grid(row=5, column=1, pady=20)




# Ejecutar el bucle principal de la aplicación
root.mainloop()

# Ajustes de estilo
style = ttk.Style()
style.configure("My.TFrame", background="#0068ee")
style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
style.map("Accent.TButton", background=[('active', '#00ccff')])