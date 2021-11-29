import string
import random
from typing import final

#Create alphabets
def createAlphabets(): 
    global alphabet, atbashAlphabet, a1z26
    alphabet = list(string.ascii_letters)

    lowerAlphabet = list(string.ascii_lowercase)
    lowerAlphabet.reverse()
    upperAlphabet = list(string.ascii_uppercase)
    upperAlphabet.reverse()
    atbashAlphabet = lowerAlphabet[:]
    atbashAlphabet += upperAlphabet[:]

    a1z26 = []
    [a1z26.append(number+1) for number in range(0, 26)]
    [a1z26.append(number+1) for number in range(0, 26)]

#There's no supervillian without a presentation
def presentation():
    global phrase
    print("____________________________________________________________________________")
    print("\n\t\tWelcome to the Password Creator program")
    print("____________________________________________________________________________")
    print("\nPlease, enter a phrase ")
    phrase = input(": ")

#Adjusments
def adjustments():
    global phrase
    a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
    trans = str.maketrans(a,b)
    phrase = phrase.translate(trans)

#Change string to list
def stringToList(): 
    global lettersList
    lettersList = [char for char in phrase]

#Index number in the alphabet
def core():
    global finalList
    finalList = []
    for letter in lettersList: 
        if letter.isspace(): pass
        else: 
            letterInAlphabet = alphabet.index(letter)
            indexNumber = letterInAlphabet+1
            
        #Create random decision
        letter_Number = random.randint(0, 6)
        
        #Letter
        if letter_Number >= 1:
            if letter.isspace(): toAssign = " "
            else: toAssign = atbashAlphabet[indexNumber-1]
            
        #Number
        if letter_Number == 0: 
            if letter.isspace():  toAssign = " "
            else: toAssign = a1z26[indexNumber-1]

        finalList.append(str(toAssign))

#List to String
def listToString(wordList):
    global listToStr 
    finalList.insert(0, "@")
    listToStr = ""
    listToStr += ''.join(str(element) for element in wordList)
    listToStr = listToStr.replace(" ", "")
    return listToStr

presentation()
createAlphabets()
adjustments()
stringToList()
core()

#Process
while True: 
    
    print("Here's your password: ")
    print(listToString(finalList))
    
    print("\nChoose 'yes' / 'no' ")
    option = input("Would you like to refresh the password: ")
    option = option.lower()
    option = option.strip()
    
    if option == "yes" or option == "y": 
        core()
        continue
    if option == "no" or option == "n": 
        print("Thank you for use our program <3")
        break

