"use strict";

let luvut = [];
let luku = parseInt(prompt("Anna luku:"));

while (!luvut.includes(luku)) {
    luvut.push(luku);
    luku = parseInt(prompt("Anna luku:"));
}

console.log("Luku on jo annettu");

luvut.sort(function(a, b) {
    return a - b;
});

for (let i = 0; i < luvut.length; i++) {
    console.log(luvut[i]);
}