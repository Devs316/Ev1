import datetime
import random

print(" " * 10 + " BIENVENIDO " + " " * 10)

libros = []

def generar_id():
    return str(random.randint(100000, 999999))

while True:
    print("1. Registrar nuevo libro")
    print("2. Consultas y reportes")
    print("3. Salir")
    
    opcion = int(input("Seleccione el número de la acción que desea realizar: "))

    if opcion == 1:
        print('** REGISTRO DE NUEVO LIBRO **')
        titulo = input('Ingrese el nombre de la obra: ').upper()
        autor = input('Ingrese el autor de la obra: ').upper()
        genero = input('Ingrese el genero de la obra: ').upper()
        año_publicacion = input("Ingrese el año de publicacion: ")
        año_publicacion = datetime.datetime.strptime(año_publicacion,"%Y").date()
        isbn = input("Ingrese el ISBN de la obra: ")
        fecha_adquisicion = input("Ingrese la fecha de su evento (dd/mm/aaaa): ")
        fecha_adquisicion = datetime.datetime.strptime(fecha_adquisicion,"%d/%m/%Y").date()
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
            print('** CONSULTAS Y REPORTES****')
            print("1. Consultas")
            print("2. Reportes")
            print("3. Volver al menu principal")
            opcion_menu_consultas = int(input("Seleccione el número de la acción que desea realizar: "))

            if opcion_menu_consultas == 1:
                print('** CONSULTAS **')
                print("Buscar libro por:")
                print("1. Título")
                print("2. ISBN")
                print("3. Volver al menu anterior")
                opcion_submenu = int(input("Opción: "))

                if opcion_submenu == 1:
                    titulo_busqueda = input("Ingrese el título: ").upper()
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
                        break
                    else:
                        print("No se encontraron libros con ese título.")

                elif opcion_submenu == 2:
                    isbn_busqueda = input("Ingrese el ISBN: ")
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
                        break 
                    else:
                        print("No se encontraron libros con ese ISBN.")
                        
            elif opcion_menu_consultas == 2:
                print('** REPORTES **')
                print("1. Catalogo")
                print("2. Reporte por autor")
                print("3. Reporte por genero")
                print("4. Reporte por año de publicacion")
                print("5. Volver al menu anterior")
                opcion_reportes = int(input("Opción\n: "))
                        
                if opcion_reportes == 1:
                    catalogo = []
                    autores = set() 
                    generos = set()
                                
                    def consultar_catalogo():
                        if len(catalogo) == 0:
                            print("No hay libros registrados en el catálogo.")
                        else:
                            print("ID\tTÍTULO\t\t\tAUTOR\t\t\tGÉNERO\t\tAÑO\tISBN\t\tFECHA")
                            for libro in catalogo:
                                print(f"{libro['id']}\t{libro['titulo'][:20]}\t{libro['autor'][:20]}\t{libro['genero']}\t\t{libro['año']}\t{libro['isbn']}\t{libro['fecha']}")
                                break 
                
                elif opcion_reportes == 2:
                    autor_seleccionado = input("Ingrese el nombre del autor a consultar: ").upper()
                    if autor_seleccionado not in autores:
                        print(f"No se encontraron libros del autor '{autor_seleccionado}' en el catálogo.")
                    else:
                        print(f"Libros del autor '{autor_seleccionado}':")
                        print("ID\tTÍTULO\t\t\tAUTOR\t\t\tGÉNERO\t\tAÑO\tISBN\t\tFECHA")
                        for libro in catalogo:
                            if libro['autor'] == autor_seleccionado:
                                print(f"{libro['id']}\t{libro['titulo'][:20]}\t{libro['autor'][:20]}\t{libro['genero']}\t\t{libro['año']}\t{libro['isbn']}\t{libro['fecha']}")
                                break
                    
                elif opcion_reportes == 3:
                    def consultar_por_genero():
                        consultar_por_genero = input("Ingrese el género a consultar: ").upper()
                        if consultar_por_genero not in generos:
                            print(f"No se encontraron libros del género '{genero}' en el catálogo.")
                        else:
                            print(f"Libros del género '{consultar_por_genero}':")
                            print("ID\tTÍTULO\t\t\tAUTOR\t\t\tGÉNERO\t\tAÑO\tISBN\t\tFECHA")
                            for libro in catalogo:
                                if libro['genero'] == consultar_por_genero:
                                    print(f"{libro['id']}\t{libro['titulo'][:20]}\t{libro['autor'][:20]}\t{libro['genero']}\t\t{libro['año']}\t{libro['isbn']}\t{libro['fecha']}")
                                    break
                
                elif opcion_reportes == 4:
                    anio_seleccionado = input("Ingrese el año de publicación a consultar: ")
                    libros_encontrados = []
                    for libro in catalogo:
                        if libro["año"].year == int(anio_seleccionado):
                            libros_encontrados.append(libro)
                    if libros_encontrados:
                        for libro in libros_encontrados:
                            print("ID:", libro["id"])
                            print("Título:", libro["titulo"])
                            print("Autor:", libro["autor"])
                            print("Género:", libro["genero"])
                            print("Año de publicación:", libro["año"])
                            print("ISBN:", libro["isbn"])
                            print("Fecha de adquisición:", libro["fecha"])
                        break
                    else:
                        print("No se encontraron libros publicados en ese año.")
                        
                elif opcion_menu_consultas == 3:
                    break
                    
                else:
                    print("Regresando al Menu Principal.")
            
            elif opcion == 3:
                print("Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")
