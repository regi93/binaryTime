let Minus = 0, Plus = 0, Zero = 0, Rest = 0;

// loadChart();
function loadChart() {
        $.ajax({
            type: "GET",
            url: "/api/v1/chart",
            data: {},
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                    Plus = parseFloat(response['timeInfo'][0]);
                    Minus = parseFloat(response['timeInfo'][1]);
                    Zero = parseFloat(response['timeInfo'][2]);
                    Rest = parseFloat(response['timeInfo'][3]);
                    console.log(response);
                    drawChart();
                }}})
}

function getChart() {
    let date = $("#date").val()
    $.ajax({
        type: "POST",
        url: "/api/v1/chart",
        data: {date : date},
        success:function(response){
            if (response['result'] == 'success') {
                alert(response['msg']);
                Plus = parseFloat(response['timeInfo'][0]);
                Minus = parseFloat(response['timeInfo'][1]);
                Zero = parseFloat(response['timeInfo'][2]);
                Rest = parseFloat(response['timeInfo'][3]);
                console.log('POST요청값',response);

                drawChart();               
            }}})
}


    
function drawChart() {
    
    var ctx = document.getElementById('myChart').getContext('2d');
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Minus', 'Plus', 'Zero' , 'Rest of day'],
            datasets: [{
                label: '# of Votes',
                data: [Minus, Plus, Zero, Rest],

                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(236, 240, 241,0.5)'
                    
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(236, 240, 241, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });


 }