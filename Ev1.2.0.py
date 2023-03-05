import datetime
import random

print(" " * 10 + " BIENVENIDO " + " " * 10)

libros = []


def generar_id():
    return str(random.randint(100000, 999999))


def buscar_libro_por_titulo(titulo_busqueda):
    libros_encontrados = []
    for libro in libros:
        if libro["titulo"] == titulo_busqueda:
            libros_encontrados.append(libro)
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print("Identificador:", libro["id"])
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            print("Año de publicación:", libro["año"])
            print("ISBN:", libro["isbn"])
            print("Fecha de adquisición:", libro["fecha"])
    else:
        print("No se encontraron libros con ese título.")


def buscar_libro_por_isbn(isbn_busqueda):
    libros_encontrados = []
    for libro in libros:
        if libro["isbn"] == isbn_busqueda:
            libros_encontrados.append(libro)
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print("ID:", libro["id"])
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            print("Año de publicación:", libro["año"])
            print("ISBN:", libro["isbn"])
            print("Fecha de adquisición:", libro["fecha"])
    else:
        print("No se encontraron libros con ese ISBN.")

while True:
    print("1. Registrar nuevo libro")
    print("2. Consultas y reportes")
    print("3. Salir")

    opcion = int(input("Seleccione el número de la acción que desea realizar:\n"))

    if opcion == 1:
        print('** REGISTRO DE NUEVO LIBRO **')
        titulo = input('Ingrese el nombre de la obra: ').upper()
        autor = input('Ingrese el autor de la obra: ').upper()
        genero = input('Ingrese el género de la obra: ').upper()
        año_publicacion = input("Ingrese el año de publicación: ")
        año_publicacion = datetime.datetime.strptime(año_publicacion, "%Y").date()
        isbn = input("Ingrese el ISBN de la obra: ")
        fecha_adquisicion = input("Ingrese la fecha de adquisición (dd/mm/aaaa): ")
        fecha_adquisicion = datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
        identificador = generar_id()
        libro = {
            "id": identificador,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "año": año_publicacion,
            "isbn": isbn,
            "fecha": fecha_adquisicion
        }
        libros.append(libro)
        print("Libro registrado con éxito.")
        print("ID del libro:", identificador)

    elif opcion == 2:
        while True:
            print('** CONSULTAS Y REPORTES ****')
            print("1. Consultas")
            print("2. Reportes")
            print("3. Volver al menú principal")

            opcion_menu_consultas = int(input("Seleccione el número de la acción que desea realizar:\n"))

            if opcion_menu_consultas == 1:
                titulo_o_isbn = input("Ingrese el título o ISBN del libro que desea buscar: ")
                if titulo_o_isbn.isdigit():
                    buscar_libro_por_isbn(titulo_o_isbn)
                else:
                    buscar_libro_por_titulo(titulo_o_isbn)

            elif opcion_menu_consultas == 2:
                print("Código para generar reportes de libros registrados")

            elif opcion_menu_consultas == 3:
                break  # Salir del ciclo de "Consultas y Reportes" y volver al menú principal

    elif opcion == 3:
        break  # Salir del programa
