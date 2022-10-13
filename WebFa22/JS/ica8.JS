function reveal(){
    document.getElementById("hide").style.display= "block";
}
const backgroundcolor = document.getElementById("button2");
const body = document.body;
const colors = ["pink","orangered","cadetblue","grey"]

backgroundcolor.addEventListener("click", changebackground)

function changebackground(){
    const colorsIndex = Math.floor(Math.random()*colors.length)
    body.style.backgroundColor = colors[colorsIndex]
}