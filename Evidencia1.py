import datetime
import random

print("*" *10 + " BIENVENIDO " + "*" *10)

while True:
    print("1. Registrar nuevo libro")
    print("2. Consultas y reportes")
    print("3. Salir")

libros = []
def generar_id():
    return str(random.randint(100000, 999999))
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
    identificador = generar_id()
    libro={
        "id": identificador,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año_publicacion,
        "isbn": isbn,
        "fecha": fecha_adquisicion
    }
    libros.append(elibro)
    print("Libro registrado con éxito.")
    print("ID del libro:", identificador)

    libros.append(libro)
    print("Libro registrado con éxito.")
    print("ID del libro:", identificador)
    
elif opción == 2:
    while True:   
        print('******** CONSULTAS ********')
        print("Buscar libro por:")
        print("1. Título")
        print("2. ISBN")
        
    opcion = input("Opción: ")
    if opcion == "1":
        titulo_busqueda = input("Ingrese el título: ").upper()
        libros_encontrados = []
        for libro in libros:
            if libros["titulo"] == titulo_busqueda:
                libros_encontrados.append(libro)
    if libros_encontrados:
            print("libros encontrados:")
            for libro in libros_encontrados:
                print("ID:", libro["id"])
                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])
                print("Género:", libro["genero"])
                print("Año de publicación:", libro["anio"])
                print("ISBN:", libro["isbn"])
                print("Fecha de adquisición:", libro["fecha"])
        else:
        print("No se encontraron libros con ese título.")
    elif opcion == "2":
        isbn_busqueda = input("Ingrese el ISBN: ")
        libros_encontrados = []
        for libro in libros:
            if libro["isbn"] == isbn_busqueda:
                libros_encontrados.append(libro)
    if libros_encontrados:
            print("libros encontrados:")
            for libro in libros_encontrados:
                print("ID:", libro["id"])
                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])
                print("Género:", libro["genero"])
                print("Año de publicación:", libro["anio"])
                print("ISBN:", libro["isbn"])
                print("Fecha de adquisición:", libro["fecha"])
        else:
    

else:
    print("ADIOS,GRACIAS POR VISITAR EL CATALOGO DE LIBROS")
exit()
