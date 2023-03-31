colors = ["", "green", "blue", "red", "purple"]

function submit(select){
    let number = select.id
    console.log(select.id)
    document.getElementById(select.id).disabled = true;
    for (let i = 1; i < 4 + 1; i++) {
        document.getElementById(String(number)+"-"+String(i)).disabled = true
    }
}

for (let collumn = 1; collumn < 12 + 1; collumn++) {
    for (let row = 1; row < 4 + 1; row++) {
        let select = document.createElement("select");
        let selectId = collumn+"-"+row
        select.setAttribute("id", selectId);
        for (let numb2 = 0; numb2 < colors.length; numb2++) {
            let option = document.createElement("option");
            option.value = colors[numb2];
            option.text = colors[numb2];
            select.appendChild(option);
            container.appendChild(select)
        }
    }
    let submit = document.createElement("button");
    submit.setAttribute("id", collumn);
    submit.setAttribute("onClick", "submit(this)")
    submit.innerHTML = "SUBMIT"
    container.appendChild(submit)
}
