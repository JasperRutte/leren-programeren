function changeColor(btn) {
    let btnColor = btn.style.backgroundColor
    if (btnColor === "rgb(0, 255, 0)"){
        return
    }



}

let container = document.getElementById('container');
for (let i = 1; i < 30 + 1; i++) {
    let button = document.createElement("button");
    button.innerHTML = i;
    button.setAttribute("id", i);
    button.setAttribute("onClick", "changeColor(this)");
    button.style.backgroundColor = "#00ff00";
    container.appendChild(button);
}
