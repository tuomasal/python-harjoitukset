"use strict";

let luvut = [];

for (let i = 0; i < 5; i++) {
    let luku = parseInt(prompt("Syötä luku:"));
    luvut.push(luku);
}

console.log("Luvut päinvastaisessa järjestyksesssä");

for (let i = luvut.length - 1; i >= 0; i--) {
    console.log(luvut[i]);
}