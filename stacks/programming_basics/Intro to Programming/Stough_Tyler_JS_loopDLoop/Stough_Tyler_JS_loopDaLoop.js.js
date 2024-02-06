/* Directions:

Create a new VS Code project called LastName_FirstName_LoopDLoop.
Create the following using what you learned and submit.

MVP Story:

A local fitness coach and a mechanical engineer are building an IoT device that pops out a piece of candy every time a runner reaches 2 miles 
on a treadmill but stops giving candy out at mile 6. You're tasked with building the loop functionality to know when to give a piece of candy 
and when to stop.

Step 1: Using comments in your VS Code, answer the following questions:

How do we know we need a loop here?
We're handing out candy multiple times until we hit 6 miles

What's the starting point of the loop?
The loop will start on mile 0

When should the loop stop?
The loop stops on mile 6

How will the loop know when to stop?
once our variable is equal to 6

What's incrementing for each iteration of the loop?
each mile ran will increase our variable by 1

What variables do we need?
Just one for the amount of miles ran*/

/* Bonus: create a new loop where the runner only gets candy every 2 miles AND if they're going faster than 5.5 miles per hour*/
var runSpd = 5.5
//Loop for how many miles that have been ran. It should increase by one each iteration.
for(var milesRan = 1; milesRan <= 6; milesRan ++){
    console.log("Mile " + milesRan)
    
    //This is the condition for whether the runner receives a piece of candy. It should deliver a piece every 2 miles
    //Additionally it should only give a piece of candy if the runSpd is at least 5.5
    if (milesRan%2 == 0 && runSpd >= 5.5) {
        console.log("Piece of Candy!")
    }
}

