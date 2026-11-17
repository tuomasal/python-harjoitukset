'use strict';
const names = ['John', 'Paul', 'Jones'];

let htmlStr = ""
for (let i = 0; i < names.length; i++) {
    let name = names[i]
    htmlStr = htmlStr + "<li>" + name + "</li>"
}
document.querySelector('#target').innerHTML = htmlStr