import tkinter as tk
from tkinter import ttk


def Tk_EcuacionesDiferencial(root):
    new_window = tk.Toplevel(root)
    new_window.title("Ecuaciones Diferenciales")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)
    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).pack(pady=10)
    new_window.configure(bg="#0050ee")  # Fondo de la ventana

    # Crear el título
    title = ttk.Label(new_window, text="Ecuaciones Diferenciales", font=("Helvetica", 24), background="#0050ee")
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
    ttk.Label(frame_inputs, text="dato inicial o intervalo(separado por comas) :", background="#0068ee",
              font=("Helvetica", 14)).grid(row=1, column=0,
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



    # Botón de Generar
    generate_button = ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate)
    generate_button.grid(row=4, column=1, pady=20)

    # Ajustes de estilo
    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])