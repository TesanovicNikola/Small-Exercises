import numpy as np

#Creating the Profit function
def max_profit(prices: list, days: int) -> int:
 
    profit = 0
 
    for i in range(1, days):
 
        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:
 
            # difference added to 'profit'
            profit += prices[i] - prices[i-1]
 
    return profit
 
# Main code
if __name__ == '__main__':
 
    # stock prices on consecutive days generated using rayleigh distribution
    rng = np.random.default_rng()
    # generating a random generator with the rayleign distribution, while using random.choice to get the scale number for the distribution
    k = rng.rayleigh(np.random.choice(10, 1), 100000)
    # Calling the profit function to calculate the max profit
    profit = max_profit(k, len(k))
    print(profit)
 

