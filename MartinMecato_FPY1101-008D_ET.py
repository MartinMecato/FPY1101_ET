import csv
import os
import time
import random

trabajadores = ['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura hernandez','Muiguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernadez'] 

def limpieza_python():
    os.system("cls")

def tiempo_espera():
    time.sleep(2)

# asigno valres aleatorios (opcion 1 completo)
def asignar_sueldos_aleatorios():
    trabajadores1=[]
    for laqboratorio in trabajadores:
        precio= random.randint(300000,2500000)
        trabajadores1.append(laqboratorio,precio)
    return trabajadores1

# opcion 2

def clasificar_sueldos(trabajadores1):
    sueldosMenor800=[]
    sueldoen800y2000=[]
    sueldomayor2000=[]
    for linea in trabajadores1:
        if linea < 800000:
            linea.append(sueldosMenor800)
        if linea < 800000 and linea > 2000000:
            linea.append(sueldoen800y2000)
        if linea > 2000000:
            linea.append(sueldomayor2000)
    
    print(f"      Sueldos menores a $800.000       \n{sueldosMenor800}\n\n      Sueldos entre $800.000 y 2.000.000      \n{sueldoen800y2000}\n\n      Sueldo Superiores a $2.000.000      \n{sueldomayor2000}")




# opcion 4
def registrar_sueldos():
    nombre=input("coloque el nombre de un trabajador: ")
    sueldo=int(input("escrba el sueldo bruto del trabajador: "))
    dest_salud= (sueldo * 0.07)
    dest_afp= (sueldo * 0.12)
    suel_liquid=(sueldo - (dest_afp + dest_salud))

    return nombre,sueldo,dest_salud,dest_afp,suel_liquid

def crear_archivo_csv(nombre,sueldo,dest_salud,dest_afp,suel_liquid,archivo_csv='archivo_csv_t'):
    with open(archivo_csv,'a', newline='')as archivo:
        campos= ['Nombre Empleado','Sueldo Base','Descuento salud','Descuento AFP','Sueldo Liquido']
        archivo = csv.DictWriter(campos)
        archivo = csv.DictWriter({
            'Nombre Empleado': nombre,
            'Sueldo Base': sueldo,
            'Descuento salud': dest_salud,
            'Descuento AFP': dest_afp,
            'Sueldo Liquido': suel_liquid
            }) 
        
def leer_archivo(archivo_csv):
    with open(archivo_csv, 'r', newline='')as archivo:
        archivo=csv.DictReader
        for line in archivo:
            print(line)

# opcion salir
def salir_por_favo():
    print("Finalizando programa… Desarrollado por Martin Mecato RUT 21.548.960-4")

def opciones_del_menu():
    while True:
        try:
            gg=int(input("Escriba la opcion ----> "))
            if gg==1:
                limpieza_python()
                asignar_sueldos_aleatorios()
            if gg==2:
                limpieza_python()
                clasificar_sueldos()
            if gg==3:
                limpieza_python()
                print("")
            if gg==4:
                limpieza_python()
                nombre,sueldo,dest_salud,dest_afp,suel_liquid = registrar_sueldos()
                crear_archivo_csv(nombre,sueldo,dest_salud,dest_afp,suel_liquid)
                leer_archivo
            if gg==5:
                limpieza_python()
                salir_por_favo()
                break
            else:
                print("Eligiste mal el numero")
        except ValueError:
            print("pusiste una letra, te equivocaste")


def menu():
    limpieza_python()
    tiempo_espera()
    print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas.\n4.	Reporte de sueldos\n5.	Salir del programa")
    opciones_del_menu()

menu()