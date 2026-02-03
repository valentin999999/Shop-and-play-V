if (document.getElementById("juegoprecio")){
    sliderprecio = document.getElementById("juegoprecio")
}
if (document.getElementById("preciovalor")){
    precio = document.getElementById("preciovalor")
}
if (document.getElementById("unidad")){
    unidad = document.getElementById("unidad")
}

if (document.getElementById("juegoprecio") && document.getElementById("preciovalor")){
    sliderprecio.oninput = function actualizarPrecio(){
        precio.innerHTML = parseFloat(this.value).toFixed(2);
    }
}

if (document.getElementById("juegostock")){
    sliderstock = document.getElementById("juegostock")
}
if(document.getElementById("stockvalor")){
    stock = document.getElementById("stockvalor")
}
if (document.getElementById("juegostock") && document.getElementById("stockvalor")){
    sliderstock.oninput = function actualizarStock(){
        stock.innerHTML = this.value
        plural()
}
}

document.addEventListener("click",function(event){
    if (event.target.matches("#juegoboton")){
        valList = []
        var cont1 = 0
        if (document.getElementById("juegoportada").value){
            valList.push(document.getElementById("juegoportada").value)
            cont1++
        }
        else{
            document.getElementById("errorbox").style.display = "grid"
            document.getElementById("errorportada").style.display = "initial"
        }
        if (document.getElementById("juegoimagenprincipal").value){
            valList.push(document.getElementById("juegoimagenprincipal").value)
            cont1++
        }
        else{
            document.getElementById("errorbox").style.display = "grid"
            document.getElementById("errorimagenprincipal").style.display = "initial"
        }
        inputList = document.getElementsByClassName("juegoinput")
        for (i=0,cont2=0;i<inputList.length;i++){
            if (inputList[i].value && inputList[i].id != "juegoprecio" && inputList[i].id   != "juegostock"){
                valList.push(inputList[i].id.slice(5))
                console.log("error"+inputList[i].id.slice(5))
                document.getElementById("error"+inputList[i].id.slice(5)).style.display = "none"
            }
            else if (inputList[i].id != "juegoprecio" && inputList[i].id   != "juegostock"){
                console.log(inputList[i].id.slice(5))
                document.getElementById("errorbox").style.display = "grid"
                document.getElementById("error"+inputList[i].id.slice(5)).style.display = "initial"
                cont2++
            }
            }
        setTimeout(function(){
            document.getElementById("errorbox").style.display = "none"
            errorList = document.getElementsByClassName("error")
            for (k=0;k<errorList.length;k++){
                errorList[k].style.display = "none"
            }
        },4500)
        if (cont1==2 && !cont2){
            queryAjaxForm('validarjuego','content','juegobox')
        }
    }
})


function plural(){
    if (document.getElementById("stockvalor") && stock.innerText.trim() == "1" && document.getElementById("unidad")){
        unidad.innerHTML="Unidad"
    }
    else if (document.getElementById("unidad")){
        unidad.innerHTML="Unidades"
    }
}

function general(){
    error = document.getElementById("errorgeneral")
    if (error && error.innerText){
        error.style.display = "initial"
    }
    setTimeout( function(){
        error.style.display = "none"
    },4500)
}
general()
plural()

function añadirTag(){
    tagList = document.getElementsByClassName("taginput")
    tagNomList = []
    for (i=0;i<tagList.length;i++){
        if (!tagNomList.includes(tagList[i].value.toUpperCase())){
            tagNomList.push(tagList[i].value.toUpperCase())
        }
    }
    tagNom = document.getElementById("nuevoTagTexto").value
    if (!tagNomList.includes(tagNom.toUpperCase()) && tagNom){
        tagNum = String(tagList.length)
        tagBox = document.getElementById("tagbox")
        
        nuevoDiv = document.createElement("div")
        tagBox.appendChild(nuevoDiv)
        nuevoDiv.classList.add("opcionbox")
        nuevoTag = document.createElement("input")
        nuevoDiv.appendChild(nuevoTag)
        nuevoTag.classList.add("taginput")
        nuevoTag.setAttribute("type","checkbox")
        nuevoTag.id = "tag"+tagNum
        nuevoTag.setAttribute("name",nuevoTag.id)
        nuevoTag.setAttribute("value",tagNom)
        nuevoLabel = document.createElement("label")
        nuevoDiv.appendChild(nuevoLabel)
        nuevoLabel.classList.add("etiquetatag")
        nuevoLabel.setAttribute("for",nuevoTag.id)
        nuevoLabel.innerText = tagNom
    }
    else if (tagNom){
        document.getElementById("errorgeneral").innerText = "Tag '"+tagNom+"' ya existente"
        general()
    }
    else{
       document.getElementById("errorgeneral").innerText = "Introduzca nombre de tag a añadir" 
       general()
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