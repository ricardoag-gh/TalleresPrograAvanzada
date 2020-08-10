import csv

import sqlite3 as dba_object 
from sqlite3 import Error


#La idea de este metodo era poder leer el archivo, y pasarle como parametros las listas, pero no es funcional aun. 

def leerArchivo(archivoALeer, lista_hora,lista_id_Ciudad,lista_Consumo_KW):

    contador = 0

    lista_hora = list()
    lista_id_Ciudad = list()
    lista_Consumo_KW = list()

    with open(archivoALeer) as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
            
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

        return lista_hora,lista_id_Ciudad,lista_Consumo_KW #Lastimosamente los return se despliegan vacios en el view. 



#Metodo que sirve para sacar los IDs repetidos de las ciudades

def filtrando_id_ciudad_rep(lista_id_Ciudad):

            myset = set(lista_id_Ciudad) 

            lista_id_Ciudad_valUnicos = list(myset) #Almaceno los resultados unicos retornados por el set

            
            return lista_id_Ciudad_valUnicos 



#Metodo suma total de KW por ciudad

def totalKW(lista_id_Ciudad, lista_Consumo_KW):

    contador=0
    usoTotalKWCiudad1=0
    usoTotalKWCiudad2=0
    usoTotalKWCiudad3=0
    usoTotalKWCiudad4=0
    usoTotalKWCiudad5=0
    usoTotalKWCiudad6=0
    usoTotalKWCiudad8=0
    usoTotalKWCiudad13=0


    #Serie de listas que utilizo para guardar el consumo total por ciudad
    lista_ConsumoTotalxCiudad_KW1 = list()
    lista_ConsumoTotalxCiudad_KW2 = list()
    lista_ConsumoTotalxCiudad_KW3 = list()
    lista_ConsumoTotalxCiudad_KW4 = list()
    lista_ConsumoTotalxCiudad_KW5 = list()
    lista_ConsumoTotalxCiudad_KW6 = list()
    lista_ConsumoTotalxCiudad_KW8 = list()
    lista_ConsumoTotalxCiudad_KW13 = list()
    lista_ConsumoTotalxCiudad_Todas = list()


    lista_horaPico = list()


    for object in lista_id_Ciudad:
        
        if lista_id_Ciudad[contador]=='1':
            
            usoTotalKWCiudad1 = usoTotalKWCiudad1 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW1.append(usoTotalKWCiudad1)
            
            #Test

        elif lista_id_Ciudad[contador]=='2':
            
            usoTotalKWCiudad2 = usoTotalKWCiudad2 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW2.append(usoTotalKWCiudad2)
            

        elif lista_id_Ciudad[contador]=='3':
            
            usoTotalKWCiudad3 = usoTotalKWCiudad3 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW3.append(usoTotalKWCiudad3)
            

        elif lista_id_Ciudad[contador]=='4':
            
            usoTotalKWCiudad4 = usoTotalKWCiudad4 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW4.append(usoTotalKWCiudad4)
            

            
        elif lista_id_Ciudad[contador]=='5':
            
            usoTotalKWCiudad5 = usoTotalKWCiudad5 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW5.append(usoTotalKWCiudad5)
            

        elif lista_id_Ciudad[contador]=='6':
            
            usoTotalKWCiudad6 = usoTotalKWCiudad6 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW6.append(usoTotalKWCiudad6)
            

        elif lista_id_Ciudad[contador]=='8':
            
            usoTotalKWCiudad8 = usoTotalKWCiudad8 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW8.append(usoTotalKWCiudad8)
            

        elif lista_id_Ciudad[contador]=='13':
            
            usoTotalKWCiudad13 = usoTotalKWCiudad13 + float(lista_Consumo_KW[contador])
            lista_ConsumoTotalxCiudad_KW13.append(usoTotalKWCiudad13)
                                              
        
        contador = contador + 1   
    
    #Agregando los valores totales a las listas 1, para aquellas que tenian dos valores, 0 para las de un solo valor
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW1[1])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW2[0])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW3[1])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW4[1])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW5[0])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW6[1])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW8[0])
    lista_ConsumoTotalxCiudad_Todas.append(lista_ConsumoTotalxCiudad_KW13[0])


    return lista_ConsumoTotalxCiudad_Todas


# El siguiente metodo permite definir si la hora es AM o PM. Aun queda por evaluar la opcion de la hora doce, 
#ya que depende el formato de hora puede ser 12 MD or 12 MN

def DeterminarHoraAM_pm(listaHorasPicoPorciudad):
    contador=0
    Hora = " "  
    listaAlmacenadorAM_PM = list()  

    for object in listaHorasPicoPorciudad:

        if listaHorasPicoPorciudad[contador]>=13: 
            #Hora = "PM"
            listaAlmacenadorAM_PM.append("PM")
            
                        
        elif listaHorasPicoPorciudad[contador]<13:
            #Hora = "AM"
            listaAlmacenadorAM_PM.append("AM")
            
        contador = contador+1

    return listaAlmacenadorAM_PM #Almaceno los resultados de la validacion y los devuelvo en una lista



   #Validacion base de datos, para validar si existen entradas en la base de datos


#Testing base de datos 

class baseDeDatos:


    def validacionBaseDeDatos(self):  
        
        Conn = self.sqlite_create_database()     
        almacenador = self.obtener_Rows(Conn) #Validacion de si hay informacion la tabla

        if almacenador:    
            if almacenador:
                for Item in almacenador:
                    almacenador = self.obtener_Rows(Conn) # De no estar vacia, se alamcena el la informacion en el almacenador
                    return almacenador
            else:
                return almacenador
        else:                                   #En caso de no haber entradas en la tabla se crea la misma. Y se retornal el almacenador. 
            self.create_table(Conn)
            almacenador = self.obtener_Rows(Conn)
            return almacenador



    def __init__(self):
        pass

    def sqlite_create_database(self): #Metodo utilizado para crear la base de datos
        try:
            conexion = dba_object.connect("mi_primera_base_datos.db")
            return conexion
        except Error as Error:
            print("Error : ", Error)


    def create_table(self,connection): #Creacion de mi tabla operador, con identity
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE TablaOperario(_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
            connection.commit()
        except Error:
            print("Posible error en creacion de tabla : ",Error)  


    def insertar_new_row(self,connection, valores): #Realizo la insercion de un row a mi base de datos
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO TablaOperario(nombre) VALUES(?)", valores)
            connection.commit()
        except Error:
            print(Error, "Puede ser un error al insertar un dato en una fila.") 


    def obtener_Rows(self, connection): #Metodo para obtener los rows de mi tabla
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM TablaOperario")
            res_Seleccion = cursor.fetchall()
            connection.commit()
            return res_Seleccion

        except Error:
            print(Error, "Puede ser un error al obtener los rows.  ") 


    
 