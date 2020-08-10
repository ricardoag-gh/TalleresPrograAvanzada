import math




#Metodo para el calculo de edad aproximadas :

def datacionPotArg1(cantKf,cantAr):

            vidaMediaPotasio = 1.248 * (pow(10,9))

            Datacionresultado = (vidaMediaPotasio / math.log(2))*math.log((cantKf+(cantAr/0.109))/cantKf)

            return Datacionresultado




#Testing metodo validar potasio

def validacionCantPotasio(cantKf,correctVal):

    
            while True:
                correctVal
                num = cantKf
                try:
                    val = int(num)
                    correctVal = True
                    mensaje = print("La cantidad ingresada de potasio es un valor entero." + " Valor: ", str(val))           
                    break;
                except ValueError:
                    try:
                        val = float(num)
                        correctVal = True
                        mensaje =print("La cantidad de potasio ingresada es un número flotante."  + " Valor: ", str(val))                  
                        break;
                    except ValueError:
                        correctVal = False
                        mensaje =print("Error, el valor ingresado es una cadena de texto. Por favor ingrese un número.")
    
                break

def eraRoca (edadRoca):

    if (edadRoca>=542000000):

        mensaje = print("Pre-paleozoica")

    elif (edadRoca < 542000000 and edadRoca >= 251000000):

        mensaje = print("Paleozoica")

    elif(edadRoca < 251000000 and edadRoca >= 65500000):

        mensaje = print("Mesozoica")

    elif(edadRoca < 65500000):
        mensaje = print("Cenozoica")


        return mensaje


        #Actualizando comentarios