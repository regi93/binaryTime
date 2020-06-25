const ball = document.querySelector(".ball"),
    shadow = document.querySelector(".shadow"),
    Pbtn = document.querySelector('#Pbtn'),
    Mbtn = document.querySelector('#Mbtn')
    TIMER = document.getElementById('timer')

let plusStatus = 'close',
    minusStatus = 'close',
    startTime;

function articleDel(timeColor, cnt) {
let time = document.querySelector(`#time${cnt}`).textContent;
    $.ajax({
        type: "DEL",
        url: "/api/v1/timelist",
        data: {
            timeType : timeColor,
            time : time,
    },
        success:function(response){
            if (response['result'] == 'success') {
                alert(response['msg']);
                loadlist();
            }
        }
    })
}


timer = setInterval(function(){
    var today = new Date();
    var h = today.getHours() 
    var sh = parseInt(startTime.split(':')[0]); 
    var m = today.getMinutes() 
    var sm = parseInt(startTime.split(':')[1]);
    var s = today.getSeconds();
    var ss = parseInt(startTime.split(':')[2]);
    console.log("@@@@")
    let stime = sh*3600 +  sm*60 + ss
    let ntime = h*3600 +  m*60 + s

    if (stime > ntime) {
        
    }
    ntime -= stime
    console.log(h,m,s)
    h = Math.floor(ntime/3600);
    console.log(ntime)
    m = Math.floor((ntime-h*3600)/60)
    console.log(ntime)
    s = ntime - h*3600 - m*60
    console.log(ntime)
    TIMER.innerHTML = `${h > 10 ? h : `0${h}`}:${m > 10 ? m : `0${m}`}:${s > 10 ? s : `0${ s }`}`;
}, 1000);

function articleInput( timeColor, cnt) {
    let article = document.querySelector(`.aInput${cnt}`).value;
    let time = document.querySelector(`#time${cnt}`).textContent;
    $.ajax({
        type: "POST",
        url: "/api/v1/timelist",
        data: {
            timeType : timeColor,
            time : time,
            article: article,
    },
        success:function(response){
            if (response['result'] == 'success') {
                alert(response['msg']);
                loadlist();

            }
        }
    })
}
function plus() {
    ball.id = 'blue'
    shadow.id = 'blue'
        
    if (Pbtn.innerText == "Start PlusTime") {
        plusStatus = 'open';
        Pbtn.innerText = 'End PlusTime';
        $.ajax({
            type: "POST",
            url: "/api/v1/plustime",
            data: {
                Time: new Date(),
                timeType : '+ Start'
                },
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                }
            }
        })
        
    } else {
        Pbtn.innerText = 'Start PlusTime';
        plusStatus = 'close';
        $.ajax({
            type: "POST",
            url: "/api/v1/plustime",
            data: {
                Time : new Date(),
                timeType : '+ End'
        },
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                    loadlist();

                }
            }
        })
    }
}

function minus() {
    ball.id = 'red'
    shadow.id = 'red'
    if (Mbtn.innerText == "Start MinusTime") {
        Mbtn.innerText = 'End MinusTime';
        minusStatus = 'open';
        $.ajax({
            type: "POST",
            url: "/api/v1/minustime",
            data: {
                Time: new Date(),
                timeType : '- Start'
                },
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                }
            }
        })
        
    } else {
        Mbtn.innerText = 'Start MinusTime';
        minusStatus = 'close';
        $.ajax({
            type: "POST",
            url: "/api/v1/minustime",
            data: {
                Time : new Date(),
                timeType : '- End'
        },
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                    loadlist();

                }
            }
        })
    }
}
    

function loadlist() {
    $.ajax({
        type: "GET",
        url: "/api/v1/timelist",
        data: {},
        success: function (response) {
            if (response['status'] == "plus") {
                startTime = response['startTime']
                Mbtn.innerText = 'Start MinusTime';
                Pbtn.innerText = 'End PlusTime';
                ball.id = 'blue'
                shadow.id = 'blue'
                timer();
            } else if (response['status'] == 'minus') {
                startTime = response['startTime']
                Mbtn.innerText = 'End MinusTime';
                Pbtn.innerText = 'Start PlusTime';
                ball.id = 'red'
                shadow.id = 'red'
                timer();

            }

            if (response['result'] == 'success') {
                alert(response['msg']);
                let timeList = response['timeList'];
                let cnt = 1;
                let timeColor = '';
                let article = '';
                $('.timeline').empty();
                timeList.forEach(element => {

                    if (element.timeType == '+ Start') {
                        timeColor = 'blueList';
                    } else {
                        timeColor= 'redList';
                    };
                    if (element.article == undefined) {
                        article = "Today's event" + cnt;
                    } else {
                        article = element.article;
                    }

                    $('.timeline').append(`<input type="checkbox" class='${timeColor}' id="event-${cnt}"/>
                        <section>
                        <label for="event-${cnt}">
                            <span class="date" id = 'time${cnt}'>${element.startTime + ' ~ ' + element.endTime}</span>
                            <span class="${timeColor}"> ${article} </span>
                        </label>
                        <p>${"지속시간 : " + element.duration}
                        <br>
                        <input style = "color : white;" placeholder = "이벤트 입력"  type="text" class = "aInput${cnt}" >
                        <br>
                        <button type = 'submit' onclick="articleInput( '${timeColor}', '${cnt}')">입력</button>
                        <button type = 'submit' onclick="articleDel( '${timeColor}', '${cnt}')">삭제</button>
                        </p>
                        </section>`);
                        cnt += 1;
                });
            }
        }
    })
}
 

loadlist();