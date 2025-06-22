import tkinter as tk
from tkinter import messagebox

def mostrar_direccion():
    """Muestra un mensaje de alerta con la dirección."""
    messagebox.showinfo("Mensaje", "¡JICARO, NUEVA SEGOVIA!")

def mostrar_edad():
    """Muestra un mensaje de alerta con la edad."""
    messagebox.showinfo("Mensaje", "¡23 AÑOS!")

root = tk.Tk()
root.title("Examen I Parcial - ESTER CARRASCO")

# Establecer un color de fondo
root.configure(bg="pink")

# Etiqueta de título con el nombre del usuario
etiqueta_usuario = tk.Label(root, text="MI NOMBRE ES ESTER CARRASCO", font=("Arial", 18, "bold"), bg="pink")
etiqueta_usuario.pack(pady=100)

# Frame para los botones
frame_botones = tk.Frame(root, bg="pink")
frame_botones.pack(pady=20)

# Botón para mostrar dirección
boton_direccion = tk.Button(frame_botones, text="VIVO EN:", command=mostrar_direccion, width=15, font=("Arial", 14))
boton_direccion.pack(side="left", padx=70)

# Botón para mostrar edad
boton_edad = tk.Button(frame_botones, text="EDAD", command=mostrar_edad, width=15, font=("Arial", 14))
boton_edad.pack(side="right", padx=70)

# Configurar tamaño de la ventana
root.geometry("800x600")

# Ejecutar el bucle principal de la aplicación
root.mainloop()