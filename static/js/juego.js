let formcompra = document.getElementById("comprabox")
let preciooriginal = ""
if (document.getElementById("precio") && !preciooriginal){
    preciooriginal = document.getElementById("precio").innerText.slice(1)
}


function cantidad(){
    if (document.getElementById("unidadvalor") && document.getElementById("unidadinput") && document.getElementById("precio")){
        p = document.getElementById("unidadvalor")
        sliderstock = document.getElementById("unidadinput")
        precio = document.getElementById("precio")
        precio.innerHTML = "$"+String(Number(preciooriginal*sliderstock.value).toFixed(2))
        p.innerText = sliderstock.value
    }
}

cantidad()

function calificar(){
    if (document.getElementById("tunumero")){
        sliderpuntuacion = document.getElementById("tunumero")
        document.getElementById("puntuacion").innerText = sliderpuntuacion.value
    }
}

calificar()

function general(){
    errorbox = document.getElementById("errorbox")
    error = document.getElementById("errorgeneral")
    if (error.innerText){
        errorbox.style.display = "grid"
        error.style.display = "initial"
        if (error.innerText.includes("enviada")){
            error.style.backgroundColor = "green"
        }
    }
    setTimeout(function(){
        errorbox.style.display = "none"
        error.style.display = "none"
    },4500)
}

general()

function color(){
    if (document.getElementsByClassName("textoreseña").length){
        listaCali = document.getElementsByClassName("textoreseña")
        for (i=0;i<listaCali.length;i++){
            if (Number(listaCali[i].innerText)==5){
                listaCali[i].style.color = "blue"
            }
            else if (Number(listaCali[i].innerText)>=4){
                listaCali[i].style.color = "green"
            }
            else if (Number(listaCali[i].innerText)>=3){
                listaCali[i].style.color = "yellow"
            }
            else if (Number(listaCali[i].innerText)>=2){
                listaCali[i].style.color = "orange"
            }
            else{
                listaCali[i].style.color = "red"
            }
        }
    }
}
color()

function queryAjax(url, idDest, method="POST", dataSend=null){
    if (document.getElementById("tunombre")){
        nombre = document.getElementById("tunombre").innerText
    }
    if (document.getElementById("tunumero")){
        sliderpuntuacion = Number(document.getElementById("tunumero").value)
    }
    console.log(url,idDest,method,dataSend)
    const xhr = new XMLHttpRequest()
    console.log(xhr)
    
    if(xhr){
        xhr.setTimeout = 2000;
        xhr.open(method,url,true);
        document.body.style.cursor = "wait";

        xhr.onload = () => {
            textHTML = xhr.responseText;
            document.body.style.cursor = "default";
            setDataIntoNode(idDest,textHTML);
            console.log("REQUEST COMPLETADA EXITOSAMENTE")
            general()
            color()
        };

        xhr.ontimeout = () => {
            console.log("TIME OUT");
        };
        
        xhr.onloadend = () => {
            document.body.style.cursor = "default";
            console.log("FIN")
            calificar()
            general()
            color()
        };

        xhr.send(dataSend);
    }
    else{
        console.log("No se pudo instanciar el objeto AJAX!");
    }
}

function queryAjaxForm(url, idDest, idForm, method="POST"){
    var formData = new FormData(document.getElementById(idForm));
    console.log(formData)
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