#Esteban Montenegro, Felix Vargas
# 21.177.769-9
# 21.146.143-8

import matplotlib.pyplot as plt
import numpy
import time

dict_1={"1":"TarapacÃ¡","2":"Antofagasta","3":"Atacama","4":"Coquimbo","5":"ValparaÃ­ so","13":"Metropolitana","6":"Oâ€™Higgins","7":"Maule","14":"Los RÃ o","10":"Los lagos","11":"AysÃ©n ","12":"Magallanes","16":"Ã‘uble"}

#Esta funcion lee los datos de los archivos de texto y los cambia por los datos del diccionario

archive = open("vacunacion_region.csv","r")
def lineas(valor): 
    x = archive.readlines()
    region = valor
    for i in (x):
        i = i.split(",")
        if i[0]== region:
            listr.append(i)

#Esta funcion sirve para graficar los datos pedidos en la funcion anterior,
#Funciona con dos sublistas de la lista que obtuvimos de la funcion anterior.
#Al final se hacen .pop para eliminar los nombres del inicio de la lista.

def listas_grafico():
    k= archive.readline()
    list(k)
    k=k.split(",") 
    first = listr[0]
    second = listr[1]
    k.pop(0)
    k.pop(0)
    first.pop(0)
    first.pop(0)
    second.pop(0)
    second.pop(0)


#Las siguientes lineas de  codigo son para convertir cada 
# elemento de la lista, de string a integer

    results = first
    first_int = [int(i) for i in results]

    results = second
    second_int = [int(i) for i in results]

# "ax" se definen como las subfunciones del grafico
# Lo de mas abajo en el grafico es para embellecer solamente. 

    fig, subplts= plt.subplots()
    plt.title("Graficas de Primera y segunda dosis") 
    plt.xticks(rotation = 90)
    plt.plot(k,first_int,color="b",label="Primera dosis")
    plt.legend() 
    subplts.set_ylabel("Personas vacunadas") 
    plt.plot(k,second_int,color="g",label="Segunda dosis")
    plt.legend()  
    subplts.set_xlabel("Fechas")
    subplts.grid(linestyle = "dashed")
    plt.show()

#Continuando por abajo, aqui empieza el 
#menu de opciones, donde el usuario puede elegir
#lo que quiere hacer con el programa.

print("Gracias por usar nuestro programa, Seleccione una opción para usar nuestro programa")
op = input("1-Informacion de vacunacion por regiones individuales.\n2-Toda la Información\n3-Comparación de entre 2 regiones.\n")

while not op.isnumeric():
    op = input("Ingrese un valor valido:")

while int(op) <=0 or int(op) >3:
    op = input("Ingrese un valor valido:")

#Este if es una de las tres opciones del menu
#
if op=="1":
    print("regiones a seleccionar:\n15-Arica y parinacota\n1-Tarapaca\n2-Antofagasta\n3-Atacama\n4-Coquimbo\n5-Valparaiso\n13-Metropolitana\n6-Bernardo Ohiggins\n7-Maule\n16-Ñuble\n8-Bío bío\n9-Araucania\n14-Los rios\n10-Los lagos\n11-Aysen\n12-Magallanes")
    print("seleccione las regiones en las cuales quiere hacer las comparaciones")
    
    data_region = input()    #Aqui el usuario debe elegir la region de la cual quiere recibir informacion.
    
    while not data_region.isnumeric():
        data_region = input("Ingrese un valor valido: \n")
    
    while int(data_region) <=0 or int(data_region) >16:
        data_region = input("Ingrese un valor valido: \n")

#En estas lineas de codigo es donde se llaman a las funciones de mas 
#arriba segun la opcion elegida por el usuario
    t_nr = (dict_1[data_region])
    listr = []
    lineas(t_nr)
    listas_grafico()
      
#Esta es la segunda de las tres opciones del menu
elif  op=="2":
    print("Aqui se muestran graficas según la gente que se vacuna y la que no: \n")
   
    l1 = archive.readline()
    list(l1)
    l1 = l1.split(",")
    l1.pop(0)
    l1.pop(0)
    l2 = archive.readline()
    list(l2)
    l2 = l2.split(",")
    l2.pop(0)
    l2.pop(0)
    l3 = archive.readline()
    list(l3)
    l3 = l3.split(",")
    l3.pop(0)
    l3.pop(0)
    re2 = l2
    first_int = [int(i) for i in re2]
    re2 = l3
    second_int = [int(i) for i in re2]

    print (2320697-55028,"Personas no se vacunaron el ultimo tiempo")
    fig, subplts= plt.subplots()
    plt.title("Grafico Vacunados")
    plt.xticks(rotation = 90)
    plt.yticks([0,200000,400000,600000,800000,1000000,1200000,1400000,1600000,1800000,2000000,2200000,2400000])
    plt.plot(l1,first_int,color="b",label="Primera dosis")
    plt.legend()
    subplts.set_ylabel("Cantidad de personas en millones")
    plt.plot(l1,second_int,color="g",label="Segunda dosis")
    plt.legend() 
    subplts.set_xlabel("Fechas")
    subplts.grid(linestyle = "dashed")
    plt.show()


#Esta es la ultima opcion de las 3 que se basa
#en una comparativa de vacunacion entre 
#dos regiones de Chile   
elif op == "3":
    listr=[]
    print("Aqui puede comparar dos regiones de Chile:")
    print("Seleccione dos regiones de Chile separadas por un ',': ")
    comp= input()
    comp = comp.split(",")
    l1=comp[0]
    l2=comp[1]
    first_region=(dict_1[l1])
    second_region=(dict_1[l2])
    lineas(first_region)
    archive = open("vacunacion_region.csv","r")
    ftl1= archive.readline()
    list(ftl1)
    ftl1=ftl1.split(",") 
    first_d = listr[0]
    second_d = listr[1]
    ftl1.pop(0)
    ftl1.pop(0)
    first_d.pop(0)
    first_d.pop(0)
    second_d.pop(0)
    second_d.pop(0)

    r1 = first_d
    first_int1 = [int(i) for i in r1]
    r1 = second_d
    second_int1 = [int(i) for i in r1]

    listr = []
    lineas(second_region)                 
    archive = open("vacunacion_region.csv","r")
    flt2= archive.readline()
    list(flt2)
    flt2=flt2.split(",") 
    first_d1 = listr[0]
    second_d2 = listr[1]
    flt2.pop(0)
    flt2.pop(0)
    first_d1.pop(0)
    first_d1.pop(0)
    second_d2.pop(0)
    second_d2.pop(0)

    r2 = first_d1
    first_int2 = [int(i) for i in r2]
    r2 = second_d2
    second_int2 = [int(i) for i in r2]

#Aqui se grafica la parte 3 de todo el codigo para mostrar la comparativa entre dos regiones
    
    fig, subplts = plt.subplots(2,2,sharey = True)
    subplts[0,0].set_ylabel("Primera dosis de primera region")
    subplts[0,1].set_ylabel("Segunda dosis de primera region")
    subplts[1,0].set_ylabel("Primera dosis de segunda region")
    subplts[1,1].set_ylabel("Segunda dosis de segunda region")
    subplts[0,0].set_xlabel("Fechas")
    subplts[0,1].set_xlabel("Fechas")
    subplts[1,0].set_xlabel("Fechas")
    subplts[1,1].set_xlabel("Fechas")
    subplts[0,0].plot(ftl1,first_int1,color = "b")
    subplts[0,1].plot(ftl1.float16,second_int1,color = "b")
    subplts[1,0].plot(flt2,first_int2,color = "g")
    subplts[1,1].plot(flt2,second_int2,color = "g")
    plt.show()