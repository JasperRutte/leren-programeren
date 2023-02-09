let question = ""

while (question != "fris" || question != "bier" || question != "wijn") {
    question = prompt("Wat wilt u bestellen")
    if (question == "fris" || question == "bier" || question == "wijn") {
        alert("Toegevoegd")
    } else if (question == "stop"){
        break
    } else {
        alert("dit ken ik niet")
    }
}