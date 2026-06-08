
especialistas = 0
residentes = 0

"""
╔══════════════════════════════════════════════════════════════╗
║       HOSPITAL CENTRAL METROPOLITANO                         ║
║       Sistema de Registro de Médicos                         ║
╚══════════════════════════════════════════════════════════════╝
"""

"mostrar encabezado del sistema"
print("=" * 45)
print("       HOSPITAL CENTRAL METROPOLITANO")    
print("    Sistema de Registro de Médicos Nuevos")
print("═" * 45)
 

while True:
    "registro de medicos"
    try:
        cantidad = int(input("    ¿cuantos medicos desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("¡Registro medico fallido! Ingresa un numero entero positivo para continuar.")
    except:
        print("¡Registro medico fallido! Ingresa un numero entero positivo para continuar.")


for i in range(cantidad):
    "registro de nombre de cada medico"
    print(f"\nRegistro de medicos # {i + 1}")
    while True:
        nombre = input("Ingrese nombre del profesional: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("formato del Nombre del profesional mal escrito.")


    while True:
        "registro de experiencia"
        try:
            experiencia = int(input("Ingrese años de experiencia: "))
            if experiencia >= 0:
                break
            else:
                print("¡Error! Ingresa un numero entero positivo para la experiencia.")
        except:
            print("¡Error! Ingresa un numero entero positivo para la experiencia.")


    if experiencia > 5:
        "clasificacion de cada medico"
        clasificacion = "Especialista Senior"
        especialistas += 1
    else:
        clasificacion = "Residente Junior"
        residentes += 1
    print("Clasificacion:", clasificacion)
  

    "final del registro de cada medico"
print("\nRecuento Final")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior! ¡registro exitoso!")