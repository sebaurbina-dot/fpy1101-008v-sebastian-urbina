
"""
╔══════════════════════════════════════════════════════════════╗
║           BIBLIOTECA CENTRAL                                 ║
║           Sistema de Gestión de Préstamos                    ║
╚══════════════════════════════════════════════════════════════╝
"""

libros = 120
prestamos = 0
prestamos_u = 0
prestamo_devuelto = 0 


print("╔═════════════════════════════════╗")
print("║      BIBLIOTECA CENTRAL         ║")
print("║ Sistema de Gestión de Préstamos ║")
print("╚═════════════════════════════════╝")


while True:
    print("\n   Menu Principal \n 1 Libros disponibles 📚 \n 2 Realizar prestamo \n 3 Devolver prestamo \n 4 prestamos activos \n 5 Salir")   

    while True:
        try:
            opcion = int(input("   Ingrese la opcion: "))
            if opcion > 0 and opcion <= 5:
                break
            else:
                print("\nDebe ingresar una de las opciones")
        except:
            print("Debe ingresar unas de las opciones")

    if opcion == 1: 
        print(f"Libros disponibles : {libros}")

    if opcion == 2:
        while True:
            try:
                prestamos_u = int(input("numero de libros que desea llevar: ")) 
                if prestamos_u > 0:
                    if prestamos_u <= libros:
                        prestamos = prestamos + prestamos_u
                        libros = libros - prestamos_u
                        print(f"¡Prestamo realizado!, quedan: {libros} libros")
                        break
                    else:
                        print("\n no hay stock")
                else:
                    print("\nDebe ser un numero mayor valido")
            except:
                print("\nDebe ingresar un numero valido ")

    if opcion == 3:
        while True:
            try:
                prestamo_devuelto = int(input("Cuantos devuelve?: "))
                if prestamo_devuelto > 0:
                    if prestamo_devuelto <= prestamos:
                        prestamos = prestamos - prestamo_devuelto
                        libros = libros + prestamo_devuelto
                        print(f"Devolvio, {prestamo_devuelto} libros, quedan: {libros} libros")
                        break   
                    else:
                        print("Debe ser menor que los libros totales")
                else:
                    print("\nDebe ser un numero mayor a 0") 
            except:
                print("\nDebe ser un numero mayor a 0")
    if opcion == 4:
        print(f"Prestamos activo: {prestamos}, quedan: {libros} libros")
    if opcion == 5:
        print("\nGracias por usar nuestro servicio, hasta pronto")
        break