import string
import random

#Password Creator v1.0.
#David Fernando Ordoñez Pérez - dordonezpe
#20Nov21

#There's no supervillian without a presentation
def presentation(): 
    global phrase
    print("____________________________________________________________________________")
    print("\n\t\tWelcome to the Password Creator program")
    print("____________________________________________________________________________")
    print("\nPlease, enter a phrase ")
    userPhrase = input(": ")
    phrase = userPhrase.lower()
    phrase = phrase.strip()
presentation()

#Change string to list
def split(word):
    global lettersList
    lettersList = [char for char in word]
    return lettersList
print(split(phrase))

#Change list to string
def listToString(wordList): 
    listToStr = "@"
    listToStr += ''.join(str(element) for element in wordList)
    return listToStr
print(listToString(lettersList))

#21Nov21
def createAlphabets(): 
    alphabet = list(string.ascii_lowercase)
    
    atbash = alphabet[:-1]
    atbash.reverse

    a1z26 = []
    [a1z26.append(number+1) for number in range(0, 26)]
createAlphabets()

randomNumber = random.randint(0, 26)
print(randomNumber)







#C:\Users\David Ordoñez\Desktop\CodingPrograms\Password Creator