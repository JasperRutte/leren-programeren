function potenTellen(giraffen, struisvogel, zebra){
    let total = 0;
    total = giraffen * 4;
    total = total + struisvogel * 2;
    total = total + zebra * 4;
    return total
}

let giraffen = Number(prompt("Hoeveel giraffen poten?"))
let struisvogel = Number(prompt("Hoeveel struisvogel poten?"))
let zebra = Number(prompt("Hoeveel zebra poten"))

alert(potenTellen(giraffen, struisvogel, zebra))
