import random, csv

trabajos=[]
sueldos=[]

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez",
                "Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez",
                "Francisco Díaz","Elena Fernández"]

def opcion_1():
    for x in range(10):
        sueldo1=random.randint(300000,2500000)
        print(sueldo1)
        sueldos.append(sueldo1)

        trabajo=[trabajadores + sueldos]



    

def opcion_2():
   pass



def opcion_3():
    geometrica=0
    medida=0
    for x in sueldos:
        if sueldos < sueldos[x]:
            print("el suelo mas bajo es "[x])
    for x in sueldos:
        if sueldos > sueldos[x]:
            print(f"el sueldo mas alto es" [sueldos])
    medida= (sueldos[0]+sueldos[1]+sueldos[2]+sueldos[3]+sueldos[4]+sueldos[5]+sueldos[6]+sueldos[7]+sueldos[8]+sueldos[9]+sueldos[10])/10
    print(f"el promedio de los sueldos es: " [medida])
    geaometrica=(sueldos[0]*sueldos[1]*sueldos[2]*sueldos[3]*sueldos[4]*sueldos[5]*sueldos[6]*sueldos[7]*sueldos[8]*sueldos[9]*sueldos[10])**1/10
    print(f"la media geometrica es: " [geometrica])
    


def opcion_4():

    with open("detalles_negocios.csv", "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow()

def opcion_5():
    print("finalizando prigrama...")
    print("desarrollado por Benjamin Valdebenito")
    print("Rut 21.971.513-7")