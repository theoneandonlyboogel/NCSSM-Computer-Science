let age = Number(prompt("How old are you?"));
/*simple conditionals, if they're 18+ they can, below they can't,
and if it doesn't match anything, invalid age*/
if (age >= 18) {console.log("You can vote!");}
else if (age < 18) {console.log("Soon enough, you can vote!");}
else {console.log("Invalid age");}