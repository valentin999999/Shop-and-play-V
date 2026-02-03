let valorbusqueda = document.getElementById("searchbar").value.toUpperCase()
let listares = document.getElementsByClassName("res")
let listatagres = document.getElementsByClassName("tagres")
let cajabusqueda = document.getElementById("busquedabox")
let cajamenu = document.getElementById("cambiobox")

function autosugerencia(){
    for (i=0,cont=0;i<listatagres.length;i++){
            listatagres[i].closest(".atagres").style.display = "none"
    }
    let valorbusqueda = document.getElementById("searchbar").value.toUpperCase()
    if (valorbusqueda && valorbusqueda[0] != "#"){
        cajabusqueda.style.display = "grid"
        for (i=0,cont=0;i<listares.length;i++){
            if (listares[i].innerText.toUpperCase().includes(valorbusqueda)){
                listares[i].closest(".ares").style.display = "initial"
                cont++
            }
            else{
                listares[i].closest(".ares").style.display = "none"
            }
        }
        
        if (cont==0){
            cajabusqueda.style.display = "none"
        }
    }
    else if (valorbusqueda && valorbusqueda[0] == "#"){
        cajabusqueda.style.display = "grid"
        for (j=0,cont=0;j<listares.length;j++){
            listares[j].closest(".ares").style.display = "none"
        }
        for (j=0,cont=0;j<listatagres.length;j++){
            if (listatagres[j].innerText.toUpperCase().includes(valorbusqueda.slice(1))){
                listatagres[j].closest(".atagres").style.display = "initial"
                cont++
            }
            else{
                listatagres[j].closest(".atagres").style.display = "none"
            }
        }
        if (cont==0){
            cajabusqueda.style.display = "none"
        }
    }
}

document.addEventListener("click", function(event){
    if (!event.target.matches("#searchbar") && !event.target.matches("#busquedabox")){
        cajabusqueda.style.display = "none"
    }
})

document.addEventListener("click", function(event){
    if (event.target.matches("#usuario") && window.getComputedStyle(cajamenu).display == "none"){
        cajamenu.style.display = "initial"
    }
    else{
        cajamenu.style.display = "none"
    }
})

if (document.getElementById("editarbox")){
    editBox = document.getElementById("editarbox")
    if (window.location.href.includes("/juego/") && !window.location.href.includes("/editarjuego")){
        editBox.style.display = "grid"
        titulo = document.getElementById("titulojuego").innerText
        editBox.setAttribute("href","/juego/"+titulo+"/editarjuego")
    }
    else{
        document.getElementById("editarbox").style.display = "none"
    }
}

autosugerencia()



