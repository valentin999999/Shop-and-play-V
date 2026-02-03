let sliderprecio = document.getElementById("juegoprecio")
let precio = document.getElementById("preciovalor")
let unidad = document.getElementById("unidad")

sliderprecio.oninput = function actualizarPrecio(){
    precio.innerHTML = parseFloat(this.value).toFixed(2);
}

let sliderstock = document.getElementById("juegostock")
let stock = document.getElementById("stockvalor")
sliderstock.oninput = function actualizarStock(){
    stock.innerHTML = this.value
    plural()
}

function plural(){
    if (stock.innerText.trim() == "1"){
        unidad.innerHTML="Unidad"
    }
    else{
        unidad.innerHTML="Unidades"
    }
}

function general(){
    error = document.getElementById("errorgeneral")
    if (error.innerText){
        error.style.display = "initial"
    }
    setTimeout(function(){
        error.style.display = "none"
    },4500)
}
general()
plural()

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
            general()
        };

        xhr.ontimeout = () => {
            console.log("TIME OUT");
        };
        
        xhr.onloadend = () => {
            document.body.style.cursor = "default";
            console.log("FIN")
            general()
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