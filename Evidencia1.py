import datetime

print("*" *10 + " BIENVENIDO " + "*" *10)

while True:
    print("1. Registrar nuevo libro")
    print("2. Consultas y reportes")
    print("3. Salir")

libros = []
opción = int(input("Seleccione el número de la acción que desea realizar \n:"))

if opción == 1:
    print('******** REGISTRO DE NUEVO LIBRO ********')
    titulo = input('Ingrese el nombre de la obra: ').upper()
    autor = input('Ingrese el autor de la obra: ').upper()
    genero = input('Ingrese el genero de la obra: ').upper()
    año_publicacion = input("Ingrese el año de publicacion: ").upper()
    año_publicacion = datetime.datatime.striptime(año_publicacion,"%Y").date()   
    isbn=input("Ingrese el ISBN de la obra: ").upper
    fecha_adquisicion = input("Ingrese la fecha de su evento  (dd/mm/aaaa): ").upper
    fecha_adquisicion = datetime.datatime.striptime(fecha_adquisicion,"%d/%m/%Y").date()
    

elif opción == 2:
    while True:   
        print("1. Consulta de titulo")
        print("2. Reportes")
        print("3. Volver al menu de consultas y reportes")
    submenu_opcion = int(input("Seleccione el numero de la opcion que quiere elegir \n:" ))
    

else:
    print("ADIOS,GRACIAS POR VISITAR EL CATALOGO DE LIBROS")
exit()
