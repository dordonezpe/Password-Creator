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

#21Nov21
def createAlphabets(): 
    global atbash, a1z26, alphabet
    alphabet = list(string.ascii_lowercase)
    
    atbash = alphabet[:]
    atbash.reverse()
    a1z26 = []
    [a1z26.append(number+1) for number in range(0, 26)]
createAlphabets()

finalList = []
i = lettersList #New
print(i)
print()
for letter in lettersList:   #lettersList = k, a, l, o, s, k, a, g...
    letterInAlphabet = alphabet.index(letter)
    indexNumber = letterInAlphabet+1 #Position - number in lettersList: 1, 2, 3, 4, 5...
    randomLetterNumber = random.randint(0, 1) #Create a value: 0 or 1
    
    print(f'IndexNumber: {indexNumber}')
    print(f'random Letter Number: {randomLetterNumber}')
        #Assign a letter
    if randomLetterNumber == 0:      
        letterNumberToAssign = atbash[indexNumber-1]
        print(f'letterNumbertoAssign: {letterNumberToAssign}')
        #Assign a number
    if randomLetterNumber == 1:      
        letterNumberToAssign = a1z26[indexNumber-1]
        print(f'letterNumbertoAssign: {letterNumberToAssign}')
    
    print()
        
    finalList.append(str(letterNumberToAssign))
    print(f'finalList: {finalList}')
        
#Change list to string
def listToString(wordList): 
    listToStr = "@"
    listToStr += ''.join(str(element) for element in wordList)
    return listToStr
print(listToString(finalList))





#C:\Users\David Ordoñez\Desktop\CodingPrograms\Password Creator