import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.CerosFunciones import *


def plot_graph(x_data, y_data):
    # Crear una nueva figura con un tamaño fijo (ancho x alto en pulgadas)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x_data, y_data, marker='o')

    ax.set(xlabel='x', ylabel='y', title='Gráfica de Datos')
    ax.grid()

    return fig


def answer(name, f, data, tol):
    if len(data) > 0 and len(data) < 3:

        if name == "Newton":
            result = newton(f, data[0], tol)
            print(result)

        if len(data) == 1:
            print("no se puede , alerta")

        elif name == "Bisección":

            print(biseccion(f, data[0], data[1], tol))

        elif name == "Falsa posición":

            print(posicion_falsa(f, data[0], data[1], tol))
        else:

            print(secante(f, data[0], data[1], tol))

    else:
        print("arreglar alerta")


def on_plot(x_data, y_data, frame_plot):
    # Crear la gráfica
    fig = plot_graph(x_data, y_data)

    # Limpiar el frame de la gráfica anterior
    for widget in frame_plot.winfo_children():
        widget.destroy()

    # Crear un canvas de tkinter para la gráfica de Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def Tk_CerosFunciones(root):
    new_window = tk.Toplevel(root)
    new_window.title("Ceros de Funciones")
    new_window.geometry("1200x700")  # Tamaño de la ventana

    new_window.configure(bg="#ffcccc")  # Fondo de la ventana

    # Crear el título
    title = ttk.Label(new_window, text="Ceros de funciones", font=("Helvetica", 24), background="#ffcccc")
    title.pack(pady=10)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)

    # Función de entrada
    ttk.Label(frame_inputs, text="Función:", background="#ffcccc", font=("Helvetica", 14)).grid(row=0, column=0,
                                                                                                padx=10, pady=5)
    function_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    function_entry.grid(row=0, column=1, padx=10, pady=5)

    # Punto a
    ttk.Label(frame_inputs, text="Punto a:", background="#ffcccc", font=("Helvetica", 14)).grid(row=1, column=0,
                                                                                                padx=10, pady=5)
    a_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    a_entry.grid(row=1, column=1, padx=10, pady=5)

    # Punto b
    ttk.Label(frame_inputs, text="Punto b:", background="#ffcccc", font=("Helvetica", 14)).grid(row=2, column=0,
                                                                                                padx=10, pady=5)
    tolerance = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    tolerance.grid(row=2, column=1, padx=10, pady=5)

    # Selección del método
    ttk.Label(frame_inputs, text="Método:", background="#ffcccc", font=("Helvetica", 14)).grid(row=3, column=0, padx=10,
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
        answer(selected_method,function, data,tolerance_)

    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)

    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#ffcccc")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])
