import json 

from MODEL.models import Player

jug = Player()

  
#Working to append
# function to add to JSON 
def write_json(data, filename='regisTest.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
"""     
with open('regisTest.json') as json_file:

    data = json.load(json_file) 
      
    temp = data['usuariosRegistrados'] 
    
    jug._username = input(" Ingrese su usuario *:  ")  
    jug._password = input(" Ingrese su password *:  ")
    jug.icon = input("Ingrese su icono *: ")
    jug._email = input("Ingrese su correo *: ")

    # python object to be appended 
    y = {"username":jug._username, 
         "password": jug._password, 
         "icono": jug._icon,
         "email": jug._email
        } 
  
  
    # appending data to emp_details  
    temp.append(y) 
      
write_json(data)  
#Working to append
"""





 