#Check Palindrome
"""
Given a String s, check it its palindrome. Return true if string is palindrome, else return false.
Palindrome strings are those, where string s and its reverse is exactly same.

Input Format :
 String S

Output Format :
"true" if S is palindrome, else "false"
"""
Sample Input 1 :
abcdcba
Sample Output 1 :
true

Sample Input 2 :
abcd
Sample Output 2 :
false

Solution :
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

s = input()
ans = isPalindrome(s)
if ans == 1:
    print("true")
else:
    print("false")


#Check Permutation
"""
Given two strings, S and T, check if they are permutations of each other. Return true or false.
Permutation means - length of both the strings should same and should contain same set of characters.
Order of characters doesn't matter.

Note : Input strings contain only lowercase english alphabets.

Input format :
Line 1 : String 1
Line 2 : String 2

Output format :
'true' or 'false'
"""
Sample Input 1 :
abcde
baedc
Sample Output 1 :
true

Sample Input 2 :
abc
cbd
Sample Output 2 :
false

Solution :

NO_OF_CHARS = 256

def Permutation(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    if len(str1) != len(str2):
        return 0

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1

str1 = input()
str2 = input()
if Permutation(str1, str2):
    print("true")
else:
    print("false")


#Remove Consecutive Duplicates
"""
Given a string, S, remove all the consecutive duplicates that are present in the given string.
That means, if 'aaa' is present in the string then it should become 'a' in the output string.

Input format :
String S

Output format :
Modified string
"""
Sample Input 1:
aabccbaa
Sample Output 1:
abcba

Sample Input 2:
xxyyzxx
Sample Output 2:
xyzx

Solution :

def removeDuplicates(S):
    n = len(S)
    if (n < 2):
        return

    j = 0
    for i in range(n):

        if (S[j] != S[i]):
            j += 1
            S[j] = S[i]
    j += 1
    S = S[:j]
    return S

if __name__ == '__main__':
    S1 = input()
    S1 = list(S1.rstrip())
    S1 = removeDuplicates(S1)
    print(*S1, sep="")


#Reverse Each Word
"""
Given a string S, reverse each word of a string individually.
For eg. if a string is "abc def", reversed string should be "cba fed".

Input Format :
String S

Output Format :
Modified string
"""
Sample Input 1:
Welcome to Coding Ninjas
Sample Output 1:
emocleW ot gnidoC sajniN

Sample Input 2:
Give proper names to variables and functions
Sample Output 2:
eviG reporp seman ot selbairav dna snoitcnuf

Solution :
def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" "))

Sentence = input()
print(reverseWordSentence(Sentence))


#Remove character
"""
Given a string and a character x.
Write a function to remove all occurrences of x character from the given string.
Leave the string as it is, if the given character is not present in the string.

Input Format :
Line 1 : String S
Line 2 : Character c

Output Format :
Modified string
"""
Sample Input 1:
welcome to coding ninjas
o
Sample Output 1:
welcme t cding ninjas

Sample Input 2:
Think of edge cases before submitting solutions
x
Sample Output 2:
Think of edge cases before submitting solutions

Solution :

test_string = input()
x = input()

for i in x:
    test_string = test_string.replace(i, '')

print(str(test_string))


#Highest Occurring Character
"""
Given a string, S, find and return the highest occurring character present in the given string.
If there are 2 characters in the input string with same frequency, return the character which comes first.

Note : Assume all the characters in the given string are lowercase.

Input format :
String S

Output format :
Highest occurring character
"""
Sample Input 1:
abdefgbabfba
Sample Output 1:
b

Sample Input 2:
xy
Sample Output 2:
x

Solution :

ASCII_SIZE = 256

def getMaxOccuringChar(str):
    count = [0] * ASCII_SIZE

    max = -1
    c = ''
    for i in str:
        count[ord(i)] += 1;

    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i

    return c

str = input()
print(getMaxOccuringChar(str))


#Compress the String
"""
Write a program to do basic string compression.
For a character which is consecutively repeated more than once,
replace consecutive duplicate occurrences with the count of repetitions.
For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

Note : Consecutive count of every character in input string is less than equal to 9.

Input Format :
String S

Output Format :
Compressed string 
"""
Sample Input 1 :
aaabbccdsa
Sample Output 1 :
a3b2c2dsa

Sample Input 2 :
aaabbcddeeeee
Sample Output 2 :
a3b2cd2e5

Solution :

str1 = input()
str2 = ''
m = 0
i = 0

while i < len(str1):
    count = 0
    temp = str1[i]
    for j in range(i, len(str1)):
        if str1[j] == temp:
            count += 1
        else:
            break
    if count > 1:
        str2 += str1[i] + str(count)

    else:
        str2 += str1[i]
    i = i + count - 1
    i += 1
print(str2)
