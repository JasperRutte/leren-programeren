let counters = [0, 0, 0]


buttonCountUp = function(button){
    const buttonElement = document.getElementById(button.id)
    for (let i = 1; i < counters.length + 1; i++) {
        const element = document.getElementById(i)

        element.style.backgroundColor = "#00a115"
        element.disabled = false
    }

    counters[Number(button.id - 1)] += 1
    buttonElement.innerHTML = counters[button.id -  1]
    document.getElementById("img").src = "./images/" + String(button.id) + ".jpg";
    document.getElementById('container').style.backgroundImage = "url(./images/bg" + String(button.id) + ".jpg)";
    buttonElement.style.backgroundColor = "#fc1303"
    buttonElement.disabled = true
}

