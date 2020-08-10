
from CONTROLLER.controllers import Controller
from MODEL.models import Player


from testing import write_json

import json
corriendo = True
num = 0

#Instancia de controller

controlador = Controller()

#Instancia usuario

usuario = Player()


while corriendo :
        print("=============================================================")
        print("1)Ingresar credenciales como login")
        print("2)Generar un nuevo jugador por medio de registración")
        print("3)Ver los jugadores existentes") 
        print("0)Salir")
        print("=============================================================")
        num = input(" Ingrese el número asociado a la opción que necesita : ")        
        try:
                num = int(num)
                
                if num ==0:
                    break

                while num<0 or num>3:
                    print("Numero inválido")
                    num = input(" Ingrese un número de 1 a 3 dependiendo de la opcion que se necesite: ")  
                    num = int(num)

                    if num ==0:
                        break                   
                else:        
                    print("Opción seleccionada: ", num)

        except ValueError:
                    opcionInvalida = True
                    while opcionInvalida:
                        print("Error, el valor ingresado no es un número entero.")
                        try:
                            num = input(" Ingrese un número de 1 a 3 dependiendo de la opcion que se necesite: ")  
                            num = int(num)

                            if num ==0:
                                break

                            if num<0 or num>3:
                                print("Numero inválido")
                                num = input(" Ingrese un número de 1 a 3 dependiendo de la opcion que se necesite: ")  
                                num = int(num)

                                if num ==0:
                                    break

                            else:
                                opcionInvalida = False
                                print("Opción seleccionada: ", num)

                        except ValueError:
                            print("Error, lo sentimos, valor incorrecto.")
                                           
        if num == 1:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("La opción seleccionada fue : Ingresar credenciales como login ")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            userCorrect = False
            usuario._username = input('Ingrese su usuario : ') 
            userCorrect = controlador.validarUserLogin1('existing_users.json',usuario._username,userCorrect)


            if(userCorrect):
                passwrdCorrect = False
                usuario._password = input('Ingrese su contraseña : ')
                passwrdCorrect = controlador.validarPasswrdLogin1('existing_users.json',usuario._password,passwrdCorrect)

                if(userCorrect == True and passwrdCorrect == True):
                    print("=============================================================")
                    print("Sr(a) " + usuario._username + " ha iniciado sesión de forma satisfactoria en el sistema.")
                    print("=============================================================")
                        
        elif num == 2:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("La opción seleccionada fue : Generar un nuevo jugador por medio de registración")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            
            #usuario._username = input(" Ingrese su usuario :  ") 
            usuario._username = controlador.usernameValidReg(usuario._username,'existing_users.json')

            #Retorno el resultado del metodo verificador passwrdVa, para ver si es valido el password ingresado
            usuario._password = controlador.passwrdValid(usuario._password)

            usuario._icon = input("Ingrese su icono : ")
            
            #usuario._email = input("Ingrese su correo : ")
            usuario._email = controlador.emailValid(usuario._email)

            with open('existing_users.json') as json_file: 

                data = json.load(json_file) 
                
                temp = data['usuariosExistentes'] 
                
                # Objeto python para agregar al json 
                y = {"username":usuario._username, 
                    "password": usuario._password, 
                    "icono": usuario._icon,
                    "email": usuario._email
                    } 
                # appending data to emp_details  
                temp.append(y) 
            
            controlador.write_json(data) 


        elif num == 3:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("La opción seleccionada fue : Ver los jugadores existentes")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            controlador.load_all_users('existing_users.json')

            

