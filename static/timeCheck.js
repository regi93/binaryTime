$(document).ready(function () {
    listing();
});
const mBtn = document.querySelector('.-btn');
mBtn.innerText = "start -Time"
function listing() {
    
}

function zero(){
    let nowDate = new Date().toLocaleDateString();
    let nowTime = new Date().toTimeString();

    $.ajax({
        type: 'POST',
        url: '/api/v1/timecheck',
        data: {
            timeType: 'zero',
            nowTime: now
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                }
            } 
    })
}
function plus() {
    
    let nowDate = new Date().toLocaleDateString();
    let nowTime = new Date().toTimeString();
    $.ajax({
        type: 'POST',
        url: '/api/v1/timecheck',
        data: {
            timeType: '+',
            nowDate: nowDate,
            nowTime : nowTime
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                }
            } 
    })
}
function minus() {
    let nowDate = new Date().toLocaleDateString();
    let nowTime = new Date().toTimeString();
    let status;
    if (mBtn.innerText = "start -Time") {
        status = 'start'
    } else {
        mBtn.innerText = 'end -Time';
        status = 'end'
    }
    $.ajax({
        type: 'POST',
        url: '/api/v1/timecheck',
        data: {
            timeType: '-',
            nowDate: nowDate,
            nowTime : nowTime,
            status : status 
            },
                success: function(response) {
                    if (response['result'] == 'success') {
                        alert(response['msg']);
                        console.log(status);
                }
        }
    });
    
    
}


