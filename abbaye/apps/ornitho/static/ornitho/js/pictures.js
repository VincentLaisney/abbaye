var links = document.querySelectorAll("td a");
var links_length = links.length;

for(var i = 0; i < links_length; i++){
    links[i].addEventListener("click", function(e){
        e.preventDefault();
        displayImg(e.currentTarget, 900, 600);
        });
}

function displayImg(link, maxW, maxH){
    var img = new Image();
    var overlay = document.getElementById("overlay");

    img.addEventListener("load", function(){
        overlay.innerHTML = "";
        if(img.width > maxW || img.height > maxH)
            var reduc = Math.max(img.width / maxW, img.height / maxH);
        else
            var reduc = 1;
        img.width = Math.round(img.width / reduc);
        img.height = Math.round(img.height / reduc);
        overlay.appendChild(img);
    });
    
    img.src = link;
    overlay.style.height = window.innerHeight + "px";
    overlay.innerHTML = "<span>Chargement de l'image…</span>";
    overlay.style.display = "flex";
}

document.getElementById("overlay").addEventListener("click", function(e){
    e.currentTarget.innerHTML = "";
    e.currentTarget.style.display = "none";
});

