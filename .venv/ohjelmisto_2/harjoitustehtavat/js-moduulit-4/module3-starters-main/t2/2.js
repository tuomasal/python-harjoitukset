 let lista = document.querySelector('#target')
 let l1 = document.createElement("li");
l1.textContent = "First item"
lista.appendChild(l1);

let l2 = document.createElement("li");
l2.textContent = "Second item"
l2.setAttribute("class", "my-item")
lista.appendChild(l2);

let l3 = document.createElement("li");
l3.textContent = "Third item"
lista.appendChild(l3);