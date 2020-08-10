from MODEL.models import Player
import json

import unittest, json, os


class Controller:
# en esta clase se hara todos los metodos necesarios


        def load_all_users(self,fileUsuariosExistentes):            #Metodo que recibe como parametro el file de usuarios 
                with open(fileUsuariosExistentes) as file:          #existentes, y cargamos el archivo con el metodo json.load()
                    data = json.load(file)

                for client in data['usuariosExistentes']:               #Recorro el archivo json e imprimo sus respectivos valores
                    print('Nombre de usuario:', client['username'])
                    print('Contraseña:', client['password'])
                    print('Icono:', client['icono'])
                    print('Correo electrónico :', client['email'])
                    print('')


        #Metodo funcional escribir en el json
        def write_json(self,data, filename='existing_users.json'): #Pasamos por parametro el json file, que es el de usuarios registrados.
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 


    
        def validatePassword(self,passwd): #Metodo utilizado para validar la contraseña

            import re
            flag = 0

            invalid = True

            while True:   
                    if (len(passwd)<8): 
                        flag = -1
                        break
                    elif not re.search("[a-z]", passwd): 
                        flag = -1
                        break
                    elif not re.search("[A-Z]", passwd): 
                        flag = -1
                        break
                    elif not re.search("[0-9]", passwd): 
                        flag = -1
                        break
                    elif not re.search("[_@$]", passwd): 
                        flag = -1
                        break
                    elif re.search("\s", passwd): 
                        flag = -1
                        break
                    else: 
                        flag = 0
                        invalid = False
                        print("Contraseña válida") 
                        break
                
            if flag ==-1: 
                print("Contraseña inválida") 


    ###################################
        
        def passwrdValid(self,passwrd): #Metodo que recibe como parametro la contraseña, donde se utiliza una
            import re                   #expresion regular y la clase re para validar si la contrasena ingresada cumple con lo
            invalid = True               #que se solicita

            while invalid:
                passwrd = input(" Ingrese una para su cuenta contraseña :  ")
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$" #expresion utilizada para evaluar el password
                
                pat = re.compile(reg)  
                                
                mat = re.search(pat, passwrd) 
            
                # Se validan condiciones 
                if mat: 
                    invalid = False
                    print("Contraseña válida : "  +  passwrd) 
                    return passwrd
                else: 
                    
                    print("Contraseña inválida : " +  passwrd)
             

        def emailValid(self,correo):  # Metodo para validar correo, cumple con el mismo principio utilizado en el metodo para evaluar
            import re                   # la contraseña, se hace el uso de la clase re para evaluar con expresion regular
            invalid = True              # si el correo cumple con lo solicitado.

            while invalid:
                correo = input(" Ingrese su correo electrónico :  ")
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

                if(re.search(regex,correo)):
                    invalid = False 
                    print("Correo válido : " + correo)  
                    return correo
                else:  
                    print("Correo inválido : " + correo)  


        def usernameValidReg(self,username,fileUsuariosExistentes): # Metodo para evaluar por expresion regular la validez del username 
            import re                                                  
            invalid = True

            while invalid:
                username = input(" Ingrese un nombre de usuario :  ")
                regex = '^[a-zA-Z0-9](_(?!(\.|_))|\.(?!(_|\.))|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$' 

                if(re.search(regex,username)):

                    ###
                    with open(fileUsuariosExistentes) as file:
                        data = json.load(file)                      # Dentro del mismo metodo cargo mi archivo de usuarios existentes
                    usuarioTomado = ""
                    for client in data['usuariosExistentes']:

                        if(client['username'] == username):    # Hago una condicion dentro de un for donde evaluo si el usuario ingresado 
                            usuarioTomado =  username           # es igual a algun usuario existente del json, y si lo es lo almaceno

                    if usuarioTomado == username:   # Notifico al usuario que el username ya es tomado
                        print("=============================================================")
                        print("Usuario " + username + " ya ha sido seleccionado por alguien más"+". Seleccione otro usuario.")
                        print("=============================================================")
                    else:
                        pass
                    ###
                        invalid = False 
                        print("Usuario válido : " + username)  
                        return username
                else:  
                    print("Usuario inválido : " + username)  


       
        def validarUserLogin1(self,fileUsuariosExistentes,user,userCorrect):   # Este metodo es para validar si el usuario ingresado        
                                                                               # esta registrado en el sistema, de igual forma cargamos el json 
                with open(fileUsuariosExistentes) as file:                      # con los usuarios existentes, se recorre con un for
                    data = json.load(file)                                      #y se valida si el usuario seleccionado para loguearse
                usuarioTomado = ""                                              # ha esta en el sistema, si lo esta se agrega
                for client in data['usuariosExistentes']:                       # en una variable. de igual forma se le indica al usuario
                                                                                # y se returna la variable "userCorrect", si esta es true
                    if(client['username'] == user):                             # en el main se preguntara el password, en caso contrario
                        usuarioTomado =  user                                   # la password no sera solicitada.

                if usuarioTomado == user:
                    userCorrect = True
                    print("=============================================================")
                    print("El usuario ingresado " + user + " esta registrado. " + "Puede proceder a ingresar su contraseña.")
                    print("=============================================================")
                    return userCorrect
                else:
                    print("=============================================================")
                    print("El usuario ingresado " + user + " parece no estar registrado aún en el sistema. ")
                    print("Puede proceder a seleccionar a opción 2 del menú, para generar un nuevo perfil con este usuario.")
                    print("=============================================================")


        def validarPasswrdLogin1(self,fileUsuariosExistentes,passwrd,passwrdCorrect):         #Metodo similar al de arriba, se utiliza  
                with open(fileUsuariosExistentes) as file:                                      #para validar el password, pero solo es llamado
                    data = json.load(file)                                                          #cuando se valida que el usuario ingresado
                passwrdIngresado = ""                                                                 # es correcto.
                for client in data['usuariosExistentes']:

                    if(client['password'] == passwrd):
                        passwrdIngresado =  passwrd

                if passwrdIngresado == passwrd:
                    passwrdCorrect = True
                    print("=============================================================")
                    print("La contraseña ingresada es correcta.")
                    print("=============================================================")
                    return passwrdCorrect
                else:
                    print("=============================================================")
                    print("La contraseña ingresada es incorrecta")
                    print("=============================================================")



controlador = Controller()      
