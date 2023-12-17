import numpy as np

def MatrixMaker(R,C):
    entries = list(map(int, input().split()))       #spliting the entries by a spacebar
    if R == 1 and C == 1:                           #in case of entering only one element
        matrix = np.array(entries)
    else:
        matrix = np.array(entries).reshape(R, C)        #making a numpy array with  R and C as rows and columns
    return matrix                                       #returning the value of the matrix

def MatrixAddition(x,y):
    return x+y                       #Adding the two matricies

def MatrixMultiplication(x,y):
    return np.matmul(x,y)                           #Instead of using a for loop, I am using the matmul function out of Numpy


if __name__ == '__main__':
    case = int(input("Choose whether you want to add or multiply matrices:\n Type 1 for addition \n Type 2 for multiplication\n"))

    if case == 1:           #Addition

        # First Matrix
        R1 = int(input("Enter the number of rows for the first matrix:\n"))
        C1 = int(input("Enter the number of columns for the first matrix:\n"))
        print("Enter the entries rowwise in a single line (separated by space): ")
        x = MatrixMaker(R1, C1)
        print('The first input matrix is: \n', x)  # Printing the input matrix to make sure that the input is correct

        # Second Matrix
        R2 = int(input("\nEnter the number of rows:\n"))
        C2 = int(input("Enter the number of columns:\n"))
        print("Enter the entries rowwise in a single line (separated by space): ")
        y = MatrixMaker(R2, C2)
        print('The second input matrix is: \n', y)  # Printing the input matrix to make sure that the input is correct
        if R1 == R2 and C1 == C2:                   # To sum the matrices, the dimensions have to be the same (at least for this project that is a must)
            addition = MatrixAddition(x,y)
            print('\nThe result of the addition is: \n', addition)
        else:
            print('\nThe matrix dimensions are wrong. To add matrices they have to have the same dimension. \nPlease try again.\n')


    if case == 2:            #Multiplication

        #First Matrix
        R1 = int(input("Enter the number of rows for the first matrix:\n"))
        C1 = int(input("Enter the number of columns for the first matrix:\n"))
        print("Enter the entries rowwise in a single line (separated by space): ")
        x = MatrixMaker(R1, C1)
        print('The first input matrix is: \n',x)  # Printing the input matrix to make sure that the input is correct

        #Second Matrix
        R2 = int(input("\nEnter the number of rows:\n"))
        C2 = int(input("Enter the number of columns:\n"))
        print("Enter the entries rowwise in a single line (separated by space): ")
        y = MatrixMaker(R2, C2)
        print('The second input matrix is: \n', y)  # Printing the input matrix to make sure that the input is correct

        if C1 == R2:           #The condition to multiply matricies
            multiplication = MatrixMultiplication(x,y)
            print('\nThe result of the multiplication is: \n', multiplication)
        else:
            print('\nInvalid input. To multiply matrices, the number of columns in the first matrix must have the same number as the number of rows in the second matrix. \nPlease try again.\n')

    else:
        print('Invalid input, please try again\n')