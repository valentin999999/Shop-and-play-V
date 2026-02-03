function obtenerValores(){
    document.getElementById("abonoprecio").innerText = monto()
    document.getElementById("inputvalor").value = Number(monto().slice(1))
    document.getElementById("inputproducto").value = recuento()
    document.getElementById("inputfecha").value = new Date().toISOString().slice(0,10)
    listavalor = document.getElementsByClassName("numerovalor")
    listacantidad = document.getElementsByClassName("cantidadInicial")
    listastockadi = document.getElementsByClassName("stockadicional")
    for (i=0;i<listavalor.length;i++){
        listastockadi[i].value = String(Number(listacantidad[i].value)-Number(listavalor[i].innerText))
    }
    listaStock = []
    for (i=0;i<listastockadi.length;i++){
        listaStock.push(listastockadi[i].value)
    }
    document.getElementById("inputstock").value = listaStock
}


if (document.getElementsByClassName("barra").length!=0){
    document.getElementsByClassName("barra")[document.getElementsByClassName("barra").length-1].style.display = "none"
}
    
function monto(){
    const listacabeceras = document.getElementsByClassName("juegoprecio")
    const listanumeros = document.getElementsByClassName("numerovalor")
    for (i=0,montofinal=0;i<listacabeceras.length;i++){
        existencia = window.getComputedStyle(listacabeceras[i].closest(".juego")).display
        valor = Number(listanumeros[i].innerText)
        if (existencia != "none"){
            precio = Number(listacabeceras[i].textContent.slice(1))
            multiplicador = Number(listanumeros[i].innerText)
            montofinal += precio * multiplicador
        }
    }
    carritoVacio()
    barra()
    return "$" + String(montofinal.toFixed(2))
}


function barra(){
        if (document.getElementsByClassName("barra").length){
            let listabarra = document.getElementsByClassName("barra")
            listabarra[listabarra.length-1].style.display = "none"
        }
    }

document.addEventListener("input", function(event){
    if (event.target.matches(".juegonumero")){
        event.target.nextElementSibling.innerText = event.target.value
    }
})

function recuento(){
    listatitulos=[]
    titulos = document.getElementsByClassName("juegonombre")
    for (i=0;i<titulos.length;i++){
        if (window.getComputedStyle(titulos[i].closest(".juego")).display != "none"){
            listatitulos.push(titulos[i].innerText)
        }
    }

    listacantidades=[]
    cantidades = document.getElementsByClassName("numerovalor")
    for (i=0;i<cantidades.length;i++){
        if (window.getComputedStyle(cantidades[i].closest(".juego")).display != "none"){
            listacantidades.push(cantidades[i].innerText)
        }
    }

    listacontenido = []

    for (i=0;i<listacantidades.length;i++){
        listacontenido.push("("+listatitulos[i]+","+listacantidades[i]+")")
    }
    return "["+listacontenido+"]"
}
obtenerValores()

function carritoVacio(){
    listajuegos = document.getElementsByClassName("juego")
    for (i=0,cont=0;i<listajuegos.length;i++){
        if (!listajuegos[i].innerText){
            listajuegos[i].style.display="none"
        }
        else{
            cont++
        }   
    }
    if (!cont){
        console.log(77777)
        document.getElementById("mensajevacio").style.height = "min-content";
        document.getElementById("listajuegos").style.gridTemplateRows = "min-content";
        document.getElementById("listajuegos").style.height = "min-content";
        document.getElementById("listajuegos").style.overflowY = "hidden";
        document.getElementById("listajuegos").style.alignSelf = "center";
        document.getElementById("listajuegos").style.height = "min-content";
        document.getElementById("listajuegos").style.width = "max-content";
        document.getElementById("abonaretiqueta").style.display = "none";
        document.getElementById("mensajevacio").style.display = "initial";

    }
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
            console.log("REQUEST COMPLETADA EXISTOSAMENTE")
        };

        xhr.ontimeout = () => {
            console.log("TIME OUT");
        };
        
        xhr.onloadend = () => {
            document.body.style.cursor = "default";
            console.log("FIN")
            carritoVacio()
            obtenerValores()
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
