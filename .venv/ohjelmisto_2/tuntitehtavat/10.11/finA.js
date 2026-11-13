async function fetchData() {
    try {
        const response = await fetch("https://pokeapi.co/api/v2/pokemon")
        if(response.ok){
            const response_data = await response.json()
            return response_data
        } else {
            throw new Error(`HTTP-virhe! Tilakoodi: ${response.status}`)
        }
    } catch (error) {
        console.log('Virhe datan hakemisessa ${error}')
    }
}

async function createPokemonView() {
    const pokemonData = await fetchData()
    const pokemonDiv = document.querySelector("#poke-content")
    for (let pokemon of pokemonData.results){
        console.log(pokemon)
        let pokemonText = document.createElement("p");
        pokemonText.textContent = pokemon.name;
        pokemonDiv.appendChild(pokemonText);
    }
}

createPokemonView()