let container = document.getElementById('container');

for (let i = 1; i < 48 + 1; i++) {
    let button = document.createElement("select");
    container.appendChild(button);
}
//
// function myFunction() {
//     var x = document.getElementById("mySelect");
//     var option = document.createElement("option");
//     option.text = "Kiwi";
//     x.add(option);