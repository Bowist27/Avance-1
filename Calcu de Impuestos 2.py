''' Primero saltará una interfaz gráfica al empezar el programa, esta cuenta con un menú
from tkinter import *
ventana = Tk()
ventana.geometry('1400x800')
ventana.title('Calculadora De Impuestos 2048')
lbl_Bienvenida=Label(text='Bienvenido a la calculadora de impuestos selecciona el ')

#Creación de Etiquetas de texto

#Creación de Menús
barraMenu=Menu(ventana)
mnuArchivo=Menu(barraMenu)
mnuEdición=Menu(barraMenu)
#Creación de archivos de barra para salida del programa general
mnuArchivo.add_command(label='Abrir')
mnuArchivo.add_command(label='Nuevo')
mnuArchivo.add_command(label='Guardar')
mnuArchivo.add_command(label='Cerrar')
mnuArchivo.add_separator()
mnuArchivo.add_command(label='Salir')
barraMenu.add_cascade(label='Archivo',menu=mnuArchivo)
mnuArchivo.add_checkbutton(delattr(label))

ventana.config(menu=barraMenu)

ventana.mainloop()
'''
#Creación de botones
# Por ahora dejaré pendiente la interfaz gráfica, pues toma más tiempo
#Creación de tutorial para aprender a usar programa básico, son tres paginas

def Predicción_cliente ():
    predicción = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?'))  # La prediccion se le hará solo si es que el cliente pide

def Bienvenida ():
    print('Bienvenido al sistema mágico de calculación de impuestos')


def main ():
    Predicción_cliente()
    salario= float(input('Escribe tu salario mensual?'))
    if salario <= 7734:
        impuestos = (salario * .0192)

    elif salario <= 65651:
        impuestos = (salario * .0640)

    elif salario <= 115000:
        impuestos = (salario * .1088)

    else:
        impuestos = (salario * .16)

    print('Tu debes', impuestos, 'borregoPesos de Impuestos')

main()




