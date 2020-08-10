
from model.model import Operador
from model.model import subEstacion

#Import listas

from model.model import lista_hora
from model.model import lista_id_Ciudad
from model.model import lista_Consumo_KW
from model.model import listaHorasPicoOrdenadaPorIDCiudad

from model.model import lsCiudadesNorepetidas
from model.model import lsUsoTotaldeKwPorCiudad
from model.model import almacenadorAM_PM

from controller.controller import baseDeDatos

#Testing

instanciaBD = baseDeDatos()

valorBase = instanciaBD.validacionBaseDeDatos()


if valorBase:

    print("Hola Sr(a): ", str(valorBase) + ", parece ser que usted ya es cliente nuestro.")

    #Validando que se ingrese un nombre de subestacion valido
    valor = True
    NuevaSubEstacion = subEstacion
    while valor==True:
        print("-----------------------------------------------------")
        subEstacion.nombreSubEstacion = input("Subestación: ") 
        print("-----------------------------------------------------") 
    
        if not subEstacion.nombreSubEstacion.strip():
            print("-----------------------------------------------------")
            print("Nombre de subestación vacío o inválido.")
            print("-----------------------------------------------------")
        

        else:
            print("-----------------------------------------------------")
            print("El nombre de subestación ingresado es  es : " + subEstacion.nombreSubEstacion)
            print("-----------------------------------------------------")
            valor = False

    print("-----------------------------------------------------")
    print("+ Reporte de operador : " + str(valorBase))
    print("+ Subestación: " + subEstacion.nombreSubEstacion)

    print("-----------------------------------------------------")
    print("+ Nota : Las horas pico son determinadas en el formato de hora de 24 horas.")
    print("-----------------------------------------------------")
    contador = 0

    for object in lsUsoTotaldeKwPorCiudad: # Este for se utiliza para la impresion de todas las listas de datos como por medio de un contador
                                            

        print("Ciudad : " + lsCiudadesNorepetidas[contador] + ", Total consumo : " + lsUsoTotaldeKwPorCiudad[contador] + " KW." + 
        " Hora pico : " + listaHorasPicoOrdenadaPorIDCiudad[contador]+ " " + almacenadorAM_PM [contador])

        contador = contador+1
    print("-----------------------------------------------------")

else:
    print("-----------------------------------------------------")
    print("Atención : Si esta viendo este mensaje debe registrarse para el uso de esta plataforma.")
    print("-----------------------------------------------------")
    print("Ingrese la siguiente información para su registro : ")
    print("-----------------------------------------------------")



    #Validando que se ingrese un nombre de usuario valido 
    valor = True
    instanciaOperador = Operador
    while valor==True:
        print("-----------------------------------------------------")
        instanciaOperador.nombre = input("Nombre: ")
        print("-----------------------------------------------------")  
        
        if not instanciaOperador.nombre.strip():# Metodo que valida que no este vacio el input
            print("-----------------------------------------------------")
            print("Nombre de operador vacío o inválido.")
            print("-----------------------------------------------------")

        else:
            print("-----------------------------------------------------")
            print("El nombre de operador ingresado es  es : " + instanciaOperador.nombre)
            print("-----------------------------------------------------")
            valor = False


    Conex = instanciaBD.sqlite_create_database()
    
    #Lista temporal para nombre operador
    tempListNombreOpera = list()
    tempListNombreOpera.append(instanciaOperador.nombre)
    # #Lista temporal para nombre operador
    instanciaBD.insertar_new_row(Conex,tempListNombreOpera)


    #Validando que se ingrese un nombre de subestacion valido
    valor = True
    NuevaSubEstacion = subEstacion
    while valor==True:
        print("-----------------------------------------------------")
        subEstacion.nombreSubEstacion = input("Subestación: ") 
        print("-----------------------------------------------------") 
    
        if not subEstacion.nombreSubEstacion.strip():
            print("-----------------------------------------------------")
            print("Nombre de subestación vacío o inválido.")
            print("-----------------------------------------------------")
        

        else:
            print("-----------------------------------------------------")
            print("El nombre de subestación ingresado es  es : " + subEstacion.nombreSubEstacion)
            print("-----------------------------------------------------")
            valor = False

    print("-----------------------------------------------------")
    print("+ Reporte de operador : " + instanciaOperador.nombre)
    print("+ Subestación: " + subEstacion.nombreSubEstacion)

    print("-----------------------------------------------------")
    print("+ Nota : Las horas pico son determinadas en el formato de hora de 24 horas.")
    print("-----------------------------------------------------")
    contador = 0

    for object in lsUsoTotaldeKwPorCiudad:

        print("Ciudad : " + lsCiudadesNorepetidas[contador] + ", Total consumo : " + lsUsoTotaldeKwPorCiudad[contador] + " KW." + 
        " Hora pico : " + listaHorasPicoOrdenadaPorIDCiudad[contador]+ " " + almacenadorAM_PM [contador])

        contador = contador+1
    print("-----------------------------------------------------")









