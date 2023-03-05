import datetime

print("*" *10 + " BIENVENIDO " + "*" *10)

while True:
    print("1. Registrar nuevo ejemplar")
    print("2. Consultas y reportes")
    print("3. Salir")
   
opción = int(input("Seleccione el número de la acción que desea realizar \n:"))

if opción == 1:
    print('******** REGISTRO DE NUEVO EJEMPLAR ********')
    titulo = input('Ingrese el nombre de la obra: ')
    autor = input('Ingrese el autor de la obra: ')
    genero = input('Ingrese el genero de la obra: ')
    año_publicacion=input("Ingrese el año de publicacion: ")
    año_publicacion = datetime.datatime.striptime(año_publicacion,"%Y").date()   
    isbn=input("Ingrese el ISBN de la obra: ") 
    fecha_adquisicion = input("Ingrese la fecha de su evento  (dd/mm/aaaa): ")
    fecha_adquisicion = datetime.datatime.striptime(fecha_adquisicion,"%d/%m/%Y").date()

elif opción == 2:
    print("1. Consulta de titulo")
    print("2. Reportes")
    print("3. Volver al menu de consultas y reportes")

elif opción == 3:
    print("ADIOS,GRACIAS POR VISITAR EL CATALOGO DE EJEMPLARES")
break
