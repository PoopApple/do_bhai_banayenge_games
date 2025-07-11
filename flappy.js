let birdSpeed = 3, gravity = 0.2;
let birdElement = document.querySelector('.bird');
let birdImage = document.getElementById('bird-1');
let pointSound = new Audio('sounds effect/point.mp3');
let dieSound = new Audio('sounds effect/die.mp3');

let birdBoundingRect = birdElement.getBoundingClientRect(); // position dega 


let backgroundBoundingRect = document.querySelector('.background').getBoundingClientRect(); // backgorund ko bhi position de dega 

let scoreDisplay = document.querySelector('.score_val');
let messageDisplay = document.querySelector('.message');
let scoreTitleDisplay = document.querySelector('.score_title');

let gameStatus = 'startgame';  
birdImage.style.display = 'none';
messageDisplay.classList.add('messageStyle');
 
document.addEventListener('keydown', (e) => { // if pressed enter the game will start and usse phle game will not be played
    if (e.key === 'Enter' && gameStatus !== 'Play') {
        document.querySelectorAll('.pipe_sprite').forEach((pipe) => {
            pipe.remove();
        });
        birdImage.style.display = 'block';
        birdElement.style.top = '40vh';
        gameStatus = 'Play';
        messageDisplay.innerHTML = '';
        scoreTitleDisplay.innerHTML = 'Score: ';
        scoreDisplay.innerHTML = '0';
        messageDisplay.classList.remove('messageStyle');
        startGame();
    }
});

function startGame() {
    function movePipes() {   
        if (gameStatus !== 'Play') return;

        let pipes = document.querySelectorAll('.pipe_sprite');
        pipes.forEach((pipeElement) => {
            let pipeRect = pipeElement.getBoundingClientRect();
            birdBoundingRect = birdElement.getBoundingClientRect();

            if (pipeRect.right <= 0) {
                pipeElement.remove();
            } else {
                // Check if the bird collides with the pipe
                if (
                    birdBoundingRect.left < pipeRect.left + pipeRect.width &&
                    birdBoundingRect.left + birdBoundingRect.width > pipeRect.left &&
                    birdBoundingRect.top < pipeRect.top + pipeRect.height &&
                    birdBoundingRect.top + birdBoundingRect.height > pipeRect.top
                ) {
                    gameStatus = 'End';
                    messageDisplay.innerHTML = 'Game Over'.fontcolor('red') + '<br>Press Enter To Restart';
                    messageDisplay.classList.add('messageStyle');
                    birdImage.style.display = 'none';
                    dieSound.play();
                    return;
                } else {
                    if (pipeRect.right < birdBoundingRect.left && pipeRect.right + birdSpeed >= birdBoundingRect.left && pipeElement.increase_score === '1') {
                        scoreDisplay.innerHTML = +scoreDisplay.innerHTML + 1;
                        pointSound.play();
                    }
                    pipeElement.style.left = pipeRect.left - birdSpeed + 'px';
                }
            }
        });
        requestAnimationFrame(movePipes);
    }
    requestAnimationFrame(movePipes);

    let birdVerticalSpeed = 0;
    function applyGravity() {
        if (gameStatus !== 'Play') return;

        birdVerticalSpeed += gravity;
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowUp' || e.key === ' ') {
                birdImage.src = 'images/fapy.png';
                birdVerticalSpeed = -7.6;
            }
        });

        document.addEventListener('keyup', (e) => {
            if (e.key === 'ArrowUp' || e.key === ' ') {
                birdImage.src = 'images/fapy.png';
            }
        });

        if (birdBoundingRect.top <= 0 || birdBoundingRect.bottom >= backgroundBoundingRect.bottom) {
            gameStatus = 'End';
            messageDisplay.style.left = '28vw';
            window.location.reload();
            messageDisplay.classList.remove('messageStyle');
            return;
        }
        birdElement.style.top = birdBoundingRect.top + birdVerticalSpeed + 'px';
        birdBoundingRect = birdElement.getBoundingClientRect();
        requestAnimationFrame(applyGravity);
    }
    requestAnimationFrame(applyGravity);
    let pipeDistance = 30;
    let pipeGap = 40;

    function generatePipes() {
        if (gameStatus !== 'Play') return;

        if (pipeDistance > 115) {
            pipeDistance = 0;

            let randomPipePosition = Math.floor(Math.random() * 43) + 8;
            let topPipe = document.createElement('div');
            topPipe.className = 'pipe_sprite';
            topPipe.style.top = randomPipePosition - 70 + 'vh';
            topPipe.style.left = '100vw';

            document.body.appendChild(topPipe);
            let bottomPipe = document.createElement('div');
            bottomPipe.className = 'pipe_sprite';
            bottomPipe.style.top = randomPipePosition + pipeGap + 'vh';
            bottomPipe.style.left = '100vw';
            bottomPipe.increase_score = '1';

            document.body.appendChild(bottomPipe);
        }
        pipeDistance++;
        requestAnimationFrame(generatePipes);
    }
    requestAnimationFrame(generatePipes);
}
