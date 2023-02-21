let question = ""
let items = {}

while (question !== "fris" || question !== "bier" || question !== "wijn") {
    question = prompt("Wat wilt u bestellen")
    if (question === "fris" || question === "bier" || question === "wijn") {
        let amountQuestion = Number(prompt("Hoeveel:"))
        if (question in items){
            items[question] += amountQuestion
        } else {
            items[question] = amountQuestion;
        }
        console.log(items);
    } else if (question === "stop"){
        break
    } else {
        alert("dit ken ik niet")
    }
}


function objectToString(items){
    if (items === "fris") {
        let getal = Object.values("fris")
        console.log(getal)
    }
}
items.forEach(objectToString)


let myString = JSON.stringify(items, null, " ");
document.getElementById("myDiv").innerHTML = myString;

