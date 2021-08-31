
// get html tag with costs
let costs = document.querySelector(".s_my_costs").innerHTML;

//get html tag budget
let budget = document.querySelector(".s_my_budget").innerHTML;

// tag with warning message
let warningDiv = document.querySelector(".warning");


costs = parseFloat(costs)

budget = parseFloat(budget)

if (costs > budget){

        warningDiv.style.display = "block"
}


