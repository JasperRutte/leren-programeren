const rows = 4
const collumn = 12
const colors = ["", "green", "blue", "red", "purple", "yellow", "orange"]

const randomColors = []
console.log(colors.length - 2)
for (let i = 1; i < rows + 1; i++){
    let randomNumber = Math.floor(Math.random() * (colors.length - 1)) + 1;
    randomColors.push(colors[randomNumber])
}

console.log(randomColors)


function submit(rowNumber){
    let number = rowNumber.id
    console.log(number)
    document.getElementById(rowNumber.id).disabled = true;
    let rowColors = []
    for (let i = 1; i < rows + 1; i++) {
        let selectId = document.getElementById(String(number+"-"+i))
        document.getElementById(String(number)+"-"+String(i)).disabled = true
        rowColors.push(selectId.value)
        console.log(rowColors)
    }
    for (let test = 0; test < randomColors.length; test++){
        if (rowColors[test] === randomColors[test]){
            console.log("correct")
        } else if (randomColors.includes(rowColors[test])){
            console.log("wrong spot")
        } else {

            console.log("wrong")
        }
    }
}

function changeColor(select){
    select.style.backgroundColor = select.value
}


for (let num1 = 1; num1 < collumn + 1; num1++) {
    for (let num2 = 1; num2 < rows + 1; num2++) {
        let select = document.createElement("select");
        select.setAttribute("onClick", "changeColor(this)")
        select.setAttribute("id", num1+"-"+num2);
        for (let color = 0; color < colors.length; color++) {
            let option = document.createElement("option");
            option.value = colors[color];
            option.text = colors[color];
            select.appendChild(option);
            container.appendChild(select)
        }
    }
    let redButton = document.createElement("button")
    let blueButton = document.createElement("button")

    let submit = document.createElement("button");
    submit.setAttribute("id", num1);
    submit.setAttribute("onClick", "submit(this)")
    submit.innerHTML = "SUBMIT"
    container.appendChild(submit)
}
