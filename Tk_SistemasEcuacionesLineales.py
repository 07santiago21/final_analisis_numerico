import tkinter as tk
from tkinter import ttk


def Tk_SistemasEcuacionesLineales(root):
    new_window = tk.Toplevel(root)
    new_window.title("Sistemas de Ecuaciones Lineales")
    new_window.geometry("1200x700")  # Tamaño fijo (ancho x alto)
    ttk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)