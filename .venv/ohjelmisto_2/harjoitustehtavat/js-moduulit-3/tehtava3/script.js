"use strict";

let koirat = [];

for (let i = 0; i < 6; i++) {
    let nimi = prompt("Anna koiran nimi:");
    koirat.push(nimi);
}

koirat.sort();
koirat.reverse();

let lista = document.querySelector("#koirat");
for (let i = 0; i < koirat.length; i++) {
    let kohta = document.createElement("li");
    kohta.textContent = koirat[i];
    lista.appendChild(kohta);
}
