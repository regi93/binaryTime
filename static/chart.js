var ctx = document.getElementById('myChart').getContext('2d');
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Minus', 'Plus', 'Zero' , 'Rest of day'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3 , 6],
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

