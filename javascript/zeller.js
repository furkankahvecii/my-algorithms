function updateDays() {
    var yearElement = document.getElementById('year');
    var monthElement = document.getElementById('month');
    var dayElement = document.getElementById('day');

    if (monthElement.value === 2) {
        if (parseInt(yearElement.value) % 4 !== 0) {
            dayElement.max = 28;
        } else {
            if (parseInt(yearElement.value) % 100 !== 0) {
                dayElement.max = 29;
            } else {
                if (parseInt(yearElement.value) % 400 !== 0) {
                    dayElement.max = 28;
                } else {
                    dayElement.max = 29;
                }
            }
        }
    } else if (monthElement.value === 4 || monthElement.value === 6 || monthElement.value === 9 ||
            monthElement.value === 11) {
        dayElement.max = 30;
    } else {
        dayElement.max = 31;
    }
}

function Zeller() {
    var D = parseInt(document.getElementById('day').value);
    var M = parseInt(document.getElementById('month').value);
    var Y = parseInt(document.getElementById('year').value);

    if (M < 3) {
        M = M + 12;
        Y = Y - 1;
    }

    var C = Math.floor(Y / 100);
    var K = Y - (100 * C);
    var S = Math.floor(2.6 * M - 5.39) + Math.floor(K / 4) + Math.floor(C / 4) + D + K - (2 * C);
    var ans = S - (7 * Math.floor(S / 7));
    var day = '';

    switch (ans) {
        case 0 : day = 'Sunday'; break;
        case 1 : day = 'Monday'; break;
        case 2 : day = 'Tuesday'; break;
        case 3 : day = 'Wednesday'; break;
        case 4 : day = 'Thursday'; break;
        case 5 : day = 'Friday'; break;
        case 6 : day = 'Saturday'; break;
    }

    document.getElementById('answer').innerHTML = 'It was a ' + day; // it is answer
}