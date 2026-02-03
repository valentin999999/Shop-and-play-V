let maximo = 0
divisionjuegos(maximo)
function divisionjuegos(maximo){
    if (maximo==0){
        document.getElementById("anterior").style.display = "none"
    }
    else{
        document.getElementById("anterior").style.display = "initial"
    }
    let pagina=document.getElementsByClassName("juego")
    if (maximo+11>pagina.length){
        document.getElementById("siguiente").style.display = "none"
    }
    else{
        document.getElementById("siguiente").style.display = "initial"
    }
    for (i=0;i<pagina.length;i++){
        if (i>=10+maximo||i<maximo){
            pagina[i].style.display="none"
        }
        else{
            pagina[i].style.display="grid"
        }
    }
}
function cambio(){
    document.addEventListener("click", function(event){
        if (event.target.matches("#anterior")){
            maximo -= 10
            document.getElementById("catalogojuegos").scrollTop = 0
            divisionjuegos(maximo)
        }

    else if (event.target.matches("#siguiente")){
            maximo += 10
            document.getElementById("catalogojuegos").scrollTop = 0
            divisionjuegos(maximo)
        }
    })  
}


/*
function general(){
    error = document.getElementById("errorgeneral")
    if (error && error.innerText){
        error.style.display = "initial"
    }
    setTimeout(function(){
        error.style.display = "none"
    },4500)
}
general()
*/
cambio()