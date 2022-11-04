$(document).ready(function(){
    var imgs = $("#carrousel img");
    var i = 0;
    imgs.css("display", "none");
    function slideImg(){
        var current_img = imgs.eq(i);
        current_img.css("display", "block");
        i++;
        if (i == imgs.length){
            i = 0;
        }
        var next_img = imgs.eq(i);
        setTimeout(function(){
            current_img.fadeOut(2000);
            next_img.fadeIn(2000);
            slideImg();
        }, 5000);
    }
slideImg();
});

