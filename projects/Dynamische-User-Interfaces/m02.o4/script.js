const colors = ["green", "red", "purple", "orange", "silver", "gold", "blue", "black"]

function changeButtonColor(btn) {
    let buttonColor = btn.style.backgroundColor
    let colorInArray = colors.indexOf(buttonColor)
    if (colorInArray + 1 === colors.length){
        btn.remove()
    } else {
        btn.style.backgroundColor = colors[colorInArray + 1]
    }
}

let container = document.getElementById('container');
for (let i = 1; i < 30 + 1; i++) {
    let button = document.createElement("button");
    button.innerHTML = i;
    button.setAttribute("onClick", "changeButtonColor(this)");
    button.style.backgroundColor = colors[0];
    container.appendChild(button);
}