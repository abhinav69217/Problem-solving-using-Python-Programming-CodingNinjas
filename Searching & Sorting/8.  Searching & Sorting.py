#Binary Search
"""
You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X.
Write a function to search this element in the given input array/list using 'Binary Search'.
Return the index of the element in the input array/list.
In case the element is not present in the array/list, then return -1.

Input format :
The first line contains an Integer 'N' which denotes the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow..

All the 't' lines henceforth, will take the value of X to be searched for in the array/list

Output Format :
For each test case, print the index at which X is present, -1 otherwise.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
7
1 3 7 9 11 12 45
1
3
Sample Output 1:
1

Sample Input 2:
7
1 2 3 4 5 6 7
2
9
7
Sample Output 2:
-1
6

Solution :

def binarysearch(arr,element):
    start=0
    end=len(arr)-1

    while (start<=end):
        mid=(start+end)//2

        if (arr[mid]==element):
            return mid

        elif (arr[mid]<element):
            start=mid+1

        else:
            end=mid-1

    return -1

n=int(input())
arr = [int(x) for x in input().split()]
element=int(input())
index=binarysearch(arr,element)
print(index)


#Bubble Sort
"""
Provided with a random integer array/list(ARR) of size N,
you have been required to sort this array using 'Bubble Sort'.

Note:
Change in the input array/list itself. You don't need to return or print the elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Output format :
For each test case, print the elements of the array/list in sorted order separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28

Sample Input 2:
2
5
9 3 6 2 0
4
4 3 2 1
Sample Output 2:
0 2 3 6 9
1 2 3 4

Solution :

def bubbleSort(arr):
    length = len(arr)

    for i in range(length - 1):

        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input())
arr = [int(x) for x in input().split()]
bubbleSort(arr)
for x in arr:
    print(x, end=" ")


#Insertion Sort
"""
Provided with a random integer array/list(ARR) of size N,
you have been required to sort this array using 'Insertion Sort'.

Note:
Change in the input array/list itself. You don't need to return or print the elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the elements of the array/list in sorted order separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28

Sample Input 2:
2
5
9 3 6 2 0
4
4 3 2 1
Sample Output 2:
0 2 3 6 9
1 2 3 4

Solution :

def insertionSort(arr):
    length=len(arr)

    for i in range (1,length):
        j=i-1
        temp=arr[i]

        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1]=temp

n=int(input())
arr=[int(x) for x in input().split()]
insertionSort(arr)
for x in arr:
    print(x,end=" ")


#Merge Two Sorted Arrays
"""
You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively,
merge them into a third array/list such that the third array is also sorted.

Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

Output Format :
For each test case, print the sorted array/list(of size N + M) in a single row, separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1 :
1
5
1 3 4 7 11
4
2 4 6 13
Sample Output 1 :
1 2 3 4 4 6 7 11 13

Sample Input 2 :
2
3
10 100 500
7
4 7 9 25 30 300 450
4
7 45 89 90
0
Sample Output 2 :
4 7 9 10 25 30 100 300 450 500
7 45 89 90

Solution :

def mergedArr(arr1, arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []

    while ((i < len1) and (j < len2)):

        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i = i + 1

        else:
            arr.append(arr2[j])
            j = j + 1

    while (i < len1):
        arr.append(arr1[i])
        i = i + 1

    while (j < len2):
        arr.append(arr2[j])
        j = j + 1

    return arr

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]
arr = mergedArr(arr1, arr2)
for x in (arr):
    print(x, end=" ")


#Push Zeros to end
"""
You have been given a random integer array/list(ARR) of size N.
You have been required to push all the zeros that are present in the array/list to the end of it.
Also, make sure to maintain the relative order of the non-zero elements.

Note:
Change in the input array/list itself. You don't need to return or print the elements.
You need to do this in one scan of array only. Don't use extra space.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the elements of the array/list in the desired order separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
2 0 0 1 3 0 0
Sample Output 1:
2 1 3 0 0 0 0
Explanation for the Sample Input 1 :
All the zeros have been pushed towards the end of the array/list.
Another important fact is that the order of the non-zero elements have been maintained as they appear in the input array/list.
Sample Input 2:
2
5
0 3 0 2 0
4
9 0 0 8 2
Sample Output 2:
3 2 0 0 0
9 8 2 0 0

Solution :

def pushZerosToEnd(arr, n):
    count = 0

    for i in range(n):

        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

n = int(input())
arr = [int(x) for x in input().split()]
pushZerosToEnd(arr, n)
for x in (arr):
    print(x, end=" ")


#Rotate array
"""
You have been given a random integer array/list(ARR) of size N.
Write a function that rotates the given array/list by D elements(towards the left).

Note:
Change in the input array/list itself. You don't need to return or print the elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains the value of 'D' by which the array/list needs to be rotated.

Output Format :
For each test case, print the rotated array/list in a row separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2

Sample Input 2:
2
7
1 2 3 4 5 6 7
0
4
1 2 3 4
2
Sample Output 2:
1 2 3 4 5 6 7
3 4 1 2

Solution :

def leftRotate(arr, d, n):

    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]

    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = temp

def printArray(arr, size):

    for i in range(size):
        print("%d" % arr[i], end=" ")

n = int(input())
arr = [int(x) for x in input().split()]
d = int(input())
leftRotate(arr, d, n)
printArray(arr, n)


#Second Largest in array
"""
You have been given a random integer array/list(ARR) of size N.
You are required to find and return the second largest element present in the array/list.
If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the second largest in the array/list if exists, -2147483648 otherwise.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
13

Sample Input 2:
1
5
9 3 6 2 9
Sample Output 2:
6

Sample Input 3:
2
2
6 6
4
90 8 90 5
Sample Output 3:
-2147483648
8

Solution :

def second_largest(lst):
    L = float('-inf')
    S = float('-inf')

    for i in range(len(lst)):

        if float(lst[i]) > L:
            S = L
            L = float(lst[i])

        elif float(lst[i]) < L:

            if float(lst[i]) > S:
                S = float(lst[i])

    print(int(S))

n = int(input())
lst = list(int(x) for x in input().split())
second_largest(lst)


#Check Array Rotation
"""
You have been given an integer array/list(ARR) of size N.
It has been sorted(in increasing order) and then rotated by some number 'K' in the clockwise direction.
Your task is to write a function that returns the value of 'K',
that means, the index from which the array/list has been rotated.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the value of 'K' or the index from which which the array/list has been rotated.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
6
5 6 1 2 3 4
Sample Output 1:
2

Sample Input 2:
2
5
3 6 8 9 10
4
10 20 30 1
Sample Output 2:
0
3

Solution :

def countRotations(arr, low, high):

    if (high < low):
        return 0

    if (high == low):
        return low

    mid = low + (high - low) / 2;
    mid = int(mid)

    if (mid < high and arr[mid + 1] < arr[mid]):
        return (mid + 1)

    if (mid > low and arr[mid] < arr[mid - 1]):
        return mid

    if (arr[high] > arr[mid]):
        return countRotations(arr, low, mid - 1);

    return countRotations(arr, mid + 1, high)

m = int(input())
arr = [int(x) for x in input().split()]
n = len(arr)
print(countRotations(arr, 0, n - 1))


#Sort 0 1 2
"""
You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s.
Write a solution to sort this array/list in a 'single scan'.
'Single Scan' refers to iterating over the array/list just once or to put it in other words,
you will be visiting each element in the array/list just once.

Note:
You need to change in the given array/list itself. Hence, no need to return or print anything.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers(all 0s, 1s and 2s) representing the elements in the array/list.

Output Format :
For each test case, print the sorted array/list elements in a row separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
0 1 2 0 2 0 1
Sample Output 1:
0 0 0 1 1 2 2

Sample Input 2:
2
5
2 2 0 1 1
7
0 1 2 0 1 2 0
Sample Output 2:
0 1 1 2 2
0 0 0 1 1 2 2

Solution :

def count(li):
    total_one=0
    total_zero = 0
    total_two=0

    for ele in li:

        if ele == 1:
            total_one+=1

        elif ele ==0:
            total_zero+=1

        elif ele==2:
            total_two+=1

    return [total_one, total_zero,total_two]

n=int(input())
li=[int(x) for x in input().split()]
total_array=count(li)
finalArray = []

for i in range(total_array[1]):
    finalArray.append(0)

for i in range (total_array[0]):
    finalArray.append(1)

for i in range(total_array[2]):
    finalArray.append(2)

for x in finalArray:
    print(x,end=" ")


#Sum of Two Arrays
"""
Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively.
Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index).
The idea here is to represent each array/list as an integer in itself of digits N and M.
You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list i.e. output array/list will also contain only single digit at every index.

Note:
The sizes N and M can be different. 
Output array/list(of all 0s) has been provided as a function argument. 
Its size will always be one more than the size of the bigger array/list. Place 0 at the 0th index if there is no carry. 
No need to print the elements of the output array/list.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

Output Format :
For each test case, print the required sum of the arrays/list in a row, separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
3
6 2 4
3
7 5 6
Sample Output 1:
1 3 8 0

Sample Input 2:
2
3
8 5 2
2
1 3
4
9 7 6 1
3
4 5 9
Sample Output 2:
0 8 6 5
1 0 2 2 0

Solution :

def convert2number(arr):
    number=0

    for item in arr:
        number=(number*10)+item

    return number

def convert2array(number,length):
    arr=list(str(number))

    if len(arr) < length + 1:

        for x in range (len(arr),length+1):
            arr.insert(0,"0")

    return arr

n=int(input())
arr1=[int(x) for x in input().split()]
m=int(input())
arr2=[int(x) for x in input().split()]
number1=convert2number(arr1)
number2=convert2number(arr2)
biggerArrSize = 0

if len(arr1) >= len(arr2):
    biggerArrSize = len(arr1)

else:
    biggerArrSize = len(arr2)

final_arr=convert2array(number1+number2,biggerArrSize)
for x in final_arr:
    print(x,end=" ")
