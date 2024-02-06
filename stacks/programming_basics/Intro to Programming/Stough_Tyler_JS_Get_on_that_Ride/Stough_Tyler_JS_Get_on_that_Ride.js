// variables for minimum requirements to ride the roller coaster
// creating variables assignment
var min_age = 10
var min_height = 42

/*get on that ride assignment
If the rider's height is greater than or equal to 42, the console.log should say "Get on that ride, kiddo!". 
Otherwise, console.log should say "Sorry kiddo. Maybe next year."*/

if (min_height == 42) {
    console.log("Get on that ride, kiddo!")
}
else console.log("Sorry kiddo. Maybe next year.")

/*stretchFeature1
Adjust the conditional statement to require both height (>=42 inches) and age (>=10 years old).*/

if (min_height >= 42 && min_age >=10){ // && is the and operator in js
    console.log("Get on that ride, kiddo!")
}

else console.log("Sorry kiddo. Maybe next year.")

/*stretchFeature2
Adjust the conditional statement to require that either the height requirement (>=42 inches) or the age requirement (>=10 years old) 
must be met in order for the console.log to say "Get on that ride, kiddo!".*/

if (min_height >= 42 || min_age >= 10) { // || is the or operator in js
    console.log("Get on that ride, kiddo!")
}

else console.log("Sorry kiddo. Maybe next year.")
