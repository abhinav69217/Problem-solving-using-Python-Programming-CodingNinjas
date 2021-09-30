#Check number
"""
Given an integer n, find if n is positive, negative or 0.
If n is positive, print "Positive"
If n is negative, print "Negative"
And if n is equal to 0, print "Zero".
"""
Input Format : Integer n
Output Format : "Positive" or "Negative" or "Zero" (without double quotes)

Solution :
n = int(input())
if n >= 1 :
    print("Positive")
elif n <= -1 :
    print("Negative")
else :
    print("Zero")


#Sum of n numbers
"""
Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.
"""
Input Format : Integer n
Output Format : Sum

Solution :
n = int(input())
count = 1
sum = 0
while count <= n:
    sum = sum + count
    count = count + 1
print(sum)


#Sum of Even Numbers
"""
Given a number N, print sum of all even numbers from 1 to N.
"""
Input Format : Integer N
Output Format : Required Sum

Solution :
n = int(input())
count = 2
sum = 0
while count <= n:
    sum = sum + count
    count = count + 2
print(sum)


#Fahrenheit to Celsius
"""
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
you need to convert all Fahrenheit values from Start to End at the gap of W,
into their corresponding Celsius values and print the table.
"""
Input Format : 3 integers - S, E and W respectively
Output Format : Fahrenheit to Celsius conversion table.
                One line for every Fahrenheit and corresponding Celsius value.
                On Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")

Solution :
fh1 = int(input())
fh2 = int(input())
step = int(input())
cth = fh1
while cth <= fh2:
    c = int((cth - 32) * 5 / 9)
    print(str(cth) + "\t" + str(c))
    cth = cth + step


#Calculator
"""
1. If the input is 1, 2 integers are taken from the user and their sum is printed.
2. If the input is 2, 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
3. If the input is 3, 2 integers are taken from the user and their product is printed.
4. If the input is 4, 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
5. If the input is 5, 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
6. If the input is 6, the program exits.
7. For any other input, print "Invalid Operation".
"""
Input format: Take integers as input, in accordance to the description of the question.
Output format: The output lines must be as prescribed in the description of the question.

Solution :
while (True):
    ch=int(input())
    if(ch==1):
        a=int(input())
        b=int(input())
        c=a+b
        print(c)
    elif(ch==2):
        a=int(input())
        b=int(input())
        c=a-b
        print(c)
    elif(ch==3):
        a=int(input())
        b=int(input())
        c=a*b
        print(c)
    elif(ch==4):
        a=int(input())
        b=int(input())
        c=a//b
        print(c)
    elif(ch==5):
        a=int(input())
        b=int(input())
        c=a%b
        print(c)
    elif(ch==6):
        break
    else:
        print("Invalid Operation")


#Reverse of a number
"""
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. 
For e.g., reverse of 10400 will be 401 instead of 00401.
"""
Input format : Integer N
Output format : Corresponding reverse number

Solution :
n = int(input())
rev = 0
while n > 0:
    l = n % 10
    n = n // 10
    rev = rev * 10 + l
print(rev)


#Palindrome number
"""
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
"""
Sample Input : 121
Sample Output : true

Solution :
n = int(input())
nclone = n
rev = 0
while n > 0:
    l = n % 10
    n = n//10
    rev = rev * 10 + l
if nclone == rev:
    print("true")
else :
    print("false")


#Sum of even & odd
"""
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places!
That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
"""
Input format : Integer N
Output format : Sum_of_Even_Digits Sum_of_Odd_Digits
                (Print first even sum and then odd sum separated by space)
Sample Input 1: 1234
Sample Output 1: 6 4

Solution :
n = int(input())
evensum = 0
oddsum = 0
while (n>0):
    d = n % 10
    if d % 2==0:
        evensum = evensum + d
    else:
        oddsum = oddsum + d
    n = n//10
print (evensum,"",oddsum)


#Nth Fibonacci number
"""
Nth term of fibonacci series F(n) is calculated using following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) = F(2) = 1
Provided N you have to find out the Nth Fibonacci Number.
"""
Input Format : Integer n
Output Format : Nth Fibonacci term i.e. F(n)
Sample Input 1: 4
Sample Output 2: 3

Solution :
n = int(input())
counter = 1
first = 1
second = 1
while counter < n:
    temp = first + second
    first = second
    second = temp
    counter = counter + 1
print(first)
