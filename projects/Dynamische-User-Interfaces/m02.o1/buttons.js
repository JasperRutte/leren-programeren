let counters = [0, 0, 0]

buttonCountUp = function(buttonId){
    counters[Number(buttonId.id - 1)] += 1
    document.getElementById(buttonId.id).innerHTML = counters[buttonId.id -  1]
    document.getElementById("img").src = "./images/" + String(buttonId.id) + ".jpg";
    document.getElementById('container').style.backgroundImage = "url(./images/bg" + String(buttonId.id) + ".jpg)";
}
