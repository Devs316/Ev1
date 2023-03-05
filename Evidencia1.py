print("*" *10 + " BIENVENIDO " + "*" *10)

while true:
    print("1. Registrar nuevo ejemplar")
    print("2. Consultas y reportes")
    print("3. Salir")
   
opción = int(input("Seleccione el número de la acción que desea realizar \n:"))

if opción == 1:
    print('******** REGISTRO PARA RESERVACION DE UNA SALA ********')
    nombre_evento = input('Ingrese el nombre de su evento: ')
    fecha_reservada = input("Ingrese la fecha de su evento  (dd/mm/aaaa): ")
fecha_reservada = datetime.datatime.striptime(fecha_reseevada,"%d/%m/%Y").date()

