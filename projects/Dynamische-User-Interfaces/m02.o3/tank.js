let image = document.getElementById("image");

image.style.transform = "rotate(90deg)"

let direction = image.style.transform


let wheels = 0
let upDown = 0
let leftRight = 0


function driving(key) {
    if (key == 32) {
        console.log("spacebar");
    } else if (key == '38') {  // up arrow
        image.style.transform = "rotate(0)"
        image.style.backgroundPosition = `${wheels = wheels + 84}px 0px`;
        upDown = upDown - 10
        image.style.marginTop = String(upDown) + "px"
    } else if (key == '40') { // down arrow
        image.style.transform = "rotate(180deg)"
        image.style.backgroundPosition = `${wheels = wheels - 84}px 0px`;
        upDown = upDown +    10
        image.style.marginTop = String(upDown) + "px"
    } else if (key == '37') { // left arrow
        image.style.transform = "rotate(270deg)"
        image.style.backgroundPosition = `${wheels = wheels - 84}px 0px`;
        image.style.marginLeft = String(leftRight = leftRight - 10) + "px"
        console.log("left arrow");
    } else if (key == '39') {   // right arrow
        image.style.transform = "rotate(90deg)"
        image.style.backgroundPosition = `${wheels = wheels + 84}px 0px`;
        image.style.marginLeft = String(leftRight = leftRight + 10) + "px"
    }
}


document.onkeydown = checkKey;
function checkKey(e) {
    console.log("key nr = " + e.keyCode);
    let key = e.keyCode
    e = e || window.event;
    if(key == 32){
        driving(key) // spacebar
    } else if (key == '38') {  // up arrow
        driving(key)
    } else if (key == '40') { // down arrow
        driving(key)
    } else if (key == '37') { // left arrow
        driving(key)
    } else if (key == '39') {   // right arrow
        driving(key)
    }
}