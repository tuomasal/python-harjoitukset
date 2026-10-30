"use strict";

let luku1 = parseInt(prompt("Anna 1. kokonaisluku:  "));
let luku2 = parseInt(prompt("Anna 2. kokonaisluku:  "));
let luku3 = parseInt(prompt("Anna 3. kokonaisluku:  "));

let summa = luku1 + luku2 + luku3;
let tulo = luku1 * luku2 * luku3;
let keskiarvo = summa / 3;

document.querySelector("#tulos").innerHTML = 
"Summa:" + summa + 
"Tulo:" + tulo + 
"Keskiarvo:" + keskiarvo;