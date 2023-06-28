import funciones as fn

while True:
    fn.mostrar_menu()
    opcion= fn.validar_opcion()
    if opcion == 1:
        rut= fn.validar_rut()
        nombre= fn.validar_nombre()
        nombre_mascota= fn.validar_nombre_mascota()
        cantidad_dias= fn.cantidad_dias()
        piso = fn.validar_piso()
        habitacion = fn.validar_habitacion()


    elif opcion == 2:
        pass
    elif opcion == 3:
        rut= fn.validar_rut()
        total_pagar= fn.total_pagar()

    else:
        break