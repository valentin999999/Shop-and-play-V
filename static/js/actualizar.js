function errores(mail, pass, passdos, user){
    if (!mail){
        document.getElementById("errormail").style.display = "initial"
    }

    if (!pass){
        document.getElementById("errorpass").style.display = "initial"
    }
    
    if (!passdos){
        document.getElementById("errorpassdos").style.display = "initial"
    }
    
    if(!user){
        document.getElementById("erroruser").style.display = "initial"
    }
    setTimeout(function(){
        listaerrores = document.getElementsByClassName("error")
        
        for (i=0;i<listaerrores.length;i++){
            listaerrores[i].style.display = "none";
            }
        }, 4500)
}

function main(){
        console.log(8888)
        let listainput = document.getElementsByClassName("datoinput")

        for (i=0,listavalor=[];i<listainput.length;i++){
            listavalor.push(listainput[i].value)
        }
        validacionuser = user(listavalor[0])
        validacionmail = mail(listavalor[1])
        validacionpass = password(listavalor[2])
        validacionpassdos = listavalor[2] == listavalor[3]
        listaerrores = [validacionmail, validacionpass, validacionpassdos]
        if (validacionmail && validacionpass && validacionpassdos && validacionuser){
            queryAjaxForm('validaractualizar','content','actualizarbox')
        }
        else{
            errores(validacionmail, validacionpass, validacionpassdos, validacionuser)
        }
    }

function user(usuario){
    inputuser = document.getElementById("userinput")
    console.log(inputuser.getAttribute("minlength"))
    return usuario.length >= inputuser.getAttribute("minlength") && usuario.length <= inputuser.getAttribute("maxlength")
}

function mail(correo){
    len = false
    end = false
    arroba = false
    inicio = false
    let listacorreos = ["@gmail.com","@yahoo.com","@hotmail.com","@aol.com","@outlook.com"]
    inputcorreo = document.getElementById("mailinput")
    for (i=0;i<listacorreos.length;i++){
        if (correo.endsWith(listacorreos[i])){
            end = true
        }
    }
    if (correo.length >= inputcorreo.getAttribute("minlength") && correo.length <= inputcorreo.getAttribute("maxlength")){
        len = true
    }
    for (j=0,arrobacont=0;j<correo.length;j++){
        if (correo[j]=="@"){
            arrobacont++
        }
    }
    if (arrobacont == 1){
        arroba = true
    }

    if (correo[0]!="@"){
        inicio = true
    }

    return len && end && arroba && inicio
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


function password(pass){
    for (i=0,min=may=sim=num=space=len=false;i<pass.length;i++){
        if (esletramay(pass[i])){
            may = true
        } 
        else if (esletramin(pass[i])){
            min = true
        }
        else if (esnum(pass[i])){
            num = true
        } 
        else if (pass[i] != " "){
            sim = true
        } 
        else{
            space = true
        }
    }
    inputpass = document.getElementById("passinput")
    if (pass.length >= inputpass.getAttribute("minlength") && pass.length <= inputpass.getAttribute("maxlength")){
        len = true
    }
    return may && min && num && sim && len && !space
}

function general(){
    error = document.getElementById("errorgeneral")
    if (error){
        if (error.innerText){
            error.style.display = "initial"
        }
    }
    setTimeout( function(){
        error.style.display = "none"
    },4500)
}

general()


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
            general()
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

