import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.CerosFunciones import *
import sympy as sp
import numpy as np


def mostrar_notificacion(mensaje):
    messagebox.showwarning("Advertencia", mensaje)

def convertir_funcion(input_usuario):
    return lambda x: eval(input_usuario)

def answer(name, f, data, tol):

    try:

        if len(data) > 0 and len(data) < 3:

            if name == "Newton" and len(data) == 1:

                return newton(f, data[0], tol)

            if len(data) == 1:

                mostrar_notificacion("ingrese los datos correctamente")
                return "ingrese los datos correctamente"

            elif name == "Bisección":

                return biseccion(f, data[0], data[1], tol)

            elif name == "Falsa posición":

                return posicion_falsa(f, data[0], data[1], tol)
            elif name == "Secante":

                return secante(f, data[0], data[1], tol)

            else:

                mostrar_notificacion("ingrese los datos correctamente")
                return "ingrese los datos correctamente"

        else:
            mostrar_notificacion("ingrese los datos correctamente")
            return "ingrese los datos correctamente"

    except:
        mostrar_notificacion("no se puede realizar ")


def Tk_CerosFunciones(root):
    new_window = tk.Toplevel(root)
    new_window.title("Ceros de Funciones")
    new_window.geometry("1200x700")  # Tamaño de la ventana

    new_window.configure(bg="#0050ee")  # Fondo de la ventana
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=5)
    # Crear el título
    title = ttk.Label(new_window, text="Ceros de funciones", font=("Helvetica", 20), background="#0050ee")
    title.pack(pady=5)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)

    # Función de entrada
    ttk.Label(frame_inputs, text="Función con (x):", background="#0068ee", font=("Helvetica", 14)).grid(row=0, column=0,
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



    especificaciones_label = ttk.Label(new_window, text="Especificaciones", font=("Helvetica", 10),
                                       background="#0050ee")
    especificaciones_label.pack(pady=5)

    especificaciones_label1 = ttk.Label(new_window,
                                        text="en el campo de función se tiene que pasar con la variable x",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label1.pack(pady=5)

    especificaciones_label4 = ttk.Label(new_window,
                                        text="ejemplo funcion = 10*(0.5*np.pi-np.arcsin(x)-h*np.sqrt(1-x**2))-10",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label4.pack(pady=5)


    especificaciones_label2 = ttk.Label(new_window,
                                        text="en exactitud se debe pasar un numero",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label2.pack(pady=5)

    especificaciones_label5 = ttk.Label(new_window,
                                        text="ejemplo de exactitud = 1e-5 o tambien 0.00001",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label5.pack(pady=5)


    especificaciones_label3 = ttk.Label(new_window, text="en dato inicial o intervalo se tiene que pasar los datos justos para el metodo", font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label3.pack(pady=5)


    especificaciones_label6 = ttk.Label(new_window,
                                        text="Biseccion solicita dos datos = 0,1 ",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label6.pack(pady=5)

    especificaciones_label7 = ttk.Label(new_window,
                                        text="Newton solicita un dato = 1 ",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label7.pack(pady=5)

    especificaciones_label8 = ttk.Label(new_window,
                                        text="Falsa posicion solicita dos datos = 1,2 ",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label8.pack(pady=5)

    especificaciones_label9 = ttk.Label(new_window,
                                        text="Secante solicita dos datos = 2,3 ",
                                        font=("Helvetica", 10),
                                        background="#0050ee")
    especificaciones_label9.pack(pady=5)






    response_label = ttk.Label(frame_inputs, text="", background="#0068ee", font=("Helvetica", 14))
    response_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    def generate():

        try:
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
            response_label.config(text="La respuesta es: " + str(respuesta),background="#ffcccc")

        except:
            mostrar_notificacion("ingrese los datos en el formato solicitado")


    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)



    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])
