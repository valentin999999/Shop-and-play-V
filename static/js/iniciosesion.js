function main(){
            if (!validar()){
            setTimeout(function(){
                listaerrores = document.getElementsByClassName("error")
                for (i=0;i<listaerrores.length;i++){
                    listaerrores[i].style.display = "none"
                }
                document.getElementById("errorgeneral").innerText = ""
            }, 3500)
            
        }
}



function validar(){
    msj = document.getElementById("errorgeneral").innerText
    res = true
    if (msj){
        res = false
        listaerrores = document.getElementsByClassName("error")
        for (i=0;i<listaerrores.length;i++){
            listaerrores[i].style.display = "initial"
        }
    }
    return res
}

main()

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
            main()
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
    console.log(url)
    console.log(idDest)
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