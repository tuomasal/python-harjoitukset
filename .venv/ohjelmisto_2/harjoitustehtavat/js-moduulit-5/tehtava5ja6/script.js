
"use strict";
const jokeForm = document.querySelector("#joke-form");
jokeForm.addEventListener("submit", async function (evt) {
    evt.preventDefault();
    const value_from_input = document.querySelector("#query").value;
    const response = await fetch(
        `https://api.chucknorris.io/jokes/search?query=${value_from_input}`
    );
    const jsonData = await response.json();
    const results = document.querySelector("#results");
    results.innerHTML = "";
    jsonData.result.forEach(joke => {
        results.innerHTML += `
            <article>
                <p>${joke.value}</p>
            </article>
        `;
    });
});

