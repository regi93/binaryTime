$(document).ready(function () {
    listing();
});

function listing() {
    
}

function zero(){

    $.ajax({
        type: 'PUT',
        url: '/api/v1/timecheck',
        data: {
            timeType: 'zero',
            timeStamp: new Date()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                }
            } 
    })
}
function plus(){
    $.ajax({
        type: 'POST',
        url: '/api/v1/timecheck',
        data: {
            timeType: 'plus',
            timeStamp: new Date()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                }
            } 
    })
}
function minus() {
    $.ajax({
        type: 'PUT',
        url: '/api/v1/timecheck',
        data: {
            timeType: 'minus',
            timeStamp: new Date()
            },
                success: function(response) {
                    if (response['result'] == 'success') {
                        alert(response['msg']);
                }
        }
    });
}


