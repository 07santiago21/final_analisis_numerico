import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.SerieTaylor import *
import sympy as sp
import numpy as np



def mostrar_notificacion(mensaje):
    messagebox.showwarning("Advertencia", mensaje)


def plot_graph(x_data, y_polinomio,y_f):
    # Crear una nueva figura con un tamaño fijo (ancho x alto en pulgadas)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x_data, y_polinomio,"b",label="polinomio")
    ax.plot(x_data, y_f, "r", label="funcion")
    ax.legend()

    ax.set(xlabel='x', ylabel='y', title='Gráfica de Datos')
    ax.grid()

    return fig

def on_plot(x0,f,serie_taylor,x, frame_plot):

    x_data =np.linspace(x0-2, x0+2, 100)

    puntos_polinomio = sp.lambdify(x, serie_taylor)
    puntos_funcion = sp.lambdify(x, f)

    y_polinomio = puntos_polinomio(x_data)
    y_funcion = puntos_funcion(x_data)

    # Crear la gráfica
    fig = plot_graph(x_data, y_polinomio, y_funcion)

    # Limpiar el frame de la gráfica anterior
    for widget in frame_plot.winfo_children():
        widget.destroy()

    # Crear un canvas de tkinter para la gráfica de Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)






def Tk_SerieTaylor(root):
    new_window = tk.Toplevel(root)
    new_window.title("Series de Taylor")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=10)
    new_window.configure(bg="#0050ee")  # Fondo de la ventana

    # Crear el título
    title = ttk.Label(new_window, text="Series de Taylor", font=("Helvetica", 24), background="#0050ee")
    title.pack(pady=10)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)

    # Función de entrada
    ttk.Label(frame_inputs, text="Función con (x):", background="#0068ee", font=("Helvetica", 14)).grid(row=0, column=0,
                                                                                                padx=10, pady=5)
    function_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    function_entry.grid(row=0, column=1, padx=10, pady=5)

    # Punto a
    ttk.Label(frame_inputs, text="punto(x_0) (en numero )", background="#0068ee",
              font=("Helvetica", 14)).grid(row=1, column=0,
                                           padx=10, pady=5)
    punto = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    punto.grid(row=1, column=1, padx=10, pady=5)

    # Punto b
    ttk.Label(frame_inputs, text="grado del polinomio(en numero):", background="#0068ee", font=("Helvetica", 14)).grid(row=2, column=0,
                                                                                                  padx=10, pady=5)
    grado_p = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    grado_p.grid(row=2, column=1, padx=10, pady=5)

    response_label = ttk.Label(frame_inputs, text="", background="#0068ee", font=("Helvetica", 14))
    response_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate():

        try:

            function = function_entry.get()
            punto_ = float(punto.get())
            grado = int(grado_p.get())


            x = sp.symbols("x")
            f = eval(function)
            print(f"Función: {function}, Punto: {punto_}, grado: {grado}")

            respuesta = Serie_Taylor(f, punto_, grado,x)

        except:
            mostrar_notificacion("ingrese los datos en el formato solicitado")


        try:
            on_plot(punto_, f, respuesta, x, frame_plot)


            response_label.config(text="el polinomio es es: " + str(respuesta),background="#ffcccc")
        except:
            mostrar_notificacion("problema al graficar")




    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)

    # Crear un frame para la gráfica
    frame_plot = ttk.Frame(new_window)
    frame_plot.pack(pady=10, fill='both', expand=True)



    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])
