#Lista vacia ,para que el usuario recorra los valores de la lista
nombres_estudiantes = []

#function for  list add
def agregar_estudiante(nombre):
    nombres_estudiantes.append(nombre)
    print(f"{nombre},ha sido agragado a la lista")

#functions for list order
def ordenar_estudiante():
    nombres_estudiantes.sort()
    print("La lista ha sido ordenadamente alfabeticamente")
    for nombre in nombres_estudiantes:
        print("El nombre del estudiante:")

while True:
    print("/n Menú:") 
    print("1.Agregar estudiantes")
    print("2.Ordenar estudiantes alfabeticamente")
    print("3.Salir")
    opcion = input("Seleccione una opcion(1,2,3): ")

    if  opcion == '1':
        nombre = input("Ingrese el nombre del estudiante:")
        agregar_estudiante(nombre)
    elif opcion == '2':
        ordenar_estudiante()
    elif opcion =='3':
        print("Salir del programa")
else:
    print("Opción no  valida, intente de nuevo")
     



