'''
# Primero saltará una interfaz gráfica al empezar el programa, esta cuenta con un menú
'''
'''
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
#Ya se hicieron los botones de la primera interfaz que tiene de fondo la entrada al programa asi como la de negativa en caso de falla de contraseña
# Se deja pendiente el tutorial de la interfaz gráfica

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


ventana.mainloop()
'''




#Creación de botones
# Por ahora dejaré pendiente la interfaz gráfica, pues toma más tiempo
#Creación de tutorial para aprender a usar programa básico, son tres paginas

#Contraseña para poder iniciar la interfaz grafica.



# Aquí empieza codigo de programa

#Se hacen funciones pues al seleccionar un boton en la interfaz gráfica este iniciará la función

def Bienvenida ():
    print('Bienvenido al sistema de calculación de impuestos 2070')

#Se hizo uso de un usuario y contraseña para poder acceder al codigo, se hizo uso de un for in range para dar limite de 3 intentos.

def Usuario_Contraseña():
    Usuario1='Usuario1'
    Usuario2='Usuario2'
    contraseña1="25632"
    contraseña2="36985"
    for i in range(1,4):
        d=input("USUARIO: ")
        c=input("CONTRASEÑA: ")
        if c == contraseña1 or c == contraseña2 or d == Usuario1 or d == Usuario2:
            print("\nEl Usuario y contraseña son correctos!!!\n")
            break
        else:
            print(f"\nLa Contraseña o el Usuario es Incorrecta, alejate niño. Lleva {i} intento/s de 3\n")
            if i == 3:
                print("\nHA FALLADO LOS 3 INTENTOS SALGA DEL PROGRAMA Y VUELVA A INTENTAR\n")
                break



# La prediccion se hace al principio para despues comparar su resultado de un unico impuesto o suma de estos.
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
    producto= input('Tu producto es libro, joyeria o arte')
    if producto == ('Si') or producto == ('si'):
        print('No pagas Impuesto de ese producto')
    else:
        precioproducto= int(input('Cuánto te costó el producto?'))
        precioproductofinal= precioproducto*.16
        sumaprecios= precioproductofinal + precioproducto
        print('El producto cuenta con un precio de impuestos de',sumaprecios, 'pesos')


def Predicción_Productos_Importados():
    print('Esta area sigue en mantenimiento, vuelva pronto :D')




# Se asigna un menú para que este diga que tipo de impuestos va a querer calcular. 
#Propuesta de red neuronal para ingresar datos como dibujo y que los detecte como numeros en el menú

def menu():
    print('Este es el Menu principal seleccione la opcion que esté buscando')
    print("1. Predecir Impuesto De Salario")
    print("2. Predecir Impuesto de Productos")
    print("3. Predecir Impuesto de Productos Importados")
    print("4. Salir")
        


# Al querer calcular mas impuestos, este entrará en un ciclo While True, esto debido a que en la interfaz grafica se podra seguri calculando sin necesidad de cerrar y volver a iniciar el programa.

def main ():
    Bienvenida()
    Usuario_Contraseña()
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
