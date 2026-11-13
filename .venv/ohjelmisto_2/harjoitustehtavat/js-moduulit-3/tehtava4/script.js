"use strict";
let luvut = [];
let luku = parseInt(prompt("Anna luku (0 lopettaa):"));
while (luku !== 0) {
    luvut.push(luku);
    luku = parseInt(prompt("Anna luku (0 lopettaa):"));
}
luvut.sort(function(a, b) {
    return b - a;
});
for (let i = 0; i < luvut.length; i++) {
    console.log(luvut[i]);
}