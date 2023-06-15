let animals = ["lion", "lobster", "seagull", "skunk", "turtle", "bear", "deer", "frog", "horse"];
let number = 0

console.log(document.getElementById("animal").src)
function changeImg(plusMin){
    if (plusMin === `+`){
        number++
    } else {
        number--
    }

    if (number === animals.length) {
        number = 0
    } else if(number === -1) {
        number = animals.length-1
    }

    document.getElementById("animal").src = "images/"+animals[number]+'.jpg'
}