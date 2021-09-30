#Binary Pattern
"""
Print the following pattern for the given number of rows.
Pattern for N = 4
    1111
    000
    11
    0
Input format : N (Total no. of rows)
Output format : Pattern in N lines
"""
Sample Input :
5
Sample Output :
11111
0000
111
00
1

Solution :
n=int(input())
for i in range(1,n+1,1):
    for j in range(n-i+2,1,-1):
        if i % 2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()


#Print Number Pyramid
"""
Print the following pattern for a given n.
For eg. N = 6

123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

"""
Sample Input 1 :
4
Sample Output 1 :
1234
 234
  34
   4
  34
 234
1234

Solution :
n = int(input())
for i in range (1,2*n,1):
    for j in range(1,n+1,1):
        if i > j and i + j < 2*n:
            print(" ", end="")
        else:
            print(j,end="")
    print()


#Rectangular numbers
"""
Print the following pattern for the given number of rows.
Pattern for N = 4

    4444444
    4333334
    4322234
    4321234
    4322234
    4333334  
    4444444
    
Input format : N (Total no. of rows)
Output format : Pattern in N lines
"""
Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333

Solution :
n = int(input())
i = 1-n
while i<n:
    j=1-n
    while j<n:
        v=1+max(abs(i),abs(j))
        print(v,end="")
        j=j+1
    print()
    i=i+1


#Print the pattern
"""
Print the following pattern for the given number of rows.

Pattern for N = 5

 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
 
Input format : N (Total no. of rows)
Output format : Pattern in N lines
"""
Sample Input :
4
Sample Output :
 1  2  3  4
 9 10 11 12
13 14 15 16
 5  6  7  8

Solution :
n = int(input())
z = 1
for i in range(1, n + 1, 1):
    toprint = (z - 1) * n + 1
    for j in range(toprint, toprint + n, 1):
        print(j, end=" ")
    if i < int((n + 1) / 2):
        z = z + 2
    elif i == int((n + 1) / 2):

        if n % 2 == 0:
            z = z + 1
        else:
            z = z - 1

    else:
        z = z - 2
    print()
