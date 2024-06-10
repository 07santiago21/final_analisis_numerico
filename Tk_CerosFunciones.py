import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_graph(x_data, y_data):
    # Crear una nueva figura con un tamaño fijo (ancho x alto en pulgadas)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x_data, y_data, marker='o')

    ax.set(xlabel='x', ylabel='y', title='Gráfica de Datos')
    ax.grid()

    return fig

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
    new_window.title("CerosFunciones")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)

    ttk.Label(new_window, text="Ceros de Funciones").pack(pady=20)

    # Campos de entrada para los datos
    frame_inputs = ttk.Frame(new_window)
    frame_inputs.pack(pady=10)

    ttk.Label(frame_inputs, text="Datos X (separados por comas):").grid(row=0, column=0, padx=5, pady=5)
    x_entry = ttk.Entry(frame_inputs, width=50)
    x_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_inputs, text="Datos Y (separados por comas):").grid(row=1, column=0, padx=5, pady=5)
    y_entry = ttk.Entry(frame_inputs, width=50)
    y_entry.grid(row=1, column=1, padx=5, pady=5)

    # Crear un frame para la gráfica
    frame_plot = ttk.Frame(new_window)
    frame_plot.pack(pady=10, fill='both', expand=True)

    # Botón para generar la gráfica
    plot_button = ttk.Button(new_window, text="Generar Gráfica", command=lambda: on_plot(
        list(map(float, x_entry.get().split(','))),
        list(map(float, y_entry.get().split(','))),
        frame_plot
    ))
    plot_button.pack(pady=10)

    ttk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

