#Creating a function that has all of the symbols within it and their probability weigh 
get_symbols <- function() {
  wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
  sample(wheel, size = 3, replace = TRUE, 
         prob = c(0.03, 0.03, 0.06, 0.1, 0.25, 0.01, 0.52))
}
#Scoring each roll
score <- function(symbols) {
  
#This makes it so Diamonds are used in the calculation for the expected value, if i treat it as a wildcard symbol, the expected value will be less
  diamonds <- sum(symbols == "DD")
  cherries <- sum(symbols == "C")
  
  #Identify case
  #Since diamonds are wild, out of the symbols one i will only select non diamond symbols
  #Matter for three of a kind and all bars
  slots <- symbols[symbols != "DD"]
  same <- length(unique(slots)) == 1
  bars <- slots %in% c("B", "BB", "BBB")
  
  #Prize assignment
  if (diamonds == 3) {
    prize <- 100
  } else if (same) {
    payouts <- c("7" = 80, "BBB" = 40, "BB" = 25,
                 "B" = 10, "C" = 10, "0" = 0)
    prize <- unname(payouts[slots[1]])
  } else if (all(bars)) {
    prize <- 5
  } else if (cherries > 0) {
    # diamonds count as cherries
    # so long as there is one real cherry
    prize <- c(0, 2, 5)[cherries + diamonds + 1]
  } else {
    prize <- 0
  }
  
  #If i get diamonds at the end, the prize is doubled, if there are 0 diamonds, then the prize remains the same, for each diamond its *2
  prize * (2 ^ diamonds)
}

#Creating the play function, which will combine everything in one
play <- function(){
  symbols <- get_symbols()
  prize <- score(symbols)
  attr(prize, "symbols") <- symbols
  symbols <- paste(symbols, collapse = "  ")
  result <- paste(symbols, prize, sep = "\nPrice:$")
  cat('\nRoll:',result)  
}
play()
#Now i will create a function that will allow me to insert a ammount of money and play the machine:
plays_till_broke <- function(entry) {
  cash <- entry
  n <- 0
  while (cash > 0) {
    symbols <- get_symbols()
    prize <- score(symbols)
    attr(prize, "symbols") <- symbols
    symbols <- paste(symbols, collapse = "  ")
    result <- paste(symbols, prize, sep = "\nPrice:$")
    cat('\nRoll:',result) 
    cash <- cash + prize - 1
    cat('\nRemaining credit $',cash, '\n')
    n <- n + 1
  }
  cat('\nNumber of total Rolls:', n)
}

#The program ends it, with this i can roll how much i want.
plays_till_broke(1)


#Now i want to calculate the expected value of the machine, this tells how much does the machine returns on a 1 dollar input
#To calculate the expected value, i need the probability of each possible combination and the prize of the roll

#The first task is to create every possible roll, for that i will use expand.grid command:
wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
combos <- expand.grid(wheel,wheel, wheel, stringsAsFactors = F)
#Creating the probabilities, same as in the get_function table
prob <- c("DD" = 0.03, "7" = 0.03, "BBB" = 0.06, 
          "BB" = 0.1, "B" = 0.25, "C" = 0.01, "0" = 0.52)
#Now to add all the probabilities in the combos table:
combos$prob1 <- prob[combos$Var1]
combos$prob2 <- prob[combos$Var2]
combos$prob3 <- prob[combos$Var3]
#The total probability is the product of all probs:
combos$TotalProb <- combos$prob1 * combos$prob2 * combos$prob3

#Adding the prize for each possible combination
combos$prize <- NA
for (i in 1:nrow(combos)) {
  symbols <- c(combos[i, 1], combos[i, 2], combos[i, 3])
  combos$prize[i] <- score(symbols)
}

#And finally to calculate the expected value i simply have to sum the product of the probabilities and prizes:
ExpectedValue <- sum(combos$TotalProb * combos$prize)
ExpectedValue
