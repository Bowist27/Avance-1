def Bienvenida():
    print('Bienvenido al sistema de calculación de impuestos 2070')

# Se hizo uso de un usuario y contraseña para poder acceder al codigo, se hizo uso de un for in range para dar limite de 3 intentos.
def  manejaArchivo(nombre):
    valor = input("Escriba su sugerencia:")
    respuesta = int(input("Esta de acuerdo con los terminos de privacidad? 1 para si, 2 para no"))
    if respuesta == 1:
        print("Usted ha aceptado los términos")
        file = open(nombre, "a")
    else:
        print("Ok no se enviará la sugerencia")
        file = open(nombre, "w")

    file.write(valor+ '\n')
    file.close()

    file = open(nombre, "r")
    file.seek(0)
    contenido = file.read()
    print(contenido)
    file.close()


# Funcion de prueba para evaluar el codigo
def Prueba():
    Predicción_Salario(500, 200, 0)
    Predicción_Productos(50, 'No', 500)


def Crear_Matriz(valor):
    matriz = []
    for i in range(1):
        matriz.append([0] * 1)
        for j in range(1):
            matriz[i][j] = valor
            return matriz


def Predicción_Salario(salario, impuestos):
    if salario <= 7734:
        impuestos = (salario * .0192)

    elif salario <= 65651:
        impuestos = (salario * .0640)

    elif salario <= 115000:
        impuestos = (salario * .1088)

    else:
        impuestos = (salario * .16)

    print('Tu debes', impuestos, 'borregoPesos de Impuestos')

    return impuestos


# Aun así cuenta con errores gramáticales

def Predicción_Productos(predicción_2, producto, precioproducto):
    lista_productos = ['Si', 'si', 'S', 'libro', 'libr', 'librp', 'joyeria', 'joyería', 'joyeri', 'arte', 'art', 'rte']

    if producto == (lista_productos[0]) or producto == (lista_productos[1]) or producto == (lista_productos[2]):
        print('No pagas Impuesto de ese producto')
    elif producto == (lista_productos[3]) or producto == (lista_productos[4]) or producto == (lista_productos[5]):
        print('No pagas Impuesto de ese producto')

    elif producto == (lista_productos[6]) or producto == (lista_productos[7]) or producto == (lista_productos[8]):
        print('No pagas Impuesto de ese producto')

    elif producto == (lista_productos[9]) or producto == (lista_productos[10]) or producto == (lista_productos[11]):
        print('No pagas Impuesto de ese producto')

    else:

        precioproductoimp = precioproducto * .16
        precioproductofinal = precioproductoimp + precioproducto
        precioimpuestos = precioproductofinal - precioproducto
        print('El producto cuenta con un precio de impuestos de', precioimpuestos,
              'pesos, quedando entonces el producto con un precio total de', precioproductofinal, 'pesos')

        matriz = [[predicción_2], [precioimpuestos]]
        # Se hará comparacion entre los dos datos de la matriz para hacer una grafica con una biblioteca
        print(matriz)


def Predicción_Productos_Importados():
    print('Esta area sigue en mantenimiento, vuelva pronto :{')


# Se asigna un menú para que este diga que tipo de impuestos va a querer calcular.
# Uso de separacion de menus con listas y saltos de linea
def menu():
    lista_menu = ['Este es el Menu principal seleccione la opcion que esté buscando', '1. Predecir Impuesto De Salario',
                  '2. Predecir Impuesto de Productos', '3. Predecir Impuesto de Productos Importados', '4. Salir', '5. Sugerencias']
    print(lista_menu[0], '\n', lista_menu[1], '\n', lista_menu[2], '\n', lista_menu[3], '\n', lista_menu[4], '\n', lista_menu[5])


# Al querer calcular mas impuestos, este entrará en un ciclo While True, esto debido a que en la interfaz grafica se podra seguri calculando sin necesidad de cerrar y volver a iniciar el programa.

# def crear_matriz():
def juntar_matrices(matriz1, matriz2):
    matriz = []
    matriz.append(matriz1)
    matriz.append(matriz2)
    return matriz


# Los usuarios van a ser algunos que yo ponga en una pagina y automaticamente se iran actualizando, necesita el uso de conexion en linea

# Contraseñas y usurios que vengan de una base de datos en línea

def main():
    Bienvenida()
    # Usuarios tienen que ser tomados de un servidor con sql, dirigidos a un hash para una mejor seguridad
    lista_users = ['Usuario1', 'Usuario2', 'Usuario3', 'Usuario4', 'Usuario5', 'Usuario6']
    lista_passwords = ['25632', '36985', '111', '222', '333', '555']

    for i in range(1, 4):
        user = input("USUARIO: ")
        password = input("CONTRASEÑA: ")
        if password == lista_passwords[0] and user == lista_users[0] or password == lista_passwords[1] and user == \
                lista_users[1] or password == lista_passwords[2] and user == lista_users[2] or password == \
                lista_passwords[3] and user == lista_users[3] or password == lista_passwords[4] and user == lista_users[
            4] or password == lista_passwords[5] and user == lista_users[5]:
            print("\nEl Usuario y contraseña son correctos!!!\n")
            while (True):
                # Prediccion de cliente se mueve al ccilo while para que le pregunte con cada prediccion
                # Uso de matriz para guardar datos para finalizar con comparación en grafica scaando el dato de la matriz con el dato resultante

                menu()
                opcion = (input())

                if opcion == '1':
                    predicción_2 = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?'))
                    matriz1 = Crear_Matriz(predicción_2)
                    print(matriz1)
                    impuestos = 0
                    salario = float(input('Escribe tu salario mensual?'))
                    variable = Predicción_Salario(salario, impuestos)
                    matriz2 = Crear_Matriz(variable)
                    print(matriz1,matriz2)
                    print(juntar_matrices(matriz1, matriz2))


                    # data to be plotted

                    # despues se manda a funcion y a libreria para hacer una grafica de comparacion


                elif opcion == '2':
                    predicción_3 = float(input('Cuanto crees que pagarás de impuestos al finalizar el cálculo?'))
                    matriz1 = Crear_Matriz(predicción_3)
                    print(matriz1)
                    producto = input('Tu producto es libro, joyeria o arte')
                    precioproducto = int(input('Cuánto te costó el producto?'))
                    Predicción_Productos(predicción_3, producto, precioproducto)



                elif opcion == '3':
                    print('Página Caida')

                elif opcion == '4':
                    print("Adios, tenga buen día")
                    break
                elif opcion == '5':
                    manejaArchivo("archivo.txt")


                else:
                    print("Por favor elija una opción correcta")
        else:
            print(f"\nLa Contraseña o el Usuario es Incorrecta, alejate niño. Lleva {i} intento/s de 3\n")
            if i == 3:
                print("\nHA FALLADO LOS 3 INTENTOS SALGA DEL PROGRAMA Y VUELVA A INTENTAR\n")
                break


main()
