def PascalTriangle(rows):
    list = []
    for n in range(rows):
        list.append([])
        list[n].append(1)
        for m in range(1,n):
            list[n].append(list[n-1][m-1]+list[n-1][m])
        if(rows != 0):
            list[n].append(1)
    for n in range(rows):
        print(' ' * (rows - n), end = ' ', sep = ' ')
        for m in range(0, n+1):
            print('{0:5}'.format(list[n][m]), end=" ", sep=" ")
        print()

if __name__ == '__main__':
    PascalTriangle(int(input("Enter the number of rows: ")))



