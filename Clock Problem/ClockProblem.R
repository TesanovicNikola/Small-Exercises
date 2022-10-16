#Given four digits, count how many valid times can be displayed of a digital clock (in 24-hour format) using those digits. The earliest
#time is 00:00 and the latest time is 23:59. Use 4 parameters that can be in range of [0...9]. If there are no correct times, return 0.

#Example, A=1, B=8, C=3, D=4, the return is 6, 12:38, 13:28, 18:23, 21:38 and 23:18


is_time <- function(A,B,C,D){
  
  library(gtools)
  library(glue)
  
  #Sampling all permutations
  all_possibilities <- permutations(4,4,as.vector(c(A,B,C,D)), repeats.allowed = FALSE, set = FALSE)
  colnames(all_possibilities) <- c('A','B','C','D')
  all_possibilities <- unique.data.frame(all_possibilities)
  all_possibilities <- as.data.frame(all_possibilities)
  
  #Doing additional filtering, now i have every single possibility. I will filter out all the ones that are from the start no possible
  #Digital clock first 2 numbers are hours, last two are minutes. So for hours the first number can be a 0,1,2 while the second one can
  #can be any number from 0 to 9
  
  #Maximum for the first number in hours is 2, everything beyond that is not considered.
  all_possibilities <- all_possibilities[all_possibilities[1:nrow(all_possibilities),1] < 3,]

  #Covering the case when there is no single right input
  if(nrow(all_possibilities) > 0){
  #Maximum for the first number in minutes is 6, everything beyond that is not considered.
  all_possibilities <- all_possibilities[all_possibilities[1:nrow(all_possibilities),3] < 7,]
 #The remaining cases will be filtered in a loop
  
  
  valid_times <- c()
  
  for (i in 1:nrow(all_possibilities)) {
    
    if (all_possibilities[i,1] == 2 && all_possibilities[i,2] < 5 && sum(all_possibilities[i,] == 0) < 4) {
      
      #Filtering out the possible date for this case
      temp_glue <- as.integer(glue_collapse(all_possibilities[i,]))
      time <- substr(as.POSIXct(sprintf("%04.0f", temp_glue), format='%H%M'), 12, 16)
      valid_times <- rbind(valid_times,data.frame(time))
      
      
    } else if (all_possibilities[i,1] < 2 && sum(all_possibilities[i,] == 0) < 4) {
      
      temp_glue <- as.integer(glue_collapse(all_possibilities[i,]))
      time <- substr(as.POSIXct(sprintf("%04.0f", temp_glue), format='%H%M'), 12, 16)
      valid_times <- rbind(valid_times,data.frame(time))
      
      
    } else if(sum(all_possibilities[i,] == 0) == 4){
      
      #This case covers when the input is 0,0,0,0
      
      time <- "00:00"
      valid_times <- rbind(valid_times,data.frame(time))
      
      
    }
    
    
  }
  
  if (!is.na(valid_times[1,1])) {
    
    cat("Number of valid times is:",nrow(valid_times),"\n")
    print.data.frame(valid_times)
    
  } else {
    
    cat("No valid times found 0")
    
  }
  
  } else {
  
    cat("No valid times found 0")
}
  
}


k <- is_time(6,2,4,7)
k <- is_time(1,8,3,2)
k <- is_time(2,3,3,2)
k <- is_time(9,9,9,9)
k <- is_time(0,0,0,4)
k <- is_time(0,0,0,0)


