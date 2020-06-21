
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
                }
            }
        })
    }
}