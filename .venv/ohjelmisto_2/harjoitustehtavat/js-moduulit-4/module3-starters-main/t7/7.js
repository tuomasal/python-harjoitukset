let target = document.querySelector("#target")
let trigger = document.querySelector("#trigger")

trigger.addEventListener("mouseenter", (e) => {
    target.setAttribute("src", "img/picB.jpg")
})

trigger.addEventListener("mouseleave", (e) => {
    target.setAttribute("src", "img/picA.jpg")
})
