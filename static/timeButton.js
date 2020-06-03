
const plusButton = document.querySelector(".plusButton");
const minusButton = document.querySelector(".minusButton");
const zeroButton = document.querySelector(".zeroButton");


console.log('timebutton.js 연동');
function zero(){
    $.ajax({
        type: "PUT",
        url: "/time",
        data: {
            startTime: new Date()
    },
        success:function(response){
            if (response['result'] == 'success') {
                alert(response['msg']);
                window.location.reload();
            }
        }
    })
};
function plus(){
    
};
function minus(){

};