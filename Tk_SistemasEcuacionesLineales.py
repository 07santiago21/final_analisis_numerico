import tkinter as tk
from tkinter import ttk, messagebox
import ast

import numpy as np

from methods.SistemasEcuacionesLineales import Gauss_s,gauss_seidel_sumatorias,eliminacion_gaussiana,pivot




def mostrar_notificacion(mensaje):
    messagebox.showwarning("Advertencia", mensaje)

def answer(A,B,method):
    try:
        if method == "Eliminacion gaussiana":
            return eliminacion_gaussiana(A,B)
        elif method == "pivoteo":
            return pivot(A,B)
        elif method == "Gauss Seidel":
            return Gauss_s(A,B)
        else:
            return gauss_seidel_sumatorias(A,B)
    except:
        mostrar_notificacion("error al ejecutar este metodo, no se puede")



def Tk_SistemasEcuacionesLineales(root):
    new_window = tk.Toplevel(root)
    new_window.title("Sistemas de Ecuaciones Lineales")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=10)
    new_window.configure(bg="#0050ee")  # Fondo de la ventana

    # Crear el título
    title = ttk.Label(new_window, text="Sistemas de Ecuaciones Lineales", font=("Helvetica", 24), background="#0050ee")
    title.pack(pady=10)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)


    # Punto a
    ttk.Label(frame_inputs, text="Matriz A:", background="#0068ee",
              font=("Helvetica", 14)).grid(row=1, column=0,
                                           padx=10, pady=5)
    A = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    A.grid(row=1, column=1, padx=10, pady=5)

    # Punto b
    ttk.Label(frame_inputs, text="B:", background="#0068ee", font=("Helvetica", 14)).grid(row=2, column=0,
                                                                                                  padx=10, pady=5)
    B = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    B.grid(row=2, column=1, padx=10, pady=5)


    # Selección del método
    ttk.Label(frame_inputs, text="Método:", background="#0068ee", font=("Helvetica", 14)).grid(row=3, column=0, padx=10,
                                                                                               pady=5)
    method_combobox = ttk.Combobox(frame_inputs, values=["Eliminacion gaussiana", "pivoteo", "Gauss Seidel", "Gauss Seidel sumas"],
                                   font=("Helvetica", 14), state="readonly")
    method_combobox.grid(row=3, column=1, padx=10, pady=5)
    method_combobox.current(0)  # Seleccionar por defecto la primera opción

    especificaciones_label = ttk.Label(new_window, text="Especificaciones", font=("Helvetica", 18),
                                       background="#0050ee")
    especificaciones_label.pack(pady=10)

    especificaciones_label1 = ttk.Label(new_window, text="en matriz A y en el dato B se tienen que ingresar los datos de la siguiente forma", font=("Helvetica", 18),
                                       background="#0050ee")
    especificaciones_label1.pack(pady=10)

    especificaciones_label2 = ttk.Label(new_window, text="ejemplo matriz A= [-3., 2., 1.], [6., -8., -2.], [1., -1., -2.]", font=("Helvetica", 18),
                                       background="#0050ee")
    especificaciones_label2.pack(pady=10)

    especificaciones_label3 = ttk.Label(new_window, text="ejemplo B = [2., 1., 3.]", font=("Helvetica", 18),
                                       background="#0050ee")
    especificaciones_label3.pack(pady=10)

    # Función para manejar el evento del botón

    response_label = ttk.Label(frame_inputs, text="", background="#0068ee", font=("Helvetica", 14))
    response_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    def generate():

        try:
            A_ = A.get()
            B_ = B.get()
            selected_method = method_combobox.get()

            A_string = f'[{A_}]'
            A_M = ast.literal_eval(A_string)
            list_of_lists = [[float(item) for item in sublist] for sublist in A_M]
            A_M = np.array(list_of_lists)


            B_string = f'{B_}'
            B_M = ast.literal_eval(B_string)
            list_of_lists_B = [float(sublist) for sublist in B_M]
            B_M = np.array(list_of_lists_B)

        except:
            mostrar_notificacion("ingrese los datos en el formato solicitado")

        print(f"A: {A_M},B: {B_M}, metodo: {selected_method}")

        respuesta = answer(A_M, B_M, selected_method)
        print(respuesta)
        response_label.config(text="La respuesta es: " + str(respuesta),background="#ffcccc")



    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)

    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])