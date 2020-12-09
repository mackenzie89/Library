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

########### Lecture 6 - Writing Functions #########################

# To define a function: add the keyword def
    # add the name of the function (same rules as with naming variables)
    # add brackets
    # indent the code that you wish to be part of the function

#To use a function:
# use its name followed by brackets
getDate()
    dateString = file_contents[1].partition(': ')[2]
    year = dateString[4:8]
    month = dateString[2:4]
    day = dateString[0:2]
    date = f"{day}/{month}/{year}“

getDemographics()
    demographics = file_contents[3].split(",")
    name = demographics[0]
    age = demographics[1]
    normalised_gender = demographics[2].lower()
    if "female" in normalised_gender:
        gender = 2
    else:
        gender = 1

#Defining a function does not execute its contents - You need to call it for that

# Add a parameter inside the brackets
# This is what’s coming from outside, from the caller
# This is what the function does not know about
# This is what will be changing every time the function is called
#
# So, when calling the function
# len(myFiles) 	 x will be the value of myFiles
# len(lines) 	 x will be the value of lines
#
# Compute the length of x, assuming that x will be some list (not a particular list)
#
# Return to the caller the result of the computation (keyword return)

# Definition

def wordCount(fileName, word)
        ………
# usage
        wordCount(fileName, word) #or wordCount(theFile, w)

#You can sort a list using sorted(aList) or aList.sort(). What’s the difference?
# “sort” is affecting the list itself (in-place) and “sorted” gives you back another list

#end of a function
#It is better to return a value for the caller to print, rather than print inside the function.
# Your function should be as generic as possible and make the least possible commitments
def addition(a, b):
        sum = a + b
        print(sum)
        print(“Summation
        done”)
#no return value vs
def addition(a, b):
        sum = a + b
        return sum
        print(“Summation
        done”)
# returns a value

#A function defines its own scope. Variables have their own meaning (value) inside the function.
        # Variables declared outside a function are not accessible inside the function
#Variables declared with the keyword “global” are accessible anywhere in the file.
#A function must be defined before being used (as with variables).

#Importing from other files: Modules A file containing python code is called a module
import demographics
yourAge = demographics.getAge()

#Three ways of importing/using definitions from a module
# Import the whole module, use function qualified by their module
import demographics
yourAge = demographics.getAge()

# Import some functions, use them unqualified
from demographics import getAge, minAge
yourAge = getAge()

# Import all the functions from the module, use them unqualified
from demographics import *
yourAge = getGender()

#In the random module there are many functions besides randint
import random	 now functions must be qualified by random.

random.shuffle(aSequence)	 randomly shuffles the elements of the sequence
random.choice(aSequence) 	 returns one element from the sequence chosen 	randomly

random.uniform(min, max)	 returns a sample (float) from a uniform distr
random.normalvariate(mn, sd)	 returns a sample from a normal distr
essentially identical to random.gauss(mn, sd)
random.expovariate	 returns a sample from a exponential distr
random.betavariate(a,b)	 returns a sample from a beta distr
random.gammavariate	 returns a sample from a gamma distr

#A module is just a .py file
# A package is a directory (a folder) containing one or more modules (.py files)
# A library contains one or more packages (often just one)
# There is a ridiculous number of libraries out there
# Some of the most useful for psychologists are:
# numpy: scientific computing, linear algebra
# scipy: uses and extends numpy, used for statistical analysis (yes t-test!). Look at scipy.stats
# matplotlib: plotting package
# PyGame: Used for 2D game development (and experiments if you’re brave)
# NLTK: Natural Language Toolkit, advanced string manipulation useful in linguistics
# Requests: contacting the web
# PsychoPy: Used in experiments, especially psychophysics
# PyQT: Used for UI design, coming in week 7
# (Django)

#Adding a library in PyCharm
#Go to
# File > Settings on Windows
# PyCharm>Preferences on macOS
# Then go to Project>Project Interpreter
# Select the interpreter you want to add the library to
# usually just a single interpreter. If more than one, make sure it’s Python3xxx not Python2xxx
# Click the plus icon (right on Windows, lower left on macOS)
# Type in the library name (be careful! there are many similar names)
# Make sure that the option to “install to user’s site packages directory”, at lower left is NOT selected.
# Click Install Package
# Wait for PyCharm to install the library and update the interpreter


######################## Lecture 7 OOP and UI ##########################

#With Object-Oriented Programming (OOP) you go a step further:
# you define new types/classes (like int, str and List) that
# have their own properties (variables)
# have their own behaviour (methods)

myStr = “one two three four”
spaceAt = myStr.index(“ “)
nums = myStr.split(“, “)
nums.append(“five”)
nums.sort()



# first argument in every method, is a reference to the object – usually named self
#Within the class the attribute is accessed through “self”, i.e. “the walls of current object”

#definition
        class House:
            def Build(self):
                self.numOfWalls = 4

            def Demolish(self):
                self.numOfWalls = 0
# usage
myHouse = House()
myHouse.Build()
print(myHouse.numOfWalls) # will print 4

myHouse.Demolish()
print(myHouse.numOfWalls) # will print 0

# Outside the class it is accessed by the variable name
        # i.e. “the walls of that object”

#accessing attributes:

#Internal call - Within the class the variable or method is accessed through self (mine)
#External call - Outside the class the variable or method is accessed through the variable name

#We create an object by using the class name followed by brackets:
aHouse = House()
myBoxer = Boxer()
# There’s a special method __init__ that is called when an object is created
#With __init__ you can set things up before any other method is called

        class Animal():
            def __init__(self):
                self.weight = 40

            def Eat(self, calories):
                self.weight = self.weight + calories

        anAnim = Animal()
        anAnim.Eat(20)

#We can also have arguments in the constructor that parametrize the way the object is initialized

    class Animal():
        def __init__(self, startingWeight):
            self.weight = startingWeight

        def Eat(self, calories):
            self.weight = self.weight + calories


    aSmallAnimal = Animal(4)
    aHugeAnimal = Animal(1400)

#classes -defining the parent

#A class without parent (doesn’t inherit anything)
class Orphan:
   def MethodA(self):

    #Classes with parents
    class Dog(Animal)
        def Run(self):
            ………

        def Walk(self):
            ………

    class Boxer(Dog):
        def Snore(self):
           ………

#overriding a method
#Sometimes we want to inherit the majority of the structure of a class.so we’ll extend that class (subclass),
class NewClass(OldClass):

#Accessing the parent: super()
super() #to access the parent version

#GUI interfacing with the code
#When you drag a button into a window:
#A QPushButton object is created:
pushButton = QPushButton()
#Certain properties of the button are set:
pushButton.X = 350
pushButton.Y = 100
pushButton.Width = 170
pushButton.Height = 51
pushButton.setText(“PushButton”)
#When you double click to change the text
pushButton.setText(“some Text”)
#When you drag around:
pushButton.X = 500


################ Lecture 8 - Interacting with GUIs ############################


from PyQt5 import uic #Import PyQt modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) #Create a QApplication: controls the execution of your UI app
app = QApplication([])

window = uic.loadUi("mywindow.ui") #Import your interface

# Your code here!

window.show() #Make the main window visible
app.exec_() #Execute your application and wait until it exits (user clicks X button)

#make sure .ui file is in the same folder as your .py code

#All widgets are properties of the window, e.g.
window.buttonPlease = QPushButton() #nb window is just a variable name

#accessing widgets
        window = uic.loadUi("mywindow.ui")

        # Get input for name and age
        userName = window.txtName.text() # variable = window.nameofwidget.nameoftheproperty()

        userAge = window.txtAge.text()

        # set text in lblWelcome label
        window.lblWelcome.setText(“Hello!”)

        window.show()
        app.exec_()

#You get the value of the property by:
window.widgetName.propertyName()
#You set the value of the property by:
window.widgetName.setPropertyName()


# Examples:

    window.label.text()    window.label.setText(“new text goeshere”)
    window.label.wordWrap()    window.label.setWordWrap(False)
    window.label.margin()     window.label.setMargin(20)
    window.lineEdit.text()     window.lineEdit.setText(“strange choice”)
    window.lineEdit.placeHolderText()  window.lineEdit.setPlaceHolder(“Please write something”)

    #exceptions
    window.checkbox.isChecked()     window.checkbox.setChecked(True)
    window.myWidget.isVisible()     window.myWidget.show() /  window.myWidget.hide() #shows or hides widget

#Getting and setting properties

#Font
    newFont = QFont("Arial", 12) # QFont("font family", font size
    window.label.setFont(newFont)

#Geometry

   newDimensions = QRect(200, 300, 100, 30) # QRect(left, top, width, height)
   window.label.setGeometry(newDimensions) # can also do window.label.setGeometry(200,300,100,30)

#Getting and setting Colours
aLabel = window.label # get the widget
aLabel.setAutoFillBackground(True)
labelColours = aLabel.palette()


#set the colour of the palette
labelColours.setColor(QPalette.Window, QColor(”red”))
#get the palette #QPalette.Window, QPalette.Text, QPalette.Base etc
#and the colour using a QColour object, e.g. QColour(“red”) or QColour(255, 0, 0) - RGB
aLabel.setPalette(labelColours)

#Signals
        # QWidget	 show, hide 	(so, all widgets that inherit from Qwidget emit these signals)
        # QPushButton   	 clicked
        # QRadioButton	 clicked
        # QPlainTextEdit 	 textChanged

        # QLineEdit  	 textChanged(String)  i.e. the text is emitted with the signal
        # QSpinBox	 valueChanged(int)
        # QComboBox	 currentIndexChanged(int) or  currentIndexChanged(String)

#To react to a signal:
sender.signal.connect(ourFunction) # thewidget.thesignal.connect(thenameofourfuncation)
window.aButton.clicked.connect(updateText)

# example: error label

PyQt5 import uic
from PyQt5.QtCore import *from PyQt5.QtGui import *from PyQt5.QtWidgets import *

app = QApplication([])

window = uic.loadUi("demographics.ui")

window.lblError.hide() #hides label on window opening

def checkText():#defines function of checking text and showing error message if name is blank
	if window.txtName.text()== "" :
		 window.lblError.setText("Please input your name before clicking submit")
		 window.lblError.show()
	else:
		 window.lblError.hide()

window.btnSubmit.clicked.connect(checkText) #checks name on click of submit button


window.show() #executes showing the window
app.exec_() #runs the code until X is clicked

#signal carrying information

#Sometimes the signal is passing arguments too. For example, the textChanged signal (lineEdit Widget) passes the text that the user has inputted
#In that case the function you connect to, must have the correct number (and type) of arguments, otherwise it will not be called.

window = uic.loadUi("demographics.ui")

window.lblError.setText("")

def nameChanged(newText):

window.lblError.setText(newText)
window.txtName.textChanged.connect(nameChanged)
window.show()
app.exec_()

#Common Signals
window.aButton.clicked.connect(onUserClick)
window.aButton.pressed.connect(onMouseDown)
window.aButton.released.connect(onMouseUp)
window.checkbox.stateChanged.connect(onStateChanged)  #-- requires “state” argument (0 is unchecked, 2 is checked)
window.txtControl.textChanged.connect(onEdit) #-- requires “text” argument
window.txtControl.selectionChanged.connect(onTextSelected) #-- requires “text” argument
window.slider.valueChanged.connect(onSliderDragged) #– requires “value” argument
window.combobox.currentIndexChanged.connect(onChange) #– requires “index” argument

#Sometimes you have one slot for many signals e.g. many similar buttons calling the same function to avoid code duplication
window.sender() #If you want to know which of them sent the signal, use window.sender() inside the slot function, i.e. the funciton handling the click, event the textChanged event etc
def aButtonClicked():
	theClickedOne = window.sender()

#Remember: functions can’t access variables declared outside their scope: Solution Global Variables

name = None
def onSubmit():
	global name
	name = window.txtName.text()

window.btnSubmit.clicked.connect(onSubmit)

#this will work, but global variables are not ideal – may lead to variable names clashing etc…
# Avoid global! Solution: Write Object oriented code

def __init__():
	self.name = none
	self.window.btnSubmit.clicked.connect(onSubmit)


def onSubmit():
	self.name = self.window.txtName.text()


#Alternatively make variables properties of your window

window.name = “Christos”
def onSubmit():
	window.txtName.setText(window.name)

window.btnSubmit.clicked.connect(onSubmit)

#Qtimer (not a widget)

    #To use it:create a new QTimer object
    myTimer = QTimer()
    # connect its “timeout” signal to the function you want to repeat
    myTimer.timeout.connect(funToRepeat)
    # start the timer, indicating the interval in milliseconds
    myTimer.start(2000) # execute funToRepeat every 2 seconds
    # Some useful methods of QTimer:
    myTimer.setInterval(xxx) # change the interval
    myTimer.setSingleShot(True) #will fire once after the interval
    myTimer.stop() # stop it (e.g. after a countdown)

#Creating and adding a widget in code

aLabel = QLabel(window)

#now the label is created and added but it has no text, size or position
#simply set the properties as before
aLabel.setText(“In code!”)
aLabel.setGeometry(200, 40, 100, 30)

#Adding widgets late and showing them
    #Any widget added after window.show() will be invisible.
    ##Your code here!
window.show()

################ Lecture 9 ############################

#Containers for experiments

#QStackedWidget

children() #gives you access to a list of QWidgets (pages) + a layout object
    window.nextButton == window.container.children()[0]
count() #tells you how many pages you have
currentIndex() #tells you which widget in the list is currently visible - returns integer
setCurrentIndex(num) #to go to a page - useful for moving to next page button
        window.myStackedOne.setCurrentIndex(window.myStackedOne.setCurrentIndex()+1) #example of how to use to increment the page

#creating your own widgets

#e.g want a button that displays images - in python picture can only be a label. Therefore need to create own widget

#Start from an existing widget and make a subclass to override with your needs/add functionality

   class Dog(): #parentclass
       def __init__(self, energyRate): #setting the constructor
           self.energyConsumptionRate = energyRate
           self.position = [0, 0]
           self.thing = None

       def sleep(self): #always have self at the beginning
           self.energyConsumptionRate = 0.1 #always have self at the beginning

       def goToThing(self, anObject):
           self.position = anObject.position

       def goBack(self):
           self.position = [0, 0]

       def grabThing(self, aThing):
           self.thing = aThing

#If you define a new __init__ in your subclass, you should call the parent’s initialiser in your new definition (by including the line “super().__init__()”, which will call & execute the __init__ you are overwriting). This is a way of keeping the old __init__ but then adding any new properties you might want to include in your subclass.


#creating the subclass

   class Bulldog(Dog): #adds method in addition to the parent class
       def barkNonStop(self):
           self.energyConsumptionRate = 0.9

#creating a widget in code - create a widget library either in separate files or one

   window = uic.loadUi(“mywindow.ui")
   aLabel = QLabel(window) #now the label is created and added but it has no text, size or position
   aLabel.setText(“In code!”) #simply set the properties as before
   aLabel.setGeometry(200, 40, 100, 30)
   window.show() #closes
   app.exec_()

#To change the background colour of a widget, e.g. QLabel we need to write many lines
   window.myLabel.setAutoFillBackground(True)
   myPalette = window.myLabel.palette()
   myPalette.setColor(QPalette.Window, QColor(“red”))
   window.mLabel.setPalette(myPalette)
#what if part of our program is to change the colour of a label hundreds of times?
#It’d be nice to simply write myLabel.setColour(“red”) but QLabel doesn’t have such method

#create own Label .e.g for above


class MyOwnLabel(QLabel): #creates subclass of label with my special properties

       def __init__(self,container, text):
           super().__init__(container) #as setting constuctor need to initialise parent too using super()
           self.setText(text)

       def setBackground(self, colour): #creating the function to set colour = needs use refer to self compared to function above
           self.setAutoFillBackground(True)
           myPalette = self.palette()
           myPalette.setColor(QPalette.Window, QColor(colour))
           self.setPalette(myPalette)

#best practice to create in separate file and import it

#making a label blinkable - animations use timings

lblColour = ColouredLabel(window)
lblColour.setText("I have colour")
lblColour.setGeometry(200, 40, 300, 80)
lblColour.blink("yellow“, “blue”)

   class ColouredLabel(QLabel): #creating new subclass of QLabel
       def setColour(self, colorString):
           self.setAutoFillBackground(True)
            myPalette = self.palette()    myPalette.setColor(QPalette.Window, QColor(colorString))    self.setPalette(m
           yPalette)

       def blink(self, color1, color2): #defining the blink function
           self.blinkColour1 = color1
           self.blinkColour2 = color2
           self.currentColour = color1
           self.blinkTimer = QTimer()
           self.blinkTimer.timeout.connect(self.onBlink)
           self.blinkTimer.start(500)

       def onBlink(self):
           if self.currentColour == self.blinkColour1:
               self.currentColour = self.blinkColour2
           else:
               self.currentColour = self.blinkColour1
           self.setColour(self.currentColour)

#Can add even more arguments to give more control over how our label blinks

def blink(self, color1, color2, speed=500, times = -1):
	self.blinkColour1 = color1
    self.blinkColour2 = color2
    self.blinkFor = times #setting number of times to blink
    self.currentBlink = 0 #starting counter
	self.currentColour = color1 #defines current colour
	self.blinkTimer = QTimer()
	self.blinkTimer.timeout.connect(self.onBlink) #connect to signal
	self.blinkTimer.start(speed)

def onBlink(self):
	if self.currentColour == self.blinkColour1:
		self.currentColour = self.blinkColour2
	else:
		self.currentColour = self.blinkColour1
	self.setColour(self.currentColour)

	if self.currentBlink==self.blinkFor:
     	self.blinkTimer.stop()
     self.currentBlink += 1


#Making a clickable label - only buttons can be clicked, but want a label (image) that can be clicked.

#in a new py file: e.g. ClickableLabel.py or myWidgets.py

    class ClickableLabel(QLabel):
        clicked = pyqtSignal()

        def mousePressEvent(self, mouseEvent):
            self.clicked.emit()

#in our main file:
    from ClickableLabel import * #name of py file not class
    ……
    myLabel = ClickableLabel(window)
    myLabel.setText("I have colour“)
    myLabel.setGeometry(200, 40, 300, 80)
    myLabel.clicked.connect(myFunctionToDoSmWhenLabelClicked)

#creating a clickable label

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, mouseEvent):
        self.clicked.emit() #will be triggered on any click


    def mousePressRightClick(self, mouseEvent):
        if mouseEvent.button() == 2: #will only emit on right click
            self.clicked.emit()

# The argument mouseEvent, is of type QMouseEvent with properties:
# button():  the mouse button that caused the event, 1 for left click, 2 for right click
# x(), y():  position of the cursor at the time of the event relative to its container
# globalX(), globalY(): position of the cursor at the time of the event relative to the window


#Example 4: A container that listens to the keyboard

# in a new py file: e.g. KeyboardWidget.py or myWidgets.py

class KeyboardWidget (QWidget): #Subclass a widget that is closest to our needs
    keyPressed = pyqtSignal(str)

    def keyPressEvent(self, keyEvent): #Extend the widget by adding functionality:
        self.keyPressed.emit(keyEvent.text())

# in our main file-
from KeyboardWidget import * #name of py file not class

myWidget = KeyboardWidget(window) #Create and add a KeyboardWidget to our window
myWidget.setGeometry(200, 40, 500, 500)
myWidget.setFocus() #otherwise keyPressEvent won’t be called
myWidget.keyPressed.connect(myFunctionToDoSmWhenKeyIsPressed)

#Focus

window.focusWidget() #will return the widget that has the focus
someWidget.setFocus() #will set the focus to someWidget (provided its window is active)
#Makes sense to override mousePressEvent too, to control focus!


#Animation

def animate():
    currentX = window.balloon.x()
    window.balloon.setGeometry(currentX+10,130, 240, 240)
timer = QTimer() #Create a QTimer that emits a signal every 50 milliseconds or so (depending who smooth you need the animation to be)
timer.timeout.connect(animate) #In the slot connected to the QTimer edit the properties of the widgets you want to animate
timer.start(50)

#example
def animate():
    currentRight = window.balloon.x() + window.balloon.width()
    if currentRight > window.pin.x():
        window.balloon.hide()
        window.pop.show()
    else:
        window.balloon.setGeometry(window.balloon.x() + 10, 130, 240, 240)


window.pop.hide()
timer = QTimer()
timer.timeout.connect(animate)
timer.start(50)

# Layout - see ppt





