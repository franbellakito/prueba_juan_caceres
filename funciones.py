import numpy
import msvcrt
import os




listas_nombres= []
listas_ruts= []
listas_nombre_mascota= []
listas_cantidad_dias =[]
acumulador = 0
valor_dia =15000
lista_habitaciones= []
listas_filas= []




def mostrar_menu():
    os.system('cls')
    print("""  Mascota segura
    1.grabar
    2.buscar
    3.retirarse
    4.salir 
    """)

def validar_opcion():
    while True:
        try: 
            opc= int(input("ingrese una opcion: "))
            if opc in (1,2,3,4):
                return opc
            else:
                print("ERROR DEBE INGRESAR UNA OPCION CORRECTA")    

        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO")

def validar_rut():

    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
        listas_ruts.append(rut)
def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
        listas_nombres.append(nombre)
def validar_nombre_mascota():
    while True:
        nombre_m = input("Ingrese su nombre de su mascota: ")
        if len(nombre_m.strip()) >= 3 and nombre_m.isalpha() and not nombre_m.isspace():
            return nombre_m
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
        listas_nombre_mascota.append(nombre_m)
def cantidad_dias():
    cantidad_dias= 0
    while True:
        try:
            c_dias= int(input("ingrese cantidad de dias que se quedara su mascota: "))
            if c_dias >= 1:
                print(F"SU MASCOTA SE AH REGISTRADO POR: {c_dias},dias")
                return c_dias
            else:
                print("ERROR DEBE REGISTRARSE AL MENOS UN DIA")

        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO: ") 
        listas_cantidad_dias(c_dias)
        cantidad_dias= cantidad_dias+ 1

habitaciones= numpy.zeros((2,5))

def validar_piso():
    while True:
        try:
            fila = int(input(f"Ingrese el piso que se desea quedar su mascota (1,2):"))
            if fila >= 1 and fila <= 2:
                return fila
            else:
                print("ERROR! EL PISO NO EXISTE")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
        listas_filas(fila)       
def validar_habitacion():
    while True:
        try:
            columna = int(input(f"Ingrese número de la habitacion que se desea quedar su mascota ({min},{max}):"))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("ERROR! HABITACION NO EXISTENTE ")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
        lista_habitaciones(columna)









def total_pagar():
    if validar_rut in listas_ruts:
        total_pagar= cantidad_dias*valor_dia

