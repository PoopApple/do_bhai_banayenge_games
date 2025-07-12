 const leaderboardBtn = document.getElementById('leaderboard-btn');
    const leaderboardModal = document.getElementById('leaderboard-modal');
    const closeLeaderboard = document.getElementById('close-leaderboard');
    const quitBtn = document.getElementById('quit-btn');

    leaderboardBtn.addEventListener('click', () => {
      leaderboardModal.classList.remove('hidden');
    });
    
    closeLeaderboard.addEventListener('click', () => {
      leaderboardModal.classList.add('hidden');
    });
    quitBtn.addEventListener('click', () => {
      if (confirm("Are you sure you want to quit?")) {
        window.close();
       
        setTimeout(() => {
          window.location.href = "about:blank";
        }, 300);
      }
    });
    leaderboardModal.addEventListener('click', (e) => {
      if (e.target === leaderboardModal) {
        leaderboardModal.classList.add('hidden');
      }
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !leaderboardModal.classList.contains('hidden')) {
        leaderboardModal.classList.add('hidden');
      }
    });
