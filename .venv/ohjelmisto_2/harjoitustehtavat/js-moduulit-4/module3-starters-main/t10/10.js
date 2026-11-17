let form = document.querySelector("#source")
let target = document.querySelector("#target")
let etunimi = document.querySelector("input[name=firstname]");
let sukunimi = document.querySelector("input[name=lastname]");

form.addEventListener("submit", (e) =>{
    e.preventDefault();

    let str = "Nimesi on " + etunimi.value + " " + sukunimi.value
    console.log(str)
    target.textContent = str
})