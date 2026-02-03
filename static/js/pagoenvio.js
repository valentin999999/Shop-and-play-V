function pickup(){
    document.title = "Pickup"
    document.getElementById("pickup").style.display = "grid"
    document.getElementById("delivery").style.display = "none"
    document.getElementById("inicialbox").style.display = "none"
    document.getElementById("pickupboton").classList.add("opcionmarcada")
    document.getElementById("deliveryboton").classList.remove("opcionmarcada")
}

function delivery(){
    document.title = "Delivery"
    document.getElementById("delivery").style.display = "grid"
    document.getElementById("pickup").style.display = "none"
    document.getElementById("inicialbox").style.display = "none"
    document.getElementById("deliveryboton").classList.add("opcionmarcada")
    document.getElementById("pickupboton").classList.remove("opcionmarcada")
}

function departamentosi(){
    document.getElementById("titulopiso").style.display="initial"
    datopiso = document.getElementById("datopiso")
    datopiso.setAttribute("required", "")
    datopiso.style.display = "initial"
}

function departamentono(){
    document.getElementById("titulopiso").style.display = "none"
    datopiso = document.getElementById("datopiso")
    datopiso.removeAttribute("required")
    datopiso.style.display = "none"
}

function main(){
    document.addEventListener("click", function(event){
        if (event.target.matches("#confirmarpickup")){
            queryAjaxForm('validarpago','content','pickup')
        }
        else if (event.target.matches("#confirmardelivery")){
            validarlocalidad = localidad(document.getElementsByClassName("datoinput")[0].value)
            validardomicilio = validarvarios(document.getElementsByClassName("datoinput")[1].value)
            if (window.getComputedStyle(document.getElementById("datopiso")) == "none"){
                validarpiso = true
            }
            else{
                validarpiso = validarvarios(document.getElementsByClassName("datoinput")[2].value)
            }
            
            if (validarlocalidad && validardomicilio && validarpiso){
                queryAjaxForm('')
            }
            else{
                if(!validarlocalidad){
                    document.getElementsByClassName("error")[0].style.display = "initial"
                }
                if(!validardomicilio){
                    document.getElementsByClassName("error")[1].style.display = "initial"
                }
                if(!validarpiso){
                    document.getElementsByClassName("error")[2].style.display = "initial"
                }
                setTimeout(function(){
                    listaerror = document.getElementsByClassName("error")
                    for (i=0;i<listaerror.length;i++){
                        listaerror[i].style.display = "none"
                    }
                    
                },4500)
            }


        }

    })
}

function localidad(localidad){
    res = true
    for (i=0;i<localidad.length;i++){
        if (!esletramin(localidad[i]) && !esletramay(localidad[i])){
            res = false
        }
    }
    return res
}

function validarvarios(dato){
    res = true
    for (i=0;i<dato.length;i++){
        if (!esletramin(dato[i]) && !esletramay(dato[i]) && !esnum(dato[i])){
            res = false
        }
    }
    return res
}

function esletramin(l){
    listaletrasesp = "áéíóúñ"
    return l>="a" && l<="z" || listaletrasesp.includes(l)
}

function esletramay(l){
    listaletrasesp = "ÁÉÍÓÚÑ"
    return l>="A" && l<="Z" || listaletrasesp.includes(l)
}

function esnum(l){
    return l>="0" && l<="9"
}

function queryAjax(url, idDest, method="POST", dataSend=null){
    const xhr = new XMLHttpRequest()
    if(xhr){
        xhr.setTimeout = 2000;
        xhr.open(method,url,true);
        document.body.style.cursor = "wait";

        xhr.onload = () => {
            textHTML = xhr.responseText;
            document.body.style.cursor = "default";
            setDataIntoNode(idDest,textHTML);
            console.log("REQUEST COMPLETADA EXITOSAMENTE")
        };

        xhr.ontimeout = () => {
            console.log("TIME OUT");
        };
        
        xhr.onloadend = () => {
            document.body.style.cursor = "default";
            console.log("FIN")
        };

        xhr.send(dataSend);
    }
    else{
        console.log("No se pudo instanciar el objeto AJAX!");
    }
}

function queryAjaxForm(url, idDest, idForm, method="POST"){
    var formData = new FormData(document.getElementById(idForm));
    queryAjax(url, idDest, method, formData);
}

function setDataIntoNode(idDest,textHTML){
    let oElement;
    let sNameTag;
    let elementsReadOnlyInnerHTML;
    elementsReadOnlyInnerHTML = ["INPUT","COL", "COLGROUP", "FRAMESET", "HEAD", "HTML",                                  
                                 "STYLE", "TABLE", "TBODY","TFOOT", "THEAD", "TITLE","TR"
                                ];
    if(document.getElementById(idDest)) {                          
        oElement = document.getElementById(idDest);           
        sNameTag = oElement.tagName.toUpperCase();
        //console.log("***"+sNameTag);
        if(elementsReadOnlyInnerHTML.indexOf(sNameTag) == -1) {
            oElement.innerHTML = textHTML;
        }
        else if(sNameTag == 'INPUT') {                                  
            oElement.value = textHTML;
        }
        else {
            setAnyInnerHTML(oElement, textHTML); 
            console.log('El elemento destino, cuyo id="'+idDest+'", no posee propiedad "innerHTML" ni "value"!');
        }                    
    }
    else {
        console.log('El elemento destino, cuyo id="'+idDest+'", no existe!');
    }    
}

function setAnyInnerHTML(oElement, html) {
    var temp = oElement.ownerDocument.createElement('div');
    temp.innerHTML =   html ;
    oElement.parentNode.replaceChild(temp.firstChild.firstChild, oElement);
}