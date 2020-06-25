const clockContainer = document.querySelector(".js-clock"),
    clockTitle = clockContainer.querySelector("h1");

function setClock(){ 
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();    
    clockContainer.innerHTML=`${h}:${m}:${s}`
    setTimeout(setClock, 500);    

}




function getTime() {
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours();
    var second = date.getSeconds();
    
    clockTitle.innerText = `${String(hours).length > 1 ? hours : `0${hours}`}:${
        String(minutes).length > 1  ? minutes : `0${minutes}`}:${
            String(second).length > 1 ? second : `0${ second }`}`;
}

function init() {
    getTime();
    setInterval(getTime, 500);
}
init();




//need two argument setInterval(fn , 1000) 1000 = 1초 간격으로 fn함수를 반복실행한다.  fn뒤에 ()안붙인다.