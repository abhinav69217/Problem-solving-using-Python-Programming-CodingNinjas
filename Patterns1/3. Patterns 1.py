#Square Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    4444
    4444
    4444
    4444
"""
Sample Input 1:
7
Sample Output 1:
7777777
7777777
7777777
7777777
7777777
7777777
7777777

Solution :
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(n , end="")
        j = j + 1
    print()
    i = i + 1


#Triangular Star Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    *
    **
    ***
    ****
Note : There are no spaces between the stars (*)
"""
Sample Input :
5
Sample Output :
*
**
***
****
*****

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*" , end = "")
        j = j + 1
    print()
    i = i +1


#Triangle Number Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
    22
    333
    4444
"""
Sample Input :
5
Sample Output :
1
22
333
4444
55555

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        print(i , end = "")
        j = j + 1
    print()
    i = i +1


#Reverse Number Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
    21
    321
    4321
"""
Sample Input :
5
Sample Output :
1
21
321
4321
54321

Solution :
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i - j + 1 , end = "")
        j = j + 1
    print()
    i = i + 1


#Character Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    A
    BC
    CDE
    DEFG
"""
Sample Input :
5
Sample Output :
A
BC
CDE
DEFG
EFGHI

Solution :
n = int(input())
i = 1
while i <= n:
    j = 1
    start = chr(ord('A')+i-1)
    while j <= i:
        charP = chr(ord(start)+j-1)
        print(charP , end = "")
        j = j + 1
    print()
    i = i + 1


#Interesting Alphabets
"""
Print the following pattern for the given number of rows.
Pattern for N = 5
    E
    DE
    CDE
    BCDE
    ABCDE
"""
Sample Input :
8
Sample Output :
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH

Solution :
n = int(input())
i = 1
start = chr(ord('A') + n -1)

while i <= n:
    j = 1
    while j <= i:
        charP = chr(ord(start)-i+j)
        print(charP , end = "")
        j = j + 1
    print()
    i = i + 1


#Number Pattern 1
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
    11
    111
    1111
"""
Sample Input :
5
Sample Output :
1
11
111
1111
11111

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("1" , end = "")
        j = j + 1
    print()
    i = i +1


#Number Pattern 2
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
    11
    202
    3003
"""
Sample Input :
5
Sample Output :
1
11
202
3003
40004

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        if (j == 1) or (j == i):
            if (i-1==0):
                print("1" , end = "")
            else:
                print(i-1 , end = "")
        else:
            print("0" , end = "")
        j = j + 1
    print()
    i = i +1


#Number Pattern 3
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
    11
    121
    1221
"""
Sample Input :
5
Sample Output :
1
11
121
1221
12221

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        if (j == 1) or (j == i):
            print("1" , end = "")
        else:
            print("2" , end = "")
        j = j + 1
    print()
    i = i +1


#Number Pattern 4
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1234
    123
    12
    1
"""
Sample Input :
5
Sample Output :
12345
1234
123
12
1

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n-i+1:
        print(j , end = "")
        j = j + 1
    print()
    i = i +1


#Alpha Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 3
    A
    BB
    CCC
"""
Sample Input :
7
Sample Output :
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

Solution :
n = int(input())
i = 1
while i <= n :
    j = 1
    start = chr(ord('A'))
    while j <= i:
        charP = chr(ord(start)+i-1)
        print(charP , end = "")
        j = j + 1
    print()
    i = i +1
