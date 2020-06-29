let Minus = 0, Plus = 0, Zero = 0, Rest = 0;
const chartList = document.querySelector("chartList")

function loadChartList() {
        $.ajax({
            type: "GET",
            url: "/api/v1/chart",
            data: {},
            success:function(response){
                if (response['result'] == 'success') {
                    response["dateList"].forEach(element => {
                        $(".chartList").append(
                            `<button width="5%" type="button" class = "btn btn-primary" onclick = "getChart('${element}')">${element}</button>`
                        )
                    });
                }}})
}

function getChart(date) {
    $.ajax({
        type: "POST",
        url: "/api/v1/chart",
        data: {date : date },
        success:function(response){
            if (response['result'] == 'success') {
                Plus = parseFloat(response['timeInfo'][0]);
                Minus = parseFloat(response['timeInfo'][1]);
                Zero = parseFloat(response['timeInfo'][2]);
                Rest = parseFloat(response['timeInfo'][3]);

                drawChart(date);               
            }}})
}


    
function drawChart(date) {
    
    var ctx = document.getElementById('myChart').getContext('2d');
    // var ctx = document.getElementById('myChart');
    $('#myChart').empty();
    let chartInfo = document.getElementById("chartInfo")
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Minus time', 'Plus time', 'Zero time' , '기록되지 않은 시간'],
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
chartInfo.innerHTML = `${date}`

 }

loadChartList();

