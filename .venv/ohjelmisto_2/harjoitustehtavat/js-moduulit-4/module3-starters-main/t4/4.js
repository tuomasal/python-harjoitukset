'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

let lista = document.querySelector('#target');
for (let i = 0; i < students.length; i++) {
  let nimi = students[i].name
  let id = students[i].id
  let optio = document.createElement("option")
  optio.setAttribute("value", id)
  optio.textContent = nimi
  lista.appendChild(optio);
}