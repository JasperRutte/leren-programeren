let button1 = document.getElementById("button1"),
    count1 = 0;

let button2 = document.getElementById("button2"),
    count2 = 0;

let button3 = document.getElementById("button3"),
    count3 = 0;


button1.onclick = function() {
    count1 += 1;
    button1.innerHTML = count1;
    document.getElementById("img").src = "./images/1.jpg"
    document.getElementById('container').style.backgroundImage = "url(./images/bg1.jpg)";
};


button2.onclick = function() {
    count2 += 1;
    button2.innerHTML = count2;
    document.getElementById("img").src = "./images/2.jpg"
    document.getElementById('container').style.backgroundImage = "url(./images/bg2.jpg)";

};


button3.onclick = function() {
    count3 += 1;
    button3.innerHTML = count3;
    document.getElementById("img").src = "./images/3.jpg"
    document.getElementById('container').style.backgroundImage = "url(./images/bg3.jpg)";
};