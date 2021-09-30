#Row Wise Sum
"""
For a given two-dimensional integer array/list of size (N x M),
find and print the sum of each of the row elements in a single line, separated by a single space.

Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output Format :
For each test case, print the sum of every ith row elements in a single line separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1:
1
4 2
1 2
3 4
5 6
7 8
Sample Output 1:
3 7 11 15

Sample Input 2:
2
2 5
4 5 3 2 6
7 5 3 8 9
4 4
1 2 3 4
9 8 7 6
3 4 5 6
-1 1 -10 5
Sample Output 2:
20 32
10 30 18 -5

Solution :

str = input().split()
n, m = int(str[0]), int(str[1])
b = input().split()
arr = [[int(b[m * i + j]) for j in range(m)] for i in range(n)]

newArr = []
for row in arr:
    sum = 0
    for ele in row:
        sum += ele
    newArr.append(sum)

for ele in newArr:
    print(ele, end=" ")


#Largest Row or Column
"""
For a given two-dimensional integer array/list of size (N x M), 
you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first.
And if ith row and jth column has the same largest sum, consider the ith row as answer

Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1 :
1
2 2
1 1
1 1
Sample Output 1 :
row 0 2

Sample Input 2 :
2
3 3
3 6 9
1 4 7
2 8 9
4 2
1 2
90 100
3 40
-10 200
Sample Output 2 :
column 2 25
column 1 342

Solution :

def largestRowCol(arr):
    rows = len(arr)
    cols = len(arr[0])

    sumRow = [0] * rows
    sumCol = [0] * cols

    for i in range(rows):
        for j in range(cols):
            sumRow[i]+= arr[i][j]
            sumCol[j]+= arr[i][j]

    l = ['row', 0, sumRow[0]]

    for i in range(rows):
        if sumRow[i] > l[2]:
            l[2] = sumRow[i]
            l[1] = i

    for j in range(cols):
        if sumCol[j] > l[2]:
            l[2] = sumCol[j]
            l[1] = j
            l[0] = 'column'

    return l

m, n = [int(x) for x in input().strip().split()]
l = [int(i) for i in input().split()]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l = largestRowCol(arr)
print(*l)


#Wave Print
"""
For a given two-dimensional integer array/list of size (N x M),
print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output format :
For each test case, print the elements of the two-dimensional array/list in the sine wave order in a single line, separated by a single space.
Output for every test case will be printed in a seperate line.
"""
Sample Input 1:
1
3 4
1  2  3  4
5  6  7  8
9 10 11 12
Sample Output 1:
1 5 9 10 6 2 3 7 11 12 8 4

Sample Input 2:
2
5 3
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
3 3
10 20 30
40 50 60
70 80 90
Sample Output 2:
1 4 7 10 13 14 11 8 5 2 3 6 9 12 15
10 40 70 80 50 20 30 60 90

Solution :

def wave_Print(twoDArr,row,col):
    top=0
    bottom=row-1
    left=0
    right=col-1
    direction=0

    while (left<=right):

        if (direction==0):
            for i in range(top,bottom+1):
                print(twoDArr[i][left],end=" ")
            left+=1
            direction=1

        elif (direction==1):
            for i in range(bottom,top-1,-1):
                print(twoDArr[i][left],end=" ")
            left+=1
            direction=0

l=[int(i) for i in input().strip().split(" ")]
row,col = l[0],l[1]
arr=[[l[(j*col)+i+2] for i in range(col)] for j in range(row)]
wave_Print(arr,row,col)


#Spiral Print
"""
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form.
That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
Mind that every element will be printed only once.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.

Output format :
For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.
Output for every test case will be printed in a seperate line. 
"""
Sample Input 1:
1
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Sample Input 2:
2
3 3
1 2 3
4 5 6
7 8 9
3 1
10
20
30
Sample Output 2:
1 2 3 6 9 8 7 4 5
10 20 30

Solution :

def spiralPrint(twoDArr,row,col):
    top=0
    bottom=row-1
    left=0
    right=col-1
    direction=0

    while (top<=bottom) and (left<=right):

        if (direction==0):
            for i in range(left,right+1):
                print(twoDArr[top][i],end=" ")
            top+=1
            direction=1

        elif (direction==1):
            for i in range(top,bottom+1):
                print(twoDArr[i][right],end=" ")
            right-=1
            direction=2

        elif (direction==2):
            for i in range(right,left-1,-1):
                print(twoDArr[bottom][i],end=" ")
            bottom-=1
            direction=3

        elif (direction==3):
            for i in range(bottom,top-1,-1):
                print(twoDArr[i][left],end=" ")
            left+=1
            direction=0

l=[int(i) for i in input().strip().split(" ")]
row,col = l[0],l[1]
arr=[[l[(j*col)+i+2] for i in range(col)] for j in range(row)]
spiralPrint(arr,row,col)
