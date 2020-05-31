const clockContainer = document.querySelector(".clock"),
    clockTitle = clockContainer.querySelector("h1");

function getTime() {
    const date = new Date();
    let minutes = date.getMinutes();
    let hours = date.getHours();
    let second = date.getSeconds();
    clockTitle.innerText = `${hours > 10 ? hours : `0${hours}`}:${
        minutes > 10 ? minutes : `0${minutes}`}:${
        second > 10 ? second : `0${ second }`}`;
}

function init() {
    getTime();
    setInterval(getTime, 500);
}
init();