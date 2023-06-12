
"""
Created on Mon Jun  5 19:54:23 2023
@author: pc
"""

class Mascota:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

def crear_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    mascota = Mascota(nombre, raza, edad)
    return mascota

def agregar_mascota(sistema, mascota):
    sistema.append(mascota)
    print("Mascota agregada correctamente.")

def mostrar_mascotas(sistema):
    if not sistema:
        print("No hay mascotas registradas.")
    else:
        print("Lista de mascotas:")
        for index, mascota in enumerate(sistema, start=1):
            print(f"Mascota {index}:")
            print(f"Nombre: {mascota.nombre}, Raza: {mascota.raza}, Edad: {mascota.edad}")
            print("")

# Lista de mascotas en el sistema
sistema_mascotas = []

print("Bienvenido al sistema de registro de mascotas 4.0")

opcion = ""
while opcion.lower() != "n":
    opcion = input("¿Desea ingresar una nueva mascota? (s/n): ")
    if opcion.lower() == "s":
        mascota = crear_mascota()
        agregar_mascota(sistema_mascotas, mascota)
    elif opcion.lower() != "n":
        print("Opción no válida. Por favor, ingrese 's' para agregar una mascota o 'n' para terminar.")

opcion_final = ""
while opcion_final.lower() != "salir":
    opcion_final = input("¿Qué desea hacer ahora?\nIngrese 'mostrar' para ver las mascotas ingresadas, 'continuar' para seguir ingresando mascotas o 'salir' para salir del programa: ")

    if opcion_final.lower() == "mostrar":
        mostrar_mascotas(sistema_mascotas)
    elif opcion_final.lower() == "continuar":
        sub_opcion = ""
        while sub_opcion.lower() != "n":
            sub_opcion = input("¿Desea ingresar una nueva mascota? (s/n): ")
            if sub_opcion.lower() == "s":
                mascota = crear_mascota()
                agregar_mascota(sistema_mascotas, mascota)
            elif sub_opcion.lower() != "n":
                print("Opción no válida. Por favor, ingrese 's' para agregar una mascota o 'n' para terminar.")
    elif opcion_final.lower() != "salir":
        print("Opción no válida. Por favor, ingrese una opción válida.")

print("Gracias por utilizar el sistema de Registro de mascotas 4.0. ¡Hasta luego!")
