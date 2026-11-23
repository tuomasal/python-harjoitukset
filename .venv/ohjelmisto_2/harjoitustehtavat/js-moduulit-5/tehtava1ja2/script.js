"use strict";
const tvForm = document.querySelector("#tv-form");
tvForm.addEventListener("submit", async function (evt) {
            evt.preventDefault();
            const query = document.querySelector("#query").value;
             const value_from_input = document.querySelector("#query").value;
try {
    const response = await fetch(
        `https://api.chucknorris.io/jokes/search?query=${value_from_input}`
        );
        if (!response.ok) {
            throw new Error("HTTP-virhe: " + response.status);
        }
        const jsonData = await response.json();
        const results = document.querySelector("#results");
        results.innerHTML = "";
            }
        });