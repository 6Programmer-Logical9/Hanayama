from tkinter import *

# Funciones
def salir():
    ventana.destroy()

def agregar():
    nota = texto.get(1.0, END)
    archivo = open("notas.txt", "a")
    archivo.write(nota)
    archivo.write("\n")
    archivo.close()

# Interfaz gráfica
ventana = Tk()
ventana.title("Notepad")

texto = Text(ventana, width=40, height=20)
texto.pack()

boton_salir = Button(ventana, text="Salir", command=salir)
boton_salir.pack()

boton_agregar = Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack()

# Ejecución
ventana.mainloop()