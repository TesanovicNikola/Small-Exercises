import numpy as np
import scipy.linalg as lg

def EigenValueVector(Matrix):
    # Using the Eig function out of scipy.linalg to determine the eigenvalues and eigenvectors
    Value, Vector = lg.eig(Matrix)
    print('The Eugenvalues: \n',Value)
    print('The EugenVectors: \n', Vector)

def MatrixMaker(R,C):
    entries = list(map(int, input().split()))       #spliting the entries by a spacebar
    matrix = np.array(entries).reshape(R, C)        #making a numpy array with  R and C as rows and columns
    return matrix                                   #returning the value of the matrix

if __name__ == '__main__':
    R = int(input("Enter the number of rows:\n"))
    C = int(input("Enter the number of columns:\n"))
    print("Enter the entries rowwise in a single line (separated by space): ")
    x=MatrixMaker(R,C)
    print('The input matrix is: \n', x)   #Printing the input matrix to make sure that the input is correct
    EigenValueVector(x)





