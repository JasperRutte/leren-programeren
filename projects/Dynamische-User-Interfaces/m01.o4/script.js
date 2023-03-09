let answer = ""
const items = {
    bier: 0,
    fris: 0,
    wijn: 0,
}

while (answer !== "stop") {
    answer = prompt("Wat wilt u bestellen")
    if (!(answer in items)) {
        if (answer !== "stop") {
            alert("Dat begrijp ik niet")
        } else {
            continue
        }
    } else {
        let amountQuestion = Number(prompt("Hoeveel?"))
        items[answer] += amountQuestion
        console.log(items)
    }
}


let itemsFormatted = "";
let total = 0;

for (const [key, value] of Object.entries(items)) {
    if (value === 0){
        continue
    }
    let price;
    if (key === "bier"){
        price = Number(value) * 3;
    } else if (key === "fris"){
        price = Number(value) * 2;
    } else {
        price = Number(value) * 5;
    }
    total = Number(total) + Number(price)
    itemsFormatted = `${itemsFormatted}${key}: ${value}x: ${price.toFixed(2)}</br>`;
}
document.getElementById("myDiv").innerHTML = itemsFormatted;

document.getElementById("myDiv2").innerHTML = (total.toFixed(2))
