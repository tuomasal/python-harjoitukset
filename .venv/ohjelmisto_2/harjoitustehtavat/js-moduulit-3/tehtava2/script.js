"use strict";

let maara = parseInt(prompt("Kerro osallistujien lukumäärä:"));
let nimet = [];
for (let i = 0; i < maara; i++) {
    let nimi = prompt("Anna osallistujien nimet:");
    nimet.push(nimi);
}

nimet.sort();
let lista = document.querySelector("#osallistujat")
for (let i = 0; i < nimet.length; i++) {
    let asia = document.createElement("li");
    asia.textContent = nimet[i];
    lista.appendChild(asia);
}