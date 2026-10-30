"use script";

let lukumaara = parseInt(prompt("Kuinka monesti heität noppaa?"));
let summa = 0;

for (let i = 0; i < lukumaara; i++){
let silmaluku = Math.floor(Math.random() * 6) + 1;
summa = summa + silmaluku;
}
document.querySelector("#tulos").textContent =
"Nopan heittojen silmälukjen summa =" + summa; 