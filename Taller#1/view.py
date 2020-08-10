
#Importacion de mi metodo del archivo controller.py

from controller import datacionPotArg1
from controller import validacionCantPotasio
from controller import eraRoca

from model import PiedrasAntiguas



instanciaModel = PiedrasAntiguas(cantPotasio=0,cantArgon=0,edadRoca=0,eraGeo=0,cantidadMuestras=0,cantidadMasa=0)


#Variables temporales 

#pulltest

contador = 0

#VISTA

#Impresion de los datos

print("Bienvenido a la Escuela de Geología de CentroAmérica")

print("Para analizar la edad aproximada de la roca por favor ingrese lo siguiente : ")


#Validando que se ingrese un numero entero como cantidad de muestras
while True:
    num = instanciaModel.cantidadMuestras = input("Ingrese la cantidad de muestras a analizar : ")  

    

    try:
        val = int(num)
        print("La cantidad ingresada de muestras a analizar es :")
        print("Valor: ", val)
        break;
   
    except ValueError:
        print("Error, el valor ingresado no es un número entero.")



listaAlmacenMasa = []
#Este es mi bucle para guardar la informacion de masa.
indiceContador = 0
while indiceContador < int(instanciaModel.cantidadMuestras):

            indiceContador = indiceContador + 1
    #Validacion en el front end de la cantidad de masa ingresada


            while True:
                num = instanciaModel.cantidadMasa = input("Ingrese la cantidad aproximada de masa de la roca  " + str(indiceContador) + " : ")
                try:
                    val = int(num)
                    print("La cantidad ingresada de masa es un valor entero.")
                    print("Valor: ", val)
                    listaAlmacenMasa.append(val)
                    break;
                except ValueError:
                    try:
                        val = float(num)
                        print("La cantidad de masa ingresada es un número flotante")
                        print("Valor: ", val)
                        listaAlmacenMasa.append(val)
                        break;
                    except ValueError:
                        print("Error, el valor ingresado es una cadena de texto. Por favor ingrese un número.")

          
#print(listaAlmacenMasa)


listaAlmacenCanPot = []
#Este es mi bucle para guardar la informacion de cantidad de Potasio.
indiceContador1 = 0
while indiceContador1 < int(instanciaModel.cantidadMuestras):

            indiceContador1 = indiceContador1 + 1


            #Validacion en el front end de la cantidad de potasio ingresada
            while True:
                num = instanciaModel.cantPotasio = input("Ingrese la cantidad aproximada de potasio de la roca : " + str(indiceContador1) + " : ")
                try:
                    val = int(num)
                    print("La cantidad ingresada de potasio es un valor entero.")
                    print("Valor: ", val)
                    listaAlmacenCanPot.append(val)
                    break;
                except ValueError:
                    try:
                        val = float(num)
                        print("La cantidad de potasio ingresada es un número flotante")
                        print("Valor: ", val)
                        listaAlmacenCanPot.append(val)
                        break;
                    except ValueError:
                        print("Error, el valor ingresado es una cadena de texto. Por favor ingrese un número.")



#print(listaAlmacenCanPot)


listaAlmacenCanArg = []
#Este es mi bucle para guardar la informacion de cantidad de Argon.
indiceContador2 = 0
while indiceContador2 < int(instanciaModel.cantidadMuestras):

            indiceContador2 = indiceContador2 + 1


#Validacion en el front end de la cantidad de  argon ingresada

            while True:
                num = instanciaModel.cantArgon = input("Ingrese la cantidad aproximada de argón de la roca : " + str(indiceContador2) + " : ")
                try:
                    val = int(num)
                    print("La cantidad ingresada de argón es un valor entero.")
                    print("Valor: ", val)
                    listaAlmacenCanArg.append(val)
                    break;
                except ValueError:
                    try:
                        val = float(num)
                        print("La cantidad de argón ingresada es un número flotante")
                        print("Valor: ", val)
                        listaAlmacenCanArg.append(val)
                        break;
                    except ValueError:
                        print("Error, el valor ingresado es una cadena de texto. Por favor ingrese un número.")


# print(listaAlmacenCanArg)


#Esta es la formula usada para el calculo de edad de las rocas.

#instanciaModel.edadRoca = (datacionPotArg1(float(instanciaModel.cantPotasio),float(instanciaModel.cantArgon)))

#instanciaModel.eraGeo = (eraRoca(int(instanciaModel.edadRoca)))


########################

listaAlmacenEdadCalculada = []
listaAlmacenEraCalculada = []
#Este es mi bucle para guardar el calculo de la edad utilizando las listas de cantArgon y cantPotasio, ademas en este bucle se almacena la era
#segun la edad

indiceContador3 = 0
while indiceContador3 < int(instanciaModel.cantidadMuestras):

            
            #Este de abajo es el metodo usado para calculo de edad.
            instanciaModel.edadRoca = (datacionPotArg1(float(listaAlmacenCanPot[indiceContador3]),float(listaAlmacenCanArg[indiceContador3])))

            listaAlmacenEdadCalculada.append(instanciaModel.edadRoca)

            
            #Este de abajo es el metodo usado para definicion de era.
            instanciaModel.eraGeo = (eraRoca(int(listaAlmacenEdadCalculada[indiceContador3])))
            listaAlmacenEraCalculada.append(instanciaModel.eraGeo)
            

            indiceContador3 = indiceContador3 + 1

            #instanciaModel.eraGeo = (eraRoca(int(instanciaModel.edadRoca)))


#######################


#Este es mi bucle para impresion
indiceContador4 = 0
while indiceContador4 < int(instanciaModel.cantidadMuestras):

            

            print("-----------------Imprimiendo resultados de la roca : " + str(indiceContador4 + 1) + " : ")
            

            print("Número de muestra : " + str(indiceContador4 + 1))
            print("Peso en KG : " + str(listaAlmacenMasa[indiceContador4]))
            print("Cantidad de potasio en mg : " + str(listaAlmacenCanPot[indiceContador4]))
            print("Cantidad de árgon en mg : " + str(listaAlmacenCanArg[indiceContador4]))
            print("Edad aproximada de la piedra : " + str(listaAlmacenEdadCalculada[indiceContador4]))
            print("Era de la piedra : " )  #check
            #Probando impresion eras
            instanciaModel.eraGeo = (eraRoca(int(listaAlmacenEdadCalculada[indiceContador4])))
            


            indiceContador4 = indiceContador4 + 1
            
            #validando







