################### LECTURE 1 ###################
int("5")
float("1.2")
str(82)
print("Hello World")
resp = input("Please write your name: ") #input will be string
print("""This is a multiline
		statement""")
print("This is a multiline \n statement")

################### LECTURE 2 ###################
if platform == "1":
    platformCharge = 0.4 * totalReward
else:
    platformCharge = 0.3 * totalReward

if platform == "1":
    platformCharge = 0.4
    totalAmountNeeded = platformCharge * totalReward
    state = “All good”
    if totalAmountNeeeded > amountAvailable:
        state = “No experiment for you”
        if amountAvailable <=0:
            state = “You’re broke”
print("This is your state: " + state)

participants = input(“Please enter the number of participants: ")
reward = input("Thanks! Now enter the reward per participant : £")
if int(participants) > 50 and float(reward) >= 1:
	totalAmount = totalReward + (totalReward * platformCharge)
else:
	 totalAmount = totalReward
print("The total amount required is £" + str(totalAmount))

if int(participants) > 50 or today==“Monday”:
	totalAmount = totalReward + (totalReward * platformCharge)
else:
    totalAmount = totalReward #when will this happen?
print("The total amount required is £" + str(totalAmount))

if platform != "1" and platform != "2" and platform !="3":
	print("You’re not paying attention. Higher charge applied!")
#But this might easier to read:
if not (platform == "1" or platform == "2" or platform =="3"):
	print("You’re not paying attention. Higher charge applied")

if platform == "1":
    charge = 0.4
elif platform == "2":
    charge = 0.3
else:
    charge = 0.35
print("Charge is " + str(charge))

#from random import randint

################### LECTURE 3 - Data Structures ####################
#Lists
aList = [1, 4, 2, "hello", 9.3]
first = aList[0]
aList[2] = "new" #set an element in list
b = aList[-1] #last element
b = aList[2:4]
b = aList[1:-2]
b = aList[:2]
b = aList[2:]

myList = [2, 3]
print(myList)
selection = input("first or second?") #user types first
if selection =="first":
	selection = 0
else:
	selection = 1
anElement = myList[selection]

aList = []

aList = [1, 4, 2, "hello", 9.3]
len(aList) #length of list
del(aList[2]) #remove item from list
aList.append(89) #add an item to the end of the list
aList.insert(1, ‘hi’) #insert an item anywhere in a list, 1st arg = index, 2nd arg = item to insert
max(aList)
min(aList)
aList.index(4)
aList.sort()
k = sorted(aList)
aList.reverse()
k = reversed(aList)

listOfLists = [[2, 4, 4], [2, 9, 7], [8, 3, 2]]
# listOfLists[1] is a list, specifically [2, 9, 7]
# listOfLists[2][0] is the 1st item from the 3rd list, i.e. 8

#Tuple
myFirstTuple = ("yet", "another", "collection", "of", 6, "things")

#Dictionary
aDict = {"key": "value", "searchMeBy": 4, "lookMeUpWith": 24.1, 12: 3}
participant = {"rt": 258, "response": 1, "age": 25, "gender": "female"}
aDict["newKey"] = "newValue"
del(aDict["key"])

participants = {
    "John": {"rt": 258, "response": 1, "age": 25, "gender": "male"},
    "Mary": {"rt": 312, "response": 2, "age": 32, "gender": "female"}
}
print("John’s reaction time is " + str(participants["John"]["rt"]))
collection = {}

#Set
biblicalSet = {"John", "Peter", "Mary", "Brian"}
biblicalSet.add("Matthias")
collection = set()

#String is a lso a data structure!
test = "This is a string"
len(test)
sorted(test)

#The in operator
aList = [43, 12, 9, "program"]
if 43 in aList:
    print("I found 43. Hooray!!!!")
if 43 not in aList:
    print("I will have to disappoint you…")

aDict = {"John": "07810928191", "Mary": "0779281729", "Peter": "0765455678"}
if "John" in aDict:
    print("The key named ‘John’ was found in the dictionary")

#isinstance(item, type) returns a Boolean (True/False) that indicates whether the ‘item’ is a variable of type ‘type’
#two args: The first is the thing we want to evaluate, and the second is the type we are testing against (e.g. str, int, float, list, tuple, dict)
isinstance(‘Hi’, str)
isinstance([2, 3, 4], str)

#Reading text from files
file = open("instructions.txt", "r")
contents = file.read() # will read the whole file and store it into the string
allLines = file.readlines()  # will read all lines in a List of strings
aLine = file.readline()  # will read the next line into a string

################### LECTURE 4 - Loops ####################
participants = ["Lara", "Neil", "Sarah", "Dave", "Adam"]
for part in participants:
    print("The participant's name is: " + part)

for part in participants:
    if "a" in part:
        print("The participant's name is: " + part)

book = {"John": "07810928191", "Mary": "0779281729", "Peter": "0765455678"}
for friend in book:
    print(friend + "'s number is " + book[friend])

#range(stop) #stop = upper bound (how many times)
for item in range(5):
    print("Hello")
#range(start, stop, step) - default start = 0, default step = 1
#Will create a list of numbers from start to stop (not including stop) in steps of size step
#e.g. range(2, 12, 3) is a list of number 2, 5, 8, 11


#“for i in range(x)” means “do x iterations and in each iteration assign to i a value between 0 and x”
for i in range(4):
    print(i*2)

names = ["Lara", "Neil", "Sarah"]
for i in range(len(names)):
    part = names[i]
    print("Name is: " + part)

for i in range(len(names)):
    print(names[i])

for name in names:
    print(name))

#Counting using loops
genders = ["male", "female", "male", "male", "female", "female", "female", "male", "female", "female", "male", "female"]
females = 0  # the counter that will be incremented every time we find a female in the loop
for participant in genders:
    if participant == "female":
        females = females + 1  # alternatively: females +=1
print("Number of females in the experiment: " + str(females))
print("Proportion of females: " + str(females / len(genders)))

marks = [[87, 76, 67], [65, 60, 66], [56, 67, 63], [48, 65, 70]]
averages = []
for student in marks:
    sum = 0
    for mark in student:
        sum += mark
    averages.append(sum/3)

age = input('Please enter your age: ')
while int(age) < 18:
    age = input('You are a minor. Please try again: ')

myVar = 3
while myVar < 4:
    print(myVar)
#This will result in an infinite loop: It will print 3 until the end of time

#When writing a while loop you need to ensure that the code to be repeated somehow changes the evaluation of the condition.
#This is fine:
age = input('Please enter your age: ')
while int(age) < 18:
        age = input('You are a minor. Please try again: ')
#This is not:
age = input('Please enter your age: ')
while int(age) < 18:
    print('You are a minor. Please try again: ')

#before the loop - initialise the variable
# e.g.: count = 0, sum = 0, items = [], word = ""
#in the loop - add values
# e.g. count += 1, sum += rt[i], items.append(rt[i]), word += character
#after the loop - work with the (filled) accumulator
# e.g. print(count), avg = sum/count, len(items), print(word)

################### LECTURE 5 - Working with text ####################
gross = "$2,186,772,302"
newGross = ""
for character in gross:
    if character != "$" and character != ",":
        newGross = newGross + character
newGross = int(newGross)

#functions operating on any collection
aString = "spamAndEggs"
len(aString)
sorted(aString)
max(aString)
min(aString)
aString[4:7] # allows you to get part of a string - slicing
aString.index(‘s’)
aString.rindex(‘s’)

#? looking for x in myString
exists = x in myString
#? but where in myString?
ind = myString.index(x)
ind = myString.find(x) #rfind will search from the end of the string (SAFER)
#? How many x’s in myString?
cnt = myString.count(x)
#EXAMPLE below - finding the T (four ways)
boxOffice = ["Avatar", "Titanic", "Star Wars: The Force Awakens”]
for film in boxOffice:
    if "T" in film:
        print("Found a T somewhere in the title")
for film in boxOffice:
    if film.index("T") == 0:  # will throw an error if there is not T
        print("Found a T at the beginning")
for film in boxOffice:
    if film.find("T") == 0:  # will return -1 if there is not T
        print("Found a T at the beginning")
for film in boxOffice:
    if film[0] == "T":
        print("Found a T at the beginning")

name = input("Please write your full name")
# assume the user enters “Christos Becsomething”
ind = name.index(" ")
name[ind+1:] #should give you surname

aString = "A long complicated 'string' containing a quote of someone important who said 'Something really important'–JB Lewis"
aString.index("'") #give index of the first quotation mark
slice1 = aString[aString.find("'") + 1:]
slice2 = slice1[slice1.find("'") + 1:]
quote = slice2[slice2.index("'") + 1:slice2.rindex("'")]

#tecniques for splitting - (1) partition, (2) split
# Slicing (e.g. aString[2:5]) produces a single substring
# (very) Often we need to split one string into two or more strings
aString = "who said 'Something really important'-JB Lewis“
aTuple = aString.partition("-") #(“who said ‘Something really important’”, “-”, “JB Lewis”)
participantIds = "344, 291, 201, 023, 382"
listOfIds = participantIds.split(“, “) #[344,291,201,023,382]

#techniques for coming together - (1) concatenate, (2) join
aStr = "It’s"
bStr = "just"
cStr = "a"
dStr = "flesh"
eStr = "wound"
allStrings = [aStr, bStr, cStr, dSrt, eStr]
# (1) concatenate
quote = aStr + bStr + cStr + dStr + eStr # "It’sjustafleshwound"
betterQuote = aStr + " " + bStr + " " + cStr + " " + dStr + " " + eStr #“It’s just a flesh wound”
# (2) join - separator.join(list)
" ".join(allStrings) #“It’s just a flesh wound”

#cases
quote = "it is just a FLESH wound"

quote.upper() #“IT IS JUST A FLESH WOUND”
quote.lower() #“it is just a flesh wound”
quote.capitalize() #“It is just a flesh wound” (first letter of the string capital, all else small)
quote.title() #“It Is Just A Flesh Wound” (first letter of every word capital, like journal article titles)
quote.swapcase() #“IT IS JUST A flesh WOUND”

#edit strings - (1) strip, (2) replace
# (1) strip - Removes leading and trailing characters from a string, The argument is optional. It defaults to whitespace
aStr = "aaaaaaEnoughaaaaaa"
newStr = aStr.strip('a') # “Enough”
# (2) replace - Replaces a substring with another one within a string
aStr = "aaaaaaEnoughaaaaaa"
newStr = aStr.replace('Enough', 'What') # “aaaaaaWhataaaaaa”

aString = "A long complicated string containing a quote of someone important who said 'Something really important'–JB Lewis“
aString[aString.index("–") + 1:] #if we want to extract just the name

#learning things about strings
myString.startswith("somestring") #Returns a Boolean that indicates whether myString starts with “some string”)
myString.endswith("some other string") #Well, you can guess…
myString.isalpha() #are all the characters in myString alphabetic(i.e.letters)?
myString.isdigit() #are all the characters in myString digits?
myString.isspace() #are all the characters whitespace(space, tab etc)?

#the f-string (ALMIGHTY lol)
#Concatenating strings (a+b) results in code that is hard to read, error-prone and sometimes slow (string is immutable)
#The join method works only in cases where we need the same separator everywhere (e.g. a space between words).
# What if we want to mix strings and numbers with a variety of phrases separating them? - f-string
# An f before the string starts, indicates to the interpreter that curly braces inside the string that follows have a special meaning
# Example
name = "peter"
age = 23
print("You are name and you are age years old") #You are name and you are age years old
print("Your name is " + name + " and your age is " + str(age)) #You are peter and you are 23 years old
print(f"You are {name} and you are {age} years old")
print(f"Next year you’ll be {age + 1}")
print(f“You are {name.capitalize()}”)
# With f-strings you can also specify the formatting
# The symbols after a colon (:) specify the format of presentation.
# % for percentage, f for decimal, e for scientific notation
f"as a decimal: {age: f}" #“as a decimal: 23.000”
f"as percentage: {age: %}" #“as percentage: 2300.000000%”
# Can also specify the number of digits after the decimal point:
f"as a decimal: {age: .2f}" # “as a decimal: 23.00”
f"as percentage: {age: .2 %}" #“as percentage: 2300.00 %”
f"as percentage: {age / 100: .2 %}" #“as percentage: 23.00 %”

# READABILITY MATTERS
newString = myString[myString.find('('):myString.find(')')].replace('-', ' ').replace('_', ' ').capitalize()
# same thing but more readable:
start = myString.find('(')
end = myString.find(')')
substring = myString[start:end]
noDashes = substring.replace('-', ' ').replace('_', ' ')
newString = noDashes.capitalize()

#Accessing a file for read or write
file = open('instructions.txt', 'r')
contents = file.read() #will read the whole file and store it into the string (called contents  here)
allLines = file.readlines() #will read all lines in a List of strings (called allLines here)
aLine = file.readline() #will read the next line into a string (called aLine here)

#write a file - (1) overwrite, (2) append
#Really important to remember to call close(), otherwise writing may fail
#option1: overwrite
file = open('instructions.txt', 'w')
file.write("This will replace whatever the file contained before")
file.close()
#option2: append
file = open('instructions.txt', 'a')
file.write("This will appended at the end of the contents")
file.close()

file.write("A new line character here \n means that this will go in the next line")

#create a file - no explicit function, If a file does not exist when attempting to open it for writing it will be created
open('someFile.txt', 'w')

#Where's the file?
#When you open a file, the filename argument is the path to the file you want to open.
#The path can be (1) relative or (2) absolute
# (1) Relative: A path relative to where your python file is located
file = open("results.txt", "w") #Your python file and results.txt file must be in the same folder

# (2) Absolute: The “whole” path to the file you want to open, irrespective of where your python file is located
file = open ("X:/projects/resources/results.txt", "w")

#CSV files
file = open('results.csv', 'w')

#reading a directory
#To list the contents of a folder we need another import statement:
from os import listdir #at the top of your program
