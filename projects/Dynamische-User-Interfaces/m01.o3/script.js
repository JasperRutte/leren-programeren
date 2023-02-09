let question = prompt("getal:")

if (question == 20){
    for (let x = 1; x < 21; x++) {
        let numb = []
        for (let y = 1; y <= x; y++) {
            numb.push(y)
        }

        const para = document.createElement("p");
        let testing = numb.join("-")
        para.innerHTML = testing;

        document.getElementById("test").appendChild(para);
    }


    for (let x = 19; x > 0; x--) {
        let numb2 = []
        for (let y = 1; y <= x; y++) {
            numb2.push(y)
        }

        const para = document.createElement("p");
        let testing = numb2.join("-")
        para.innerHTML = testing;

        document.getElementById("test").appendChild(para);
    }
} else {
    alert("beep")
}


