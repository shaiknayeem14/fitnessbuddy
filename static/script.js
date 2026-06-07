function showMessage() {

    alert(
        "Stay consistent and trust the process!"
    );
}

function showLoader() {

    let loader =
    document.getElementById("loader");

    if(loader){

        loader.style.display = "block";
    }
}

function typeWriter(text, elementId) {

    let i = 0;

    let speed = 25;

    document.getElementById(elementId).innerHTML = "";

    function typing() {

        if(i < text.length){

            document
            .getElementById(elementId)
            .innerHTML += text.charAt(i);

            i++;

            setTimeout(
                typing,
                speed
            );
        }
    }

    typing();
}

window.onload = function(){

    console.log(
        "Fitness Buddy Loaded Successfully"
    );

}