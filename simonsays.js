let level = 0;
let startgame = false;
let box = ["yellow", "green", "red", "blue"];
let user = [];
let gamesq = [];
let startscore = 0
let body = document.querySelector("body");
let h2 = document.querySelector("h2");
let btns = document.querySelectorAll(".btn"); 

function input() {
  body.addEventListener("keypress", function () {
    if (startgame === false) {
      console.log("Key Pressed. Game Started");
      startgame = true;
      nextSequence(); 
    } // done
  });

  clickinput();
}

function clickinput() {
  for (let btn of btns) {
    btn.addEventListener("click", function () {
      if (startgame === true) {
        userflash(btn); // done
       playSound();
        user.push(btn.id);
        console.log("User:", user);
        checkbts(user.length - 1);
      }
    });
  }
}

function checkbts(idx) { 
  if (user[idx] === gamesq[idx]) {
    if (user.length === gamesq.length) { // 
      console.log("successful");
       display();
      setTimeout(() => {
        nextSequence();
      }, 500);
    }
  } else {
    console.log(" unsuccessful");
    h2.innerText = "Game Over. Press any key to Restart";
    body.style.backgroundColor = "#FF5722";
    setTimeout(() => {
      body.style.backgroundColor = "#011F3F";
    }, 300);
    resetGame();
  }
}

function nextSequence() { 
  user = [];
  level++;
  h2.innerText = `Level ${level}`;
  let coloridx = Math.floor(Math.random() * 4); 
  let color = box[coloridx];
  let btn = document.getElementById(color);

  flashup(btn); 
  gamecollection(btn);
  
} 

function gamecollection(b) {
  gamesq.push(b.id);
  console.log("Game:", gamesq);
}

function flashup(bt) {
  bt.classList.add("flash");
  setTimeout(() => {
    bt.classList.remove("flash");
  }, 300);
} // done 

function userflash(btn) {
  btn.classList.add("flash");
  setTimeout(() => {
    btn.classList.remove("flash");
  }, 300);
} // done

function resetGame() {
  level = 0;
  user = [];
  gamesq = [];
  startgame = false;
  startscore = 0;
  score.innerText = 0
}
function display(){
    startscore +=10;
    let score = document.querySelector("#score")
    score.innerText = startscore;
}

function playSound() {
  let sound = new Audio("mouse-click-290204.mp3");
  sound.play();
}

input();