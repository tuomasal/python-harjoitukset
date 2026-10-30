"use strict";

let luku = parseInt(prompt("Anna joku kokonaisluku"));
let alkuluku = true;

if (luku <= 1) {
alkuluku = false;
} else {
for (let i = 2; i < luku; i++) {
if (luku % i === 0) {
alkuluku = false;
}
}
}
if (alkuluku) {
document.querySelector("#tulos").textContent = 
luku + " on alkuluku";
} else {
document.querySelector("#tulos").textContent = 
luku + " ei ole alkuluku";
}