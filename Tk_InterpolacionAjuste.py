import tkinter as tk
from tkinter import ttk


def Tk_InterpolacionAjuste(root):
    new_window = tk.Toplevel(root)
    new_window.title("Interpolacion y Ajuste")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=10)
    new_window.configure(bg="#0050ee")  # Fondo de la ventana

    # Crear el título
    title = ttk.Label(new_window, text="Interpolacion y Ajuste", font=("Helvetica", 24), background="#0050ee")
    title.pack(pady=10)

    # Crear un frame para las entradas
    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.pack(pady=10)

    # Punto a
    ttk.Label(frame_inputs, text="datos de x:", background="#0068ee",
              font=("Helvetica", 14)).grid(row=1, column=0,
                                           padx=10, pady=5)
    x = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    x.grid(row=1, column=1, padx=10, pady=5)

    # Punto b
    ttk.Label(frame_inputs, text="datos de y:", background="#0068ee", font=("Helvetica", 14)).grid(row=2, column=0,
                                                                                          padx=10, pady=5)
    y = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    y.grid(row=2, column=1, padx=10, pady=5)

    # Función de entrada
    ttk.Label(frame_inputs, text="dato que se desea aproximar:", background="#0068ee", font=("Helvetica", 14)).grid(row=0, column=0,
                                                                                                   padx=10, pady=5)
    aprox = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    aprox.grid(row=0, column=1, padx=10, pady=5)

    # Selección del método
    ttk.Label(frame_inputs, text="Método:", background="#0068ee", font=("Helvetica", 14)).grid(row=3, column=0, padx=10,
                                                                                               pady=5)
    method_combobox = ttk.Combobox(frame_inputs,
                                   values=["Polinomial Simple","Lagrange", "Mínimos cuadrados"],
                                   font=("Helvetica", 14), state="readonly")
    method_combobox.grid(row=3, column=1, padx=10, pady=5)
    method_combobox.current(0)  # Seleccionar por defecto la primera opción

    # Función para manejar el evento del botón

    def generate():
        x_data = x.get()
        y_data = y.get()
        data_aprox = float(aprox.get())
        selected_method = method_combobox.get()

        print(f"x: {x_data},y: {y_data}, data aprox: {data_aprox}, metodo: {selected_method}")

    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)


    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])