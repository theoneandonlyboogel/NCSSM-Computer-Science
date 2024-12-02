/*A little complicated, basically just converts the float returned
by Math.random to an integer we can actually use*/
const randInt = Math.floor(Math.random() * (10 - 1 + 1)) + 1;

//loops continually until the user guesses the number in randInt
while (true) {
    let userInput = Number(prompt("Enter a number"))
    if (userInput === randInt) {
        console.log("Got it");
        //breaks out of loop if the number is right
        break;
    } else if (userInput < randInt) {
        //continue to go, tells the user if they're high or low
        console.log("Too low");
    } else if (userInput > randInt) {
        console.log("Too high")
    } else {
        console.log("Invalid Number");
    } 
}

