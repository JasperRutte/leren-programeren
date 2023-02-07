let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n"+
"Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

alert(uitleg);
let gewenste_aantal_autos = prompt("Hoeveel autos wilt u kwijt in de parkeergarage?");

let aantal = Math.ceil((gewenste_aantal_autos - 80) / 120);

let antwoord = "Ik heb " + aantal + " verdiepingen nodig";
document.getElementById("antwoord").innerText = antwoord;
window.alert(aantal)


console.log("Om het gewenste aantal autos kwijt te kunnen heb ik " + aantal + " verdiepingen nodig.")
