var block = document.getElementById("block");
var hole = document.getElementById("hole");
var birdy = document.getElementById("birdy");
var jumping = 0;
var counter = 0;

hole.addEventListener('animationiteration', () => {
    var random = Math.random()*3;
    var top = random(random*100)+150;
    hole.style.top = -(top) + "px";
    counter++;
});

setInterval(function(){
    var birdyTop = parseInt(window.getComputedStyle(birdy).getPropertyValue("top"));
    if(jumping==0){
    birdy.style.top = (birdyTop+3)+"px";
    }
    var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
    var holeTop = parseInt(window.getComputedStyle(hole).getPropertyValue("top"));
    var bTop = -(500-birdyTop);
    if((birdyTop>480)||((blockLeft<20)&&(blockLeft>-50)&&((bTop<holeTop)||(bTop>holeTop+130)))){
        alert("Game over. Score: ");
        birdy.style.top = 100 + "px";
        counter=0;
    }
},10);

function jump(){
    jumping = 1;
    let jumpCount = 0;
    var jumpInterval = setInterval(function(){
        var birdyTop = parseInt(window.getComputedStyle(birdy).getPropertyValue("top"));
        if((birdyTop>6)&&(counter<15)){
            birdy.style.top = (birdyTop-4)+"px";
        }
        if(jumpCount>20){
            clearInterval(jumpInterval);
            jumping=0;
            jumpCount=0;
        }
        jumpCount++;
    },10);
}

/* inspiration and instructions came from https://www.youtube.com/watch?v=3SsYZDJdeXk */
