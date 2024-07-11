
from f_examen import *
import os, time

while True:
    os.system("cls")
    print("\ndatos de trabajadores")
    print("1.asignar sueldo aleatorio")
    print("2.clasificar sueldo")
    print("3.ver estadisticas")
    print("4. Reporte de sueldo")
    print("5. salir del programa")
    opt = int(input("ingrese una opcion: "))
    os.system("cls")
    if opt == 1:
        opcion_1()
    elif opt == 2:
        opcion_2()
    elif opt == 3:
        opcion_3()
    elif opt == 4:
        opcion_4()
    elif opt == 5:
        opcion_5()
    time.sleep(5)

