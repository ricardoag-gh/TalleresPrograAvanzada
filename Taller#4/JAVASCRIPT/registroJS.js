


function pageRedirectIndex(){
    window.location.href = "../HTML/index.html";
    }

    function placeInfoHlbl(){

    var name = document.getElementById("formRegistro").elements[0].value;
    var lastName = document.getElementById("formRegistro").elements[1].value;
    var usuario = document.getElementById("formRegistro").elements[2].value;
    var correo = document.getElementById("formRegistro").elements[3].value;
    var password = document.getElementById("formRegistro").elements[4].value;

    var mi_json_en_string = '{"Nombre":"NombreQuemado"}'

    
    obj_json = JSON.parse(mi_json_en_string)
    
    
    
    document.getElementById("demo").innerHTML = obj_json.Nombre

    
    
}



