document.addEventListener("DOMContentLoaded", function () {
    var chartElement = document.getElementById('monthly-document-requests-chart');
    var ctx = chartElement.getContext('2d');

    var labels = chartElement.dataset.labels.split(',');
    var data = chartElement.dataset.data.split(',').map(Number);

    var chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Monthly Document Requests',
          data: data,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
});
