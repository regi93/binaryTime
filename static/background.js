const body = document.querySelector("body");
const image = new Image();
// '/../../foo.bar'
image.src = `/../static/images/4.jpg`;
image.classList.add("bgImage");
body.appendChild(image);
