
    document.addEventListener('DOMContentLoaded', function() {
      // Play button - navigate to flappy.html
      document.getElementById('play-button').addEventListener('click', function() {
        window.location.href = 'flappy.html';
      });
      
      // Quit button - close the window/tab
      document.getElementById('quit-button').addEventListener('click', function() {
        window.close();
      });
      
      // Create animated pipes for background effect
      const pipes = document.querySelectorAll('.pipe');
      pipes.forEach((pipe) => {
        const startLeft = parseInt(pipe.style.left);
        
        function animatePipe() {
          let left = startLeft;
          
          function movePipe() {
            left -= 0.5;
            if (left < -10) {
              left = 110;
            }
            pipe.style.left = `${left}%`;
            requestAnimationFrame(movePipe);
          }
          
          requestAnimationFrame(movePipe);
        }
        
        animatePipe();
      });
    });
