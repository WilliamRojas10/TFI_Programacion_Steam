from steam import *
steam = Plataforma()
steam.agregar_juego(1, 'Counter Strike', 'accion', 2012, 'Valve', 'Counter Strike', 'Valve', 150)
steam.agregar_juego(2, 'GTA V', 'accion', 2014, 'Rockstar North', 'Grand Thef Auto', 'Rockstar Games', 12000)
steam.agregar_juego(3, 'FIFA 23', 'deporte', 2022, 'EA Canada', 'EA Sports', 'Electronic Arts', 11999)
steam.agregar_juego(4, 'Call of Duty Black Ops II', 'accion', 2012, 'Treyarch', 'Call of Duty', 'Activision', 24500.99)
steam.agregar_juego(5, 'Mortal Kombat II', 'lucha', 2013, 'NetherRealm', 'Mortal kombat', 'Interactive Enternainment', 50)
steam.agregar_juego(6, 'No Mans Sky', 'supervivencia', 2016, 'Hello Games', 'No Mans Sky', 'Hello Gams', 3800)
steam.agregar_juego(7, 'Need for Speed Unbound', 'carreras', 2022, 'Criterion Games', 'Need for Speed', 'Electronic Arts', 10499)
steam.agregar_juego(8, 'Need for Speed Payback', 'carreras', 2017, 'Ghost Games', 'Need for Speed', 'Electronic Arts', 1399)



def menu_mostrar_juego(opcionID):
    #IMPLEMENTAR EN CAS M DE QUYE NO SE INGRESE NINGUNA OPCION
    if opcionID == 0:
        menu()
    print(" ")
    titulo = steam._juegos().obtener(3).titulo 
    print(steam.buscar_juego(titulo))
    print('\n0- Salir'
    '\n1- Atrás'
    '\n2- Comprar juego')
    opcion2 = int(input("Elige una opción: "))
    
    while opcion2 != 0:
        if int(opcion2) == 1:
            menu()
        if opcion2 == 2:
            nombreTarjeta = input("Escriba el NOMBRE de su tarjeta: ")
            numeroTarjeta = int(input("Ingrese el NÚMERO de su tarjeta: "))
            steam.get_usuario(dni, numeroTarjeta, nombreTarjeta)
            comprado = steam.comprar_juego(dni, titulo)
            if comprado:
                print(f"\nSe realizó su compra con éxito \n{titulo} se agregó a su Biblioteca")
                menu()
            else:
                menu_mostrar_juego(opcionID)
        else: 
            menu()

def menu_buscar_juego():
    juego = input("\nIngrese el titulo del juego: ")
    print(steam.buscar_juego(juego))
    print('\n1- Salir'
    '\n2- Atrás'
    '\n3- Comprar juego')
    opcion2 = int(input("Elige una opción: "))
    while opcion2 != 0:
        if opcion2 == 1:
            menu()
        if opcion2 == 2:
            menu_buscar_juego()
        if opcion2 == 3:
            nombreTarjeta = input("Escriba el NOMBRE de su tarjeta: ")
            numeroTarjeta = int(input("Ingrese el NÚMERO de su tarjeta: "))
            steam.get_usuario(dni, numeroTarjeta, nombreTarjeta)
            comprado = steam.comprar_juego(dni, juego)
            if comprado:
                print(f"\nSe realizó su compra con éxito \n{juego} se agregó a su Biblioteca")
                menu()
        else:
            menu()


def menu():
    print('\nBIENVENIDO A STEAM'
    '\n0- Salir'      
    '\n1- Ver juegos'
    '\n2- Ingresar a mi biblioteca' 
    '\n3- Buscar juego')
    opcion = int(input("Elige una opción: "))
    while opcion != 0:
        if opcion == 1:
            print('\n0 -> Atrás')
            steam.mostrar_juegos()
            opcionID = int(input("Ingrese el índice del juego: "))
            menu_mostrar_juego(opcionID)
        if opcion == 2:         
            print("\nSu biblioteca")
            steam.mostrar_biblioteca(dni)
            opc = int(input("\n0) Atrás \n1) Eliminar juego \nElige una opción: "))
            if opc == 0:
                menu()
            if opc == 1:
                biblioteca = steam.usuarios.obtener(dni).biblioteca
                indice = int(input("ingrese el indice del juego a eliminar: "))
                if indice == len(biblioteca):
                    del(biblioteca[indice-1])
                    print ("Juego eliminado")
                else:
                    print("No existe el indice ingresado o no hay juegos para eliminar")
            menu()
        if opcion == 3:
            menu_buscar_juego()
        
            
            
#test menu
opcion = 5
while opcion != 0:
    print("\n----- PLATAFORMA STEAM -----")
    print('0- Salir'
    '\n1- Iniciar sesión'
    '\n2- Crear cuenta')
    opcion= int(input("Elige una opción: "))
    if opcion == 1:
        print("\nINICIO DE SESIÓN")
        correo = input("Ingresa tu correo electronico: ")
        contrasenia = input("Ingresa tu contraseña: ")
        if steam.contiene_usuario(correo, contrasenia) == True:
            menu()
            break
        else:
            print("El usuario que ingresaste no existe ")
            opcion = 3
    elif opcion == 2:
          dni = int(input("Ingrese su DNI: "))
          nombre = input("Ingresa tu nombre: ")
          apellido = input("Ingresa tu apellido: ")
          telefono = int(input("Ingresa tu numero de teléfono: "))
          correo = input("Ingresa tu correo electronico: ")
          contrasenia = input("Ingresa tu contraseña: ")
          pais = input("Ingresa el nombre de pais: ")
          cp = int(input("Ingresa tu código postal: "))
          steam.crear_usuario(dni, nombre, apellido, telefono, correo, contrasenia, pais, cp)
          print("\nCuenta creada con éxito!")
    elif opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3: 
        print("Ingrese una opción válida")



