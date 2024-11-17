const magicBox = document.getElementById('magicBox');
const bpmInput = document.getElementById('bpmInput');
let intervalId = null;  // Placeholder for now, used later

// function to reveal box and give default colors
function revealBox() {
  magicBox.style.display = 'block';
  magicBox.style.backgroundColor = '#1a237e';
  magicBox.style.color = 'white';
}

// function to Hide the box
function hideBox() {
  magicBox.style.display = 'none';
  if (intervalId) {
    clearInterval(intervalId);  // stops flashing when hidden
  }
}

// function for changing color and generating a new random one
function changeColor() {
  const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
  magicBox.style.backgroundColor = randomColor;
}

// function to use the bpm input and start flashing
function startFlashing() {
  const bpm = parseInt(bpmInput.value);
  
  if (isNaN(bpm) || bpm <= 0) {
    alert('Please enter a valid BPM value!');
    return;
  }

  // clears the flashing
  if (intervalId) {
    clearInterval(intervalId);
  }

  // interval calculation for into seconds
  const interval = 60000 / bpm;

  // FLASH
  intervalId = setInterval(changeColor, interval);
}