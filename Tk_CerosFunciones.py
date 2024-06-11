import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.CerosFunciones import *
import sympy as sp
import numpy as np




def convertir_funcion(input_usuario):
    return lambda x: eval(input_usuario)

def answer(name, f, data, tol):
    if len(data) > 0 and len(data) < 3:

        if name == "Newton" and len(data) == 1:

             return newton(f, data[0], tol)

        if len(data) == 1:

            return "ingrese los datos correctamente"

        elif name == "Bisección":

            return biseccion(f, data[0], data[1], tol)

        elif name == "Falsa posición":

            return posicion_falsa(f, data[0], data[1], tol)
        else:

            return secante(f, data[0], data[1], tol)

    else:
        return "ingrese los datos correctamente"




def Tk_CerosFunciones(root):
    new_window = tk.Toplevel(root)
    new_window.title("Ceros de Funciones")
    new_window.geometry("1200x700")  # Tamaño de la ventana

    new_window.configure(bg="#0050ee")  # Fondo de la ventana
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=10)
    # Crear el título
    title = ttk.Label(new_window, text="Ceros de funciones", font=("Helvetica", 24), background="#0050ee")
    title.pack(pady=10)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)

    # Función de entrada
    ttk.Label(frame_inputs, text="Función:", background="#0068ee", font=("Helvetica", 14)).grid(row=0, column=0,
                                                                                                padx=10, pady=5)
    function_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    function_entry.grid(row=0, column=1, padx=10, pady=5)

    # Punto a
    ttk.Label(frame_inputs, text="dato inicial o intervalo(separado por comas) :", background="#0068ee", font=("Helvetica", 14)).grid(row=1, column=0,
                                                                                                padx=10, pady=5)
    a_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    a_entry.grid(row=1, column=1, padx=10, pady=5)

    # Punto b
    ttk.Label(frame_inputs, text="Exactitud:", background="#0068ee", font=("Helvetica", 14)).grid(row=2, column=0,
                                                                                                padx=10, pady=5)
    tolerance = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    tolerance.grid(row=2, column=1, padx=10, pady=5)

    # Selección del método
    ttk.Label(frame_inputs, text="Método:", background="#0068ee", font=("Helvetica", 14)).grid(row=3, column=0, padx=10,
                                                                                               pady=5)
    method_combobox = ttk.Combobox(frame_inputs, values=["Bisección", "Newton", "Falsa posición", "Secante"],
                                   font=("Helvetica", 14), state="readonly")
    method_combobox.grid(row=3, column=1, padx=10, pady=5)
    method_combobox.current(0)  # Seleccionar por defecto la primera opción

    # Función para manejar el evento del botón

    def generate():
        function = function_entry.get()
        data = list(map(float, a_entry.get().split(',')))
        tolerance_ = float(tolerance.get())
        selected_method = method_combobox.get()

        print(f"Función: {function}, Punto a: {data}, Punto b: {tolerance_}, Método: {selected_method}")

        if selected_method == "Newton":
            x = sp.symbols('x')
            f = eval(function)

        else:
            f = convertir_funcion(function)

        respuesta = answer(selected_method, f, data, tolerance_)
        ttk.Label(frame_inputs, text="la respuesta es :" + str(respuesta) , background="#ffcccc", font=("Helvetica", 14)).grid(row=4, column=0,
        padx = 10, pady = 5)


    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)



    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])
