# -*- coding: utf-8 -*-
"""Copy of StringAndFile_Student.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0W5R2l3D1cGtflmcjg-51P_tBIjh-CG

<B>String Revision
"""

s = "I'm a string"
t = 'I said "This is a string".'
chars = input() #key input are strings
c = 0
for ch in chars: #for each ch in chars
    if ch in s:
        c += 1
print("first", c)
for i in range(len(t)): #for each char in t
    if t[i] in s:
        c += 1
print("second c", c)

r = ""
for k in range(2,10,2):
    r += str(k)    # 2468 string concat
r = 2*r            # 24682468 repetition
print(r)

"""<B>=======================================</B>

Revision Exercise: Write a program to transform any word (lower case) to its plural form.

The rule (this is just a simplified rule) is :
- If the word ends with "s", "x", or "ch" then add "es".
- If the word ends with "y", but the character before "y" is not a vowel, then change "y" to "ies".
- Otherwise, add "s" to the back of the word.
"""

#Write your code here
def transform_to_plural(s) :
  vowels = ["a","e","i","o","u"]
  if s[-1] == "s" or s[-1] == "x" or s[-2]+s[-1] == "ch" :
    s += "es"
    return s
  elif s[-1] == "y" and s[-2] not in vowels :
    new_s = s[:len(s)-1:]
    new_s += "ies"
    return new_s
  else :
    s += "s"
    return s
print(transform_to_plural("toss"))
print(transform_to_plural("poppy"))
print(transform_to_plural("sword"))

"""<B>================================================</B>

Example 1:

Read N names (each name <= 10 characters), separated by ", " and display 3 names on each line. Each name must be displayed using 12 characters (add space when appropriate).

For example:

Bucciarati, Gioruno, Abbacchio, Arancia, Pannacotta, Mista, Resotto, Doppio will result in
"""

x = input().split(", ")
for i in range(len(x)) :
    x[i] = x[i] + " "*(12-len(x[i]))

for i in range(0,len(x),3) :
    print("".join(x[i:i+3]))

"""=======================================

Example 2: Air Quality Report!!

http://air4thai.pcd.go.th/services/getNewAQI_XML.php?stationID=52t stores an XML file with air quality information of a site. The file is updated regularly.

![image-3.png](attachment:image-3.png)
"""

import urllib.request

def find(s, start, c):
    for i in range(start, len(s)):
        if s[i] == c: return i
    return -1

url = "http://air4thai.pcd.go.th/services/getNewAQI_XML.php?stationID=52t"
web = urllib.request.urlopen(url)
for line in web:
    line = line.decode()
    if "<PM25 value=" in line:
        i = find(line, 0, '"')
        j = find(line, i+1, '"')
        print("PM 2.5 =", line[i+1:j])
        break

"""======================================

<B>Exercise 7-1<B>

Question 1: 
Write a function is_palindrome(s)to check whether string s is a palindrome. A palindrome is a string where you get the same sequence of character from left to right and right to left. 

For example: 

ABBA and 12-343-21 are palindromes.
"""

#Write your code here!
def is_palindrome(s) :
  if s[:len(s)//2:] == s[-1:-len(s)//2:-1] :
    return True
  else : return False
print(is_palindrome("mom"))
print(is_palindrome("what"))
print(is_palindrome("12-343-21"))

"""Question 2:

Write function ngrams(s,n). This function returns a list of all possible character sequence of length n (n is always >=1) from the string s.

For example, "ABCDEF" -> ["ABC","BCD","CDE","DEF"]

"""

#Write your code here!

def ngrams(s,n) :
  arr = []
  for i in range(0,len(s)) :
    arr.append(s[i:n+i:])
    if len(s) - i <= n :
      break
  return '[\"'+ '\",\"'.join(arr)+'\"]'
print(ngrams("ABCDEF", 3))
print(ngrams("ABBAXD", 2))

"""Question 3:

Write function strip_all(s,c). This function return string s, with all characters in string c removed. 

For example:

strip_all("I-dont-know-how-to-code-this", "-") will return "Idontknowhowtocodethis"

strip_all("I-dont-know-how-to-code-this", "-o") will return "Idntknwhwtcdethis"
"""

#Write your code here
def strip_all(s, c) :
  new_s = ""
  for ch in s :
    if ch not in c :
      new_s += ch
  return new_s
print("\""+strip_all("I-dont-know-how-to-code-this", "-")+"\"")
print("\""+strip_all("I-dont-know-how-to-code-this", "-o")+"\"")

"""Question 4:

Write function zero_pad(n,d), where n and d are integers. This function returns a string containing numbers in n but it adds zero to the left so that the resulting string's length is d. If n is already of length d or greater, then this funtion just returns n. 

For example: 

zero_pad(123, 5) will return "00123"

zero_pad(123, 2) will return "123"
"""

# Write your code here

def zero_pad(n, d):
    dlen = max(len(str(n)), d)
    result = '0'*d + str(n)
    return result[-dlen:]

print(zero_pad(123, 5))
print(zero_pad(123, 2))

'0'*-3

"""Question 5:

Write function thousands_separator(n). This function receives integer n. It returns a string that is like n but add commas, for example: 

thousands_separator(1234567) will return "1,234,567"

"""

#Write your code here
def thousands_separator(n) :
  s = str(n)
  s = s[::-1]
  arr = []
  for i in range(0,len(s),3) :
    arr.append(s[i:3+i:])
  a = ",".join(arr)
  a = a[::-1]
  return a
print(thousands_separator(1234567))
print(thousands_separator(1111111111))
print(thousands_separator(112))

"""========================================

<B>Escape Characters</B>

S = “   “  cannot have “ inside

S = ‘   ‘   cannot have ‘ inside
"""

s = " " "   # will cause error
s = " "sddd" "  # will cause error
s = ' ' '  # will cause error
s = " 'sddd' " #this is ok

s = "Hello"
print(s)              # Hello

s = "\"Hello\""
print(s)              # "Hello"

s = "\'Hello\'"
print(s)              # 'Hello'

s = "\"\'\\Hello\\"
print(s)              # "'\Hello\

s = "Hello\nPython"   # Hello
                      # Python
print(s)

print("A\n\n\nBCD\nE")

"""<B>Example: 

Replacing “ ‘ / \ ( ) , . : ;  with space using function remove_punc(t).
"""

def remove_punc(t) :
    result = ""
    for e in t :
        if e in "\"\'/\\(),.:;" :
            result += " "
        else : 
            result += e
    return result

s = input()
print(remove_punc(s))

#try with "\"hello\"()AB, CD"

remove_punc("\"hello\"()AB, CD")

"""========================================

<B>String Methods
    


"""

#01234567890123
s = "  Hello World "
len(s)   
len("") 
print(s.lower())     # returns a new string  
print(s.upper())     # returns a new string

print(s.strip())     # returns a new string

print(s.find("o"))   # find the first position that has o

print(s.find("ex"))  # find the first position that has ex

print(s.find("o",7)) # find, starting from position 7, the first position that has o 
                     # the returned position number is not relative

"""Getting back to Air Quality Example"""

import urllib.request

#def find(s, start, c):
#    for i in range(start, len(s)):
#        if s[i] == c: return i
#    return -1

url = "http://air4thai.pcd.go.th/services/getNewAQI_XML.php?stationID=52t"
web = urllib.request.urlopen(url)
for line in web:
    line = line.decode()
    if "<PM25 value=" in line:
        i = line.find('"')         # we now use string's find
        j = line.find('"',i+1)     # we now use string's find
        print("PM 2.5 =", line[i+1:j])
        break

"""=======================================

<B>Exercise 7-2

Question 1:

Write function number_of_newlines(s). This function returns the number of new line characters in string s.
"""

#Write your code here
def number_of_newlines(s) :
  count = 0
  for i in range(1,len(s)) :
    if s[i-1]+s[i] == "\n" :
      count += 1
  return count

"""Question 2:

Write function left_strip(s). This function returns a new string that looks like s but does not have spaces on its left hand size. 

For example: left_strip(" ab ") returns "ab "



"""

# Write your code here
def left_strip(s) :
  new_s = ""
  #s = s[::-1]
  #print(s)
  for i in range(len(s)) :
    if s[i] == " " :
      pass
    else :
      new_s += s[i:]
      break
  #new_s = new_s[::-1]
  return new_s#[::-1]

print(left_strip("   Hello   B     "))

"""Question 3:

Write function right_strip(s). This function returns a new string that looks like s but does not have spaces on its right hand size. 

For example: left_strip("  ab       ") returns "  ab"

"""

# Write your code here
def right_strip(s) :
  new_s = ""
  s = s[::-1]
  #print(s)
  for i in range(len(s)) :
    if s[i] == " " :
      pass
    else :
      new_s += s[i:]
      break
  #new_s = new_s[::-1]
  return new_s[::-1]

print(right_strip("   Hello   B     "))

"""Question 4: 

Write function first_index_of(s,t). This function returns the first position of t in string s. It returns -1 if there is no t in s. 

For example: 

first_index_of("abracadabra", "bra") returns 1

first_index_of("abracadabra", "BRA") returns -1



"""

# Write your code here
def first_index_of(s,c) :
  if c not in s :
    return -1
  for i in range(len(s)) :
    if c == s[i:i+len(c):] :
      return i

    #return -1

print(first_index_of("abracadabra", "bra"))
print(first_index_of("abracadabra", "BRA"))

"""Question 5: 

Write function first_index_of(s,t). This function returns the first position of t in string s. It returns -1 if there is no t in s. <u>Capital letters and non-capital letters are considered to be the same. 

For example: 

first_index_of("abracadabra", "bra") returns 1

first_index_of("abracadabra", "BRA") returns 1

"""

# Write your code here 
def first_index_of(s,t) :
  #s = s.lower()
  #t = t.lower()
  if t.lower() not in s.lower() :
    return -1
  for i in range(len(s)) :
    if t.lower() == s[i:i+len(t):].lower() :
      return i

print(first_index_of("abracadabra", "bra"))
first_index_of("abracadabra", "BRA")

"""Question 6: 

Write function last_index_of(s,t). This function returns the last position of t in string s. It returns -1 if there is no t in s. <u>Capital letters and non-capital letters are considered to be the same. 

For example: 

last_index_of("abracadabra", "bra") returns 8

last_index_of("abracadabra", "BRA") returns 8
"""

# Write your code here 
def last_index_of(s,t) :
  if t.lower() not in s.lower() :
    return -1
  for i in range(0,len(s)) :
    if t[::-1].lower() == s[len(t)+i:i:-1].lower() :
      return len(s)-i-len(t)

print(last_index_of("abracadabra", "bra"))
print(last_index_of("abracadabra", "BRA"))

"""Question 7:

Write function index_of_kth(s,t,k). This function returns the position of the k<sup>th</sup> t in string s. It returns -1 if there is no k<sup>th</sup> t in s. The value of k starts from 1.

For example: 

index_of_kth("ABabAB", "AB", 1) returns 0

index_of_kth("ABabAB", "AB", 2) returns 4

index_of_kth("ABabAB", "AB", 3) returns -1

"""

# Write your code here 
def index_of_kth(a,b,k) :
  if k < 1 : return "Error k >= 1"
  count = 0
  for i in range(len(a)) :
    if b == a[i:i+len(b):] :
      count += 1
    if count == k :
      return i
  if count < k : return -1  
    
    
print(index_of_kth("ABabAB", "AB",1))
print(index_of_kth("ABabAB", "AB", 2))
print(index_of_kth("ABabAB", "AB", 3))

"""Question 8: 

Write function remove_duplicates(s). This function returns a new string that looks like s but does not have duplicates of any letter once that letter is found. <u>Capital letters and non-capital letters are considered to be the same.

For example: 
    
remove_duplicates("AbaaaaBbBbC") returns "AbC"
"""

# Write your code here 
def remove_duplicates(s) :

"""Question 9: 

Write function contains(s, w). This function checks whether w is a standalone word in s. Word punctuations are " ' / \ , . : ; ( ) [ ] { } and space. <u>Capital letters and non-capital letters are considered to be the same.</u> 

For example: 
    
contains("That's all folks", "that") returns True 

contains("That's all folks", "folk") returns False
"""

# Write your code here

"""Question 10: 
    
Write function camelCase(s). This function returns a string like s, but in camel case form.

* All words (separated by "\"\'/\\,.:;()[]{}") are pushed together.
* The first word is all lower case.
* Other words begin with a capital letter, with other letters being lower case. 

For example: 

"An example of "camel case"" returns "anExampleOfCamelCase"

"Emergency call 911" returns "emergencyCall911"



    
    
    
"""

# Write your code here

"""<B>======================================

<B>Function Composition 
"""

import math
d = float(input())

x = math.radians(d)
s = math.sin(x)
y = abs(s)
r = round(y, 2)
print(r)

#This is equivalent to the function composition below.
#The calls are nested. 
r = round(abs(math.sin(math.radians(d))), 2)
print(r)

"""<B>Method Chaining

"""

line1 = input()
line2 = line1.strip()
line3 = line2.upper()
i     = line3.find("OK")
print(i)

#This is equivalent to the method chaining below.
i = input().strip().upper().find("OK")
print(i)

"""<B>Beware!
    
String cannot be changed!
"""

s = "123456789"

# Both of these cause errors
s[2] = "a"
s[3:7] = "1111"

"""String method therefore does not change the string. It creates a new string!

"""

s = "HELLO"
print(s.lower())
print(s)  # the original string does not change!

"""But we can re-assign the original string variable to store the method's result. """

s = "HELLO"
s = s.lower()
print(s)

"""<B>Example: rot-13 (encode/decode)
    
we encode/decode a character by changing it to the one 13 places in front. 
    
<img src="rot13.png"
     alt="Rot 13 encoding"
     style="float: left; margin-right: 10px;" />

"""

def rot_13(s):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets *= 2
    rot13 = ""
    for ch in s :
        if "A" <= ch <= "Z" :
            pos = alphabets.find(ch)
            k = pos + 13
            rot13 += alphabets[k]
        else :
            rot13 += ch
    return rot13

original = "I HAVE A BAD FEELING ABOUT THIS."
print(rot_13(original))

"""===============================

<B>Exercise 7-3
    
Question 1 :

Make rot-13 work on lower case letters! The encoding/decoding of a lower case letter must be a lower case letter too.
    
"""

# Write your code here

"""Question 2:

Write function dedent(line). This functions resturns a new string that is like line, but it reduces spaces on the left hand side by half.


"""

# Write your code here

"""Question 3:

Write function rot5_digits(s). This function returns a new string that changes characters in s from 0,1,2,3,4,5,6,7,8 and 9 to 5,6,7,8,9,0,1,2,3 and 4 respectively. 

For example:

rot5_digits("My number is 02-218-6981") returns "My number is 57-763-1436"


"""

# Write your code here

"""Question 4: 

String dna contains only A, T, G, and C. Write function count_bases(dna). This function returns a list that stores number of A, T, G, C respectively.

For example:

count_bases("AAAATTTGGC") returns [4, 3, 2, 1] 




"""

# Write your code here

"""===========================

<B>Reading data from a file

Let us have file data.txt that contains 3 lines:
    
<img src="dataFile01.png"
     alt="simple data file"
     style="float: left; margin-right: 10px;" />
    
 Now we write code to open this file for reading.
    
"""

fn = open("data.txt", "r")  # r indicates READ mode
line1 = fn.readline()        # read one line (it can read beyond the last line) 
line2 = fn.readline()
line3 = fn.readline()
line4 = fn.readline()

fn.close() # close file

print(line1)
print(line2)
print(line3)
print(line4)  # it doesn't have anything to print, but it does not cause error!

"""The print result looks like it's having too many "\n". Let's test it a bit more!"""

print(len(line1))
print(len(line2))
print(len(line3))
print(len(line4))

"""There is a "\n" at the end of each line! (print already inserts its own "\n" for your string, that's why we have printed new line twice, except line 3, which does not have "\n").

Line 4 has 0 character, indicating the end of the file. We can use this to write a loop, reading each line from a file. As shown below: 


"""

fn = open("data.txt", "r")  
line = fn.readline()
while len(line) > 0 :
    print(line)
    line = fn.readline()
fn.close()

fn = open("data.txt", "r")  
for line in fn : #Easier!!!
    print(line)
fn.close()

"""<B><U>Example</U></B>: Print average score from the first 3 students in a file (score01.txt)!

The score file looks like this: 

<img src="score01Capture.png"
     alt="simple score file"
     style="float: left; margin-right: 10px;" />
"""

fn = open("score01.txt", "r")  
count = 0
sum = 0 
i = 0
for line in fn : 
    i += 1
    if i > 3 :
        break
    sum += float(line[-3:-1:1])    ### BUT THIS IS NOT GOOD IF SCORE ARE DECIMALS
    count += 1
print("Average = ", sum/count)
    
fn.close()

"""A more generic code is :"""

sum_points = 0; n = 3  # we can easily change n (very easy to see)

infile = open("score01.txt", "r")
for k in range(n):
    line = infile.readline() 
    x = line.split()
    sum_points += float(x[1])   # can have different decimals
infile.close()

print("Average =", sum_points/n)

"""<B><U>Example</U></B>: Display sort from high to low score (score01.txt)!"""

students = []  

fn = open("score01.txt", "r")  
for line in fn : 
    sid,point = line.strip().split() # split gives 2 value in a list. We can use 2 variables.
    point = float(point)          
    students.append([point, sid]) # add to a list, with score first, so it can be used in sort.
fn.close()

students.sort(reverse=True)   # we can sort normally and then reverse the list.
for [point,sid] in students :
    print(sid,point)

"""=====================================

<B>Exercise 7-4</B>

Question 1:

Given a file score02.txt 

<img src="score02Capture.png"
     alt="simple score 2 file"
     style="float: left; margin-right: 10px;" />

Find average of students whose ID starts with a given number) .

For example: 
* Input: score02.txt 62  -> output: Average = 84.6
* Input: score02.txt 59  -> output: No data


"""

# Write your code here

"""====================================

<B>Writing data to a file</B>
"""

fout = open(filename, "w")  #open for writing
fout.write("First line")    # write at the end of the file 
fout.write("Text\n")        # write and go to a new line  

fout.close()

"""Example: 

Record 100 numbers into a file, 10 numbers per line!

Triangilar number is number + i , number starts from 0 and i starts from 1.

1 3 6 10 15 ...  comes from 0+1, 1+2, 3+3, 6+4, 10+5, ...


"""

fout = open("tri_numbers.txt", "w")  #open for writing
num = 0
for i in range(1,101) :
    num = num + i
    fout.write(str(num)+" ")
    if i%10 == 0 :
        fout.write("\n")
fout.close()

"""================================

<B>Exercise 7-5</B>

Question 1: 

Create a file that contains a rot-13 code of an input file! The example file is "poen.txt"



"""

# Write your code here 
from google.colab import files
files.upload()

!pwd

!ls

/content/sample_data/

"""Question 2:

Write function count_line(filename). This function returns the number of lines in the given file. 


"""

# Write your code here

"""Question 3:

Write function print_merge(filename1, filename2). It reads 2 files and alternatingly shows lines from both files. If one file ends first, display the rest of the other file.
"""

# Write your code here

"""Question 4: 

Write funtion count_articles(filename) to count the total number of "a", "an", "the" in a file. You are given a "gridman.txt" to test (the file contains lyrics of a TV show opening). The answer from this file should be 14.   


"""

def replace_punctuation(s):
    # replace punctuation with space
    t = ""
    for e in s:
        if e in "\"\'/\\,.:;()[]{}!?":
            t += " "
        else:
            t += e
    return t

def count_word(words, w):
    # count number of w in list words
    w = w.lower()
    c = 0
    for e in words:
        if e.lower() == w:
            c += 1
    return c
    
def count_articles(filename):
    
   # Write your code here
