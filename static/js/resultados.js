function general(){
    res = document.getElementById("msjresultados")
    if (res && res.innerText){
        res.style.display = "initial"
        catalogotitulo = document.getElementById("catalogotitulo").innerText
        busqueda = catalogotitulo.slice(17,catalogotitulo.length-1)+"'"
        res.innerText+=busqueda
        document.getElementById("catalogotitulo").style.display="none"
        document.title = "Sin resultados para '"+busqueda
    }
}

general()