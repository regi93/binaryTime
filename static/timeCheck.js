
// window.onload;

const Pbtn = document.querySelector('#Pbtn'),
    Mbtn = document.querySelector('#Mbtn');




function plus() {
    if (Pbtn.innerText == "Start PlusTime") {
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
                
                timeList.forEach(element => {
                    if (element.timeType == '+ Start') {
                        timeColor = 'blueList';
                    } else {
                        timeColor= 'redList';
                    };
                    $('.timeline').append(`<input type="checkbox" class='${timeColor}' id="event-${cnt}"/>
                        <section>
                        <label for="event-${cnt}">
                            <span class="date">${element.startTime + ' ~ ' + element.endTime}</span>
                            <span class="${timeColor}">Today's event ${cnt}</span>
                        </label>
                        <p>${element.timeType + "지속시간 : " + element.duration}
                        </p>
                        </section>`);
                    cnt += 1;
                });
                

            }
        }
    })
 }
loadlist();