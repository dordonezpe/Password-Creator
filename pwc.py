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

    a1z26, finalList = [], []
    [a1z26.append(number+1) for number in range(0, 26)]
    [a1z26.append(number+1) for number in range(0, 26)]

#There's no supervillian without a presentation
def presentation():
    phrase = input("Enter a phrase: ")

#Adjusments
a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
trans = str.maketrans(a,b)
phrase = phrase.translate(trans)

#Change string to list
lettersList = [char for char in phrase]

#Index number in the alphabet
for letter in lettersList: 
    if letter.isspace(): pass
    else: 
        letterInAlphabet = alphabet.index(letter)
        indexNumber = letterInAlphabet+1
        
    #Create random decision
    letter_Number = random.randint(0, 4)
    print(f"Random Number: {letter_Number}")
    
    #Letter
    if letter_Number >= 1:
        if letter.isspace(): toAssign = " "
        else: toAssign = atbashAlphabet[indexNumber-1]
        
    #Number
    if letter_Number == 0: 
        if letter.isspace():  toAssign = " "
        else: toAssign = a1z26[indexNumber-1]

    finalList.append(str(toAssign))

finalList.insert(0, "@")
listToStr = ""
listToStr += ''.join(str(element) for element in finalList)
listToStr = listToStr.replace(" ", "")

print("Here's your password: ")
print(listToStr)

