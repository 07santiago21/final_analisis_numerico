import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import sympy as sp
from methods.InterpolacionAjuste import *


def Tk_InterpolacionAjuste(root):
    # Configuración de la ventana principal
    new_window = tk.Toplevel(root)
    new_window.title("Interpolación y Ajuste")
    new_window.geometry("1200x700")
    new_window.configure(bg="#0050ee")

    ttk.Button(new_window, style="Accent.TButton", text="volver", command=new_window.destroy).grid(row=0, column=0,
                                                                                                   padx=10, pady=10)

    title = ttk.Label(new_window, text="Interpolación y Ajuste", font=("Helvetica", 24), background="#0050ee")
    title.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    frame_inputs = ttk.Frame(new_window, padding="10", style="My.TFrame")
    frame_inputs.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Entrada de datos X
    ttk.Label(frame_inputs, text="Datos X (separados por comas):", background="#0068ee", font=("Helvetica", 14)).grid(
        row=0, column=0, padx=10, pady=5)
    x_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    x_entry.grid(row=0, column=1, padx=10, pady=5)

    # Entrada de datos Y
    ttk.Label(frame_inputs, text="Datos Y (separados por comas):", background="#0068ee", font=("Helvetica", 14)).grid(
        row=1, column=0, padx=10, pady=5)
    y_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    y_entry.grid(row=1, column=1, padx=10, pady=5)

    # Punto a aproximar
    ttk.Label(frame_inputs, text="Punto a aproximar:", background="#0068ee", font=("Helvetica", 14)).grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
    approx_entry = ttk.Entry(frame_inputs, width=30, font=("Helvetica", 14))
    approx_entry.grid(row=2, column=1, padx=10, pady=5)

    # Selección de método
    ttk.Label(frame_inputs, text="Seleccione método:", background="#0068ee", font=("Helvetica", 14)).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
    method_var = tk.StringVar()
    method_combo = ttk.Combobox(frame_inputs, textvariable=method_var,
                                values=["Polinomial Simple", "Polinomio de Lagrange", "Mínimos Cuadrados"],
                                state="readonly")
    method_combo.grid(row=3, column=1, padx=10, pady=5)

    style = ttk.Style()
    style.configure("My.TFrame", background="#0068ee")
    style.configure("Accent.TButton", font=("Helvetica", 14), background="#00ccff", foreground="#000000", relief="flat")
    style.map("Accent.TButton", background=[('active', '#00ccff')])

    response_label = ttk.Label(frame_inputs, text="", background="#0068ee", font=("Helvetica", 14))
    response_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate():

        try:
            x_data = list(map(float, x_entry.get().split(',')))
            y_data = list(map(float, y_entry.get().split(',')))
            approx_point_entry = approx_entry.get()

            # Limpiar el label de respuesta antes de actualizarlo
            response_label.config(text="")


            # Verificar si el punto aproximado está vacío
            if not approx_point_entry:
                approx_point = None
            else:
                approx_point = float(approx_point_entry)

            if method_var.get() == "Polinomial Simple":
                coef = Pol_simple_2(x_data, y_data)
                if approx_point is not None:
                    approx_value = Poly(coef, approx_point)
                    output_data = f"Polinomio Simple: {coef}\nAproximación en {approx_point}: {approx_value}"
                else:
                    output_data = f"Polinomio Simple: {coef}"

            elif method_var.get() == "Polinomio de Lagrange":
                pol = langrange_polinomio(x_data, y_data)
                P_x = sp.lambdify(sp.symbols('x'), pol)
                if approx_point is not None:
                    approx_value = P_x(approx_point)
                    output_data = f"Polinomio de Lagrange: {pol}\nAproximación en {approx_point}: {approx_value}"
                else:
                    output_data = f"Polinomio de Lagrange: {pol}"

            elif method_var.get() == "Mínimos Cuadrados":
                a0, a1 = minimos_cuadrados(np.array(x_data), np.array(y_data))
                if approx_point is not None:
                    approx_value = a0 + a1 * approx_point
                    output_data = f"Mínimos Cuadrados: y = {a0} + {a1}x\nAproximación en {approx_point}: {approx_value}"
                else:
                    output_data = f"Mínimos Cuadrados: y = {a0} + {a1}x"

            else:
                messagebox.showerror("Error", "Debe seleccionar un método de interpolación o ajuste")
                return

            # Actualizar el label con la salida
            response_label.config(text=output_data)
        except Exception as e:
            response_label.config(text=e)

    # Botón para generar gráficas
    ttk.Button(frame_inputs, text="Generar", style="Accent.TButton", command=generate).grid(row=4, column=1, pady=20)
