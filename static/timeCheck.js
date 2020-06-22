
// window.onload;

const Pbtn = document.querySelector('#Pbtn'),
Mbtn = document.querySelector('#Mbtn');

let plusStatus = 'close',
minusStatus = 'close'; // open or close


// function articleDel(timeColor, cnt) {
//     $.ajax({
//         type: "DEL",
//         url: "/api/v1/timelist/del",
//         data: {
//             cnt: cnt,
//     },
//         success:function(response){
//             if (response['result'] == 'success') {
//                 alert(response['msg']);
//             }
//         }
//     })
// }
    

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
            if (response['result'] == 'success') {
                alert(response['msg']);
                let timeList = response['timeList'];
                let cnt = 1;
                let timeColor = '';
                let article = '';
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
                    // if (element.endTime == undefined) {
                    //     if (element.timeType == '+ Start') {
                    //         plusStatus = 'open';
                    //     } else {
                    //         minusStatus = 'close';
                    //     }
                    // }
                    $('.timeline').append(`<input type="checkbox" class='${timeColor}' id="event-${cnt}"/>
                        <section>
                        <label for="event-${cnt}">
                            <span class="date" id = 'time${cnt}'>${element.startTime + ' ~ ' + element.endTime}</span>
                            <span class="${timeColor}"> ${article} </span>
                        </label>
                        <p>${"지속시간 : " + element.duration}
                        <br>
                        <input type="text" class = "aInput${cnt}" >
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