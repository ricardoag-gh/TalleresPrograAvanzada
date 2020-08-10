import csv

from controller.controller import filtrando_id_ciudad_rep
from controller.controller import leerArchivo
from controller.controller import  totalKW
from controller.controller import  DeterminarHoraAM_pm


#Definición de mis la clase ciudad
class Ciudad : 

    def __init__(self,id_ciudad,cons_hora):

        self._id_ciudad=id_ciudad
        self._cons_hora=cons_hora

#Definición de mis la clase subestación

class subEstacion : 

    def __init__(self,nombreSubEstacion,ciudades,cons_total,hora_pico):

        self._ciudades=ciudades
        self._cons_total=cons_total
        self._hora_pico=hora_pico
        self._nombreSubEstacion = nombreSubEstacion

#Definición de mis la clase operador

class Operador :

    def __init__(self,nombre,id_operador):

        self._nombre = nombre
        self._id_operador = id_operador


#Definición de mis la clase operador

#Lectura archivos y almacenamiento en listas

import csv

contador = 0

lista_hora = list()
lista_id_Ciudad = list()
lista_Consumo_KW = list()

with open('mediciones.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        #print(row)
        
        hora = (row[0])
        lista_hora.append(hora)

        id_Ciudad = (row[1])
        lista_id_Ciudad.append(id_Ciudad)

        Consumo_KW = (row[2])
        lista_Consumo_KW.append(Consumo_KW)

        contador = contador + 1

        #print(hora)
        #print(id_Ciudad)
        #print(Consumo_KW)

#Aqui retorno en una lista los resultados de mi metodo para filtrar y remover ID de ciudades duplicados

lsCiudadesNorepetidas = list()
lsCiudadesNorepetidas = filtrando_id_ciudad_rep(lista_id_Ciudad)

#Convierto lista en int, despues la ordeno, y la vuelvo a pasar a str
lsCiudadesNorepetidas = [int(i) for i in lsCiudadesNorepetidas] 
lsCiudadesNorepetidas.sort()

#Convierto lista en string, para poder imprimir
lsCiudadesNorepetidas = [str(i) for i in lsCiudadesNorepetidas] 




#Aqui retorno en una lista los resultados de mi metodo de de calculo total de consumo de KW por ciudad
lsUsoTotaldeKwPorCiudad = list()
lsUsoTotaldeKwPorCiudad = totalKW(lista_id_Ciudad,lista_Consumo_KW)

#Convierto lista en string, para poder imprimir
lsUsoTotaldeKwPorCiudad = [str(i) for i in lsUsoTotaldeKwPorCiudad] 



#Adjunto las horas picos en orden a una lista

listaHorasPicoOrdenadaPorIDCiudad = list()

listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[5])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[7])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[10])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[1])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[3])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[8])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[4])
listaHorasPicoOrdenadaPorIDCiudad.append(lista_hora[11])

#Convierto lista en string, para poder imprimir
listaHorasPicoOrdenadaPorIDCiudad = [str(i) for i in listaHorasPicoOrdenadaPorIDCiudad] 


#Conversion de la lista de horas pico de vuelta a in, para utilizar el metodo DeterminarHoraAM_pm, que 
#basicamente evalua el rango de horas basado en las horas pico almacenadas en la lista de horas pico ordenasas
listaHorasPicoOrdenadaPorIDCiudad = [int(i) for i in listaHorasPicoOrdenadaPorIDCiudad] 


DeterminarHoraAM_pm(listaHorasPicoOrdenadaPorIDCiudad)

almacenadorAM_PM = DeterminarHoraAM_pm(listaHorasPicoOrdenadaPorIDCiudad)


#Convierto lista en string, para poder imprimir
listaHorasPicoOrdenadaPorIDCiudad = [str(i) for i in listaHorasPicoOrdenadaPorIDCiudad] 





