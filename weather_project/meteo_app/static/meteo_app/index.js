let ctx = document.getElementById('myChart').getContext('2d');
let chart = new Chart(ctx, {
    type: 'line',

    data: {
        labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль'],
        datasets: [
        { // График синего цвета
            label: 'График 2',
            backgroundColor: 'transparent',
            borderColor: 'blue',
            data: [5, 3, 10, 30, 40, 20, 5]
        }],
    },
});