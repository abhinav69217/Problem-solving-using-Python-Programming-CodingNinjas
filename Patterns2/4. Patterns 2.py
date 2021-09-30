#Inverted Number Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    4444
    333
    22
    1
"""
Sample Input :
5
Sample Output :
55555
4444
333
22
1

Solution :
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i + 1:
        print(n-i+1 , end = "")
        j = j+1
    print()
    i = i + 1


#Mirror Number Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    ...1
    ..12
    .123
    1234
The dots represent spaces.
"""
Sample Input :
3
Sample Output :
  1
 12
123

Solution :
n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" ",end="")
        s = s + 1
    j = 1
    while j <= i:
        print(j,end ="")
        j = j+1
    print()
    i = i+1


#Star Pattern
"""
Print the following pattern
Pattern for N = 4
    ...*
    ..***
    .*****
    *******
The dots represent spaces.
"""
Sample Input  :
3
Sample Output  :
   *
  ***
 *****

Solution :
n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" " , end = "")
        s = s + 1
    star = 1
    while star <= i:
        print("*" , end = "")
        star = star + 1
    star2=i-1
    while star2>=1:
        print("*",end="")
        star2 = star2-1
    print()
    i = i+1


#Triangle of Numbers
"""
Print the following pattern for the given number of rows.
Pattern for N = 4
    ...1
    ..232
    .34543
    4567654
The dots represent spaces.
"""
Sample Input :
5
Sample Output :
           1
          232
         34543
        4567654
       567898765

Solution :
n = int(input())
i = 1
while i <= n:
    s = 1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j = 1
    p = i
    while j <= i:
        print(p , end = "")
        j = j + 1
        p = p + 1
    n2=2*(i-1)
    while n2>=i:
        if i>1:
            print(n2,end="")
        n2=n2-1
    print()
    i = i + 1


#Diamond of stars
"""
Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
    ..*
    .***
    *****
    .***
    ..*
The dots represent spaces.
"""
Sample Input :
3
Sample Output :
  *
 ***
  *

Solution :
n = int(input())
i = 1
n1 = (n+1)/2
while i <= n1:
    space = 1
    while space <=n1-i:
        print(" ",end="")
        space = space+1
    star = 1
    while star <= (2*i-1):
        print("*",end="")
        star = star+1
    print()
    i = i+1
i=1
n2=n/2
while i<=n2:
    space2=1
    while space2 <= i:
        print(" ",end="")
        space2 = space2+1
    star2=n-2*i
    while star2 > 0:
        print("*",end="")
        star2=star2-1
    print()
    i=i+1


#Number Pattern
"""
Print the following pattern for n number of rows.
For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321
"""
Sample Input :
4
Sample Output :
1      1
12    21
123  321
12344321

Solution :
n = int(input())
for i in range(1,n+1,1):
    for j in range (1,i+1,1):
        print(j,end="")
    for s in range((2*n)-2*i,0,-1):
        print(" ",end="")
    for n2 in range (i,0,-1):
        print(n2,end="")

    print()


#Zeros and Stars Pattern
"""
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
"""
Sample Input :
3
Sample Output :
*00*00*
0*0*0*0
00***00

Solution :
n = int(input())
for i in range(1,n+1,1):
    for j in range(1,2*n+2,1):
        if i==j or i+j==2*n+2 or j == n+1:
            print("*",end="")
        else:
            print("0",end="")
    print()


#Pyramid Number Pattern
"""
Print the following pattern for the given number of rows.
Pattern for N = 4
       1
      212
     32123
    4321234
Input format : N (Total no. of rows)
Output format : Pattern in N lines
"""
Sample Input :
5
Sample Output :
        1
       212
      32123
     4321234
    543212345

Solution :
n = int(input())
for i in range(1,n+1,1):
    for s in range(n-i):
        print(" ",end ="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1,1):
        if i!=1:
             print(j,end="")
    print()


#Arrow pattern
"""
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7

*
 * *
   * * *
     * * * *
   * * *
 * *
*

"""
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*

Solution :
n = int(input())
i = 0
while(i<n):
    k=1
    j=0
    if(i<n//2):
        while(k<=i):
            print(" ",end="")
            k=k+1
        while(j<=i):
            print("* ",end="")
            j=j+1
    else:
        k=i
        j=i
        while(k<n-1):
            print(" ",end="")
            k=k+1
        while(j<=n-1):
            print("* ",end="")
            j=j+1
    i=i+1
    print()
