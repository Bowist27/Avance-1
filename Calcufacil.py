# Primero saltará una interfaz gráfica al empezar el programa, esta cuenta con un menú
import tkinter as tk

#Colores Primera Parte
fondo_entrar = "#F51487"
fondo_menu = "#6DE1E4"
fondo_incorrecto = "#F51487"
fondo_entradausercontra = "#6DE1E4"
fondo_entradausercontra = "#FA1A1A"


ventana = tk.Tk()
ventana.title('Login')
ventana.geometry('1800x950')
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file='Calcula-Fácil (1).png')
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1 )
# En el caso de error de contraseña, se dispondra de 2 intentos más, despues de eso terminará el programa
#Letra Montserrat 30

#Creacion de Botones
botón1 = tk.Button(ventana, text='Entrar', cursor='hand2', bg = fondo_entrar, width= 10, relief='flat', font=("Comic Sans MS", 20, "bold"))
botón1.place(x=1450, y=800)




'''
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
'''

ventana.mainloop()



#Creación de botones
# Por ahora dejaré pendiente la interfaz gráfica, pues toma más tiempo
#Creación de tutorial para aprender a usar programa básico, son tres paginas

#Contraseña para poder iniciar la interfaz grafica.

#Propuesta de red neuronal para ingresar datos como dibujo y que los detecte como numeros en el menú





# Aquí empieza codigo de programa

#Se hacen funciones pues al seleccionar un boton en la interfaz gráfica este iniciará la función

def Bienvenida ():
    print('Bienvenido al sistema de calculación de impuestos 2070')


def Usuario():
    Usuario= int(input('Ingrese Usuario'))

def Contraseña():
    Contraseña= int(input('Ingrese Contraseña'))

# La prediccion se le hará solo si es que el cliente pide
def Predicción_cliente ():
    predicción = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?')) 

#Se hacen funciones pues al seleccionar un boton en la interfaz gráfica este iniciará la función

def Predicción_Salario():
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



def Predicción_Productos():
    print('jijiji2ja')

def Predicción_Productos_Importados():
    print(a)





# Se asigna un menú para que este diga que tipo de impuestos va a querer calcular. 

def menu():
    print('Este es el Menu principal seleccione la opcion que esté buscando')
    print("1. Predecir Impuesto De Salario")
    print("2. Predecir Impuesto de Productos")
    print("3. Predecir Impuesto de Productos Importados")
    print("4. Salir")
        


# Al querer calcular mas impuestos, este entrará en un ciclo While True, mientras quiera seguir añadiendo más
# este tendrá que escribir la palabra 'Si'. 

def main ():
    Bienvenida()
    Predicción_cliente()
    while(True):
        menu()
        opcion = (input( ))

        if opcion=='1':
            Predicción_Salario()
        
        elif opcion == '2':
            Predicción_Productos()

        elif opcion == '3':
            Predicción_cliente()
            
        elif opcion == '4':
            print("Adios, tenga buen día")

            break
        
        else:
            print("Por favor elija una opción correcta")
  
main()