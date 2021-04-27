function animatePacman() {
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');

    var firstPosition = 100;
    var dir = -10;
    var pctOpen = 100;

    function drawPacman(position, pctOpen) {
        var foodPositions = 100;

        // Convert percent open to a float
        var fltOpen = pctOpen / 100;

        // Clear the canvas
        context.clearRect(0, 0, canvas.width, canvas.height);

        // An arc which stops at a specific percent to allow for the open mouth to be drawn
        context.beginPath();
        context.arc(position, 150, 100, (fltOpen * 0.2) * Math.PI, (2 - fltOpen * 0.2) * Math.PI);

        // The line leading back to the center and then closing the path to finish the open mouth
        context.lineTo(position, 100);
        context.closePath();

        // Fill pacman's head yellow
        context.fillStyle = '#FF0';
        context.fill();

        // Stroke pacman's border black
        context.strokeStyle = '#000';
        context.stroke();

        // A circle for the eye
        context.beginPath();
        context.arc(position, 100, 10, 0, 2 * Math.PI);
        context.fillStyle = '#000';
        context.fill();

        // Outline the eye
        context.strokeStyle = '#FFF';
        context.beginPath();

        // Create foods according to the position of pacman
        while (foodPositions < 1300) {
            if (position + 90 > foodPositions) {
                foodPositions += 100;

                continue;
            } else {
                context.arc(foodPositions, 100, 10, 0, 2 * Math.PI);
                context.fillStyle = '#000';
                context.fill();
                foodPositions += 100;
            }
        }

        context.stroke();
    }

    setInterval(function () {
        if (firstPosition < 1250) {
            drawPacman(firstPosition += 3, pctOpen += dir);
        }

        if (pctOpen % 100 === 0) {
            dir = -dir;
        }
    }, 100);
}