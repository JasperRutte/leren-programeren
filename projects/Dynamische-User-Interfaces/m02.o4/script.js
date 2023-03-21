// for (let int = 0; int < 6; int++){
//     let int2 = int
//     int2 = document.createElement("p")
//     console.log(int2)
//     int2.innerHTML = "\n"
//     for (let numb = 0; numb < 9; numb++){
//         // let numb2 = numb
//         numb2 = document.createElement("button");
//         numb2.innerHTML = "Hello Button";
//         numb2.setAttribute("id", "-" + String(numb))
//         document.body.appendChild(numb2);
//     }
// }

//
// const n = document.createElement("button");
// n.setAttribute("id", "button" + String(n))

let container = document.getElementById('container');
for (let i = 1; i < 30 + 1; i++) {
    let button = document.createElement("button");
    button.innerHTML = i;
    button.setAttribute('id', i);
    button.style.backgroundColor = '#00cc00';
    container.appendChild(button);
}