from tkinter import CASCADE
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

#Funcion de prueba para evaluar el codigo 
def Prueba():
    Predicción_Salario(500,200,0)
    Predicción_Productos(50,'No',500)

    # Predicción_Productos('Si')

# La prediccion se hace al principio para despues comparar su resultado de un unico impuesto o suma de estos.

#matplotlib agregar para 
#Se hacen funciones pues al seleccionar un boton en la interfaz gráfica este iniciará la función

def Predicción_Salario(salario,predicción_2,impuestos):

    if salario <= 7734:
        impuestos = (salario * .0192)
        
    elif salario <= 65651:
        impuestos = (salario * .0640)

    elif salario <= 115000:
        impuestos = (salario * .1088)

    else:
        impuestos = (salario * .16)

    print('Tu debes', impuestos, 'borregoPesos de Impuestos')

    matriz = [[predicción_2],[impuestos]]
    print(matriz)


#Aun así cuenta con errores gramáticales 

def Predicción_Productos(predicción_2,producto,precioproducto):

    lista_productos = ['Si','si','S','libro','libr','librp','joyeria','joyería','joyeri','arte','art','rte']
    
    if producto == (lista_productos[0]) or producto == (lista_productos[1]) or producto == (lista_productos[2]):
        print('No pagas Impuesto de ese producto')
    elif producto == (lista_productos[3]) or producto == (lista_productos[4]) or producto == (lista_productos[5]):
        print('No pagas Impuesto de ese producto')

    elif producto == (lista_productos[6]) or producto == (lista_productos[7]) or producto == (lista_productos[8]):
        print('No pagas Impuesto de ese producto')

    elif producto == (lista_productos[9]) or producto == (lista_productos[10]) or producto == (lista_productos[11]):
        print('No pagas Impuesto de ese producto')
        
    else:
        
        precioproductoimp = precioproducto*.16
        precioproductofinal = precioproductoimp + precioproducto
        precioimpuestos = precioproductofinal - precioproducto
        print('El producto cuenta con un precio de impuestos de',precioimpuestos,'pesos, quedando entonces el producto con un precio total de',precioproductofinal, 'pesos')
        matriz = [[predicción_2],[precioimpuestos]]
        #Se hará comparacion entre los dos datos de la matriz para hacer una grafica con una biblioteca
        print(matriz)

def Predicción_Productos_Importados():
    print('Esta area sigue en mantenimiento, vuelva pronto :{')



# Se asigna un menú para que este diga que tipo de impuestos va a querer calcular. 
#Uso de separacion de menus con listas y saltos de linea
def menu():
    lista_menu = ['Este es el Menu principal seleccione la opcion que esté buscando', '1. Predecir Impuesto De Salario','2. Predecir Impuesto de Productos','3. Predecir Impuesto de Productos Importados', '4. Salir']
    print(lista_menu[0],'\n',lista_menu[1],'\n',lista_menu[2],'\n',lista_menu[3],'\n',lista_menu[4])      


# Al querer calcular mas impuestos, este entrará en un ciclo While True, esto debido a que en la interfaz grafica se podra seguri calculando sin necesidad de cerrar y volver a iniciar el programa.

#def crear_matriz():

# Los usuarios van a ser algunos que yo ponga en una pagina y automaticamente se iran actualizando, necesita el uso de conexion en linea

#Contraseñas y usurios que vengan de una base de datos en línea

def main ():
    Bienvenida()
    #Usuarios tienen que ser tomados de un servidor con sql, dirigidos a un hash para una mejor seguridad 
    lista_users = ['Usuario1','Usuario2','Usuario3','Usuario4','Usuario5','Usuario6']
    lista_passwords = ['25632','36985','111','222','333','555']

    for i in range(1,4):
        user = input( "USUARIO: ")
        password = input( "CONTRASEÑA: ")
        if password == lista_passwords[0] and user == lista_users[0] or password == lista_passwords[1] and user == lista_users[1] or password == lista_passwords[2] and user == lista_users[2] or password == lista_passwords[3] and user == lista_users[3] or password == lista_passwords[4] and user == lista_users[4] or password == lista_passwords[5] and user == lista_users[5]:
            print("\nEl Usuario y contraseña son correctos!!!\n")
            while(True):
                #Prediccion de cliente se mueve al ccilo while para que le pregunte con cada prediccion
                #Uso de matriz para guardar datos para finalizar con comparación en grafica scaando el dato de la matriz con el dato resultante

                menu()
                opcion = (input())

                if opcion=='1':
                    predicción_2 = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?'))
                    impuestos = 0
                    salario= float(input('Escribe tu salario mensual?'))
                    Predicción_Salario(salario, predicción_2, impuestos)
                
                
                    #despues se manda a funcion y a libreria para hacer una grafica de comparacion
                    

                elif opcion == '2':
                    predicción_2 = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?'))
                    producto= input('Tu producto es libro, joyeria o arte')
                    precioproducto= int(input('Cuánto te costó el producto?'))
                    Predicción_Productos(predicción_2,producto, precioproducto)
                    

                    #despues se manda a funcion y a libreria para hacer una grafica de comparacion

                elif opcion == '3':
                    print('Si')
                    #despues se manda a funcion y a libreria para hacer una grafica de comparacion
                elif opcion == '4':
                    print("Adios, tenga buen día")
                    break
                else:
                    print("Por favor elija una opción correcta")     
        else:
            print(f"\nLa Contraseña o el Usuario es Incorrecta, alejate niño. Lleva {i} intento/s de 3\n")
            if i == 3:
                print("\nHA FALLADO LOS 3 INTENTOS SALGA DEL PROGRAMA Y VUELVA A INTENTAR\n")
                break
  
#main()
Prueba()
