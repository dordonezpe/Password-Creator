import string
import random

#Password Creator v1.0.
#David Fernando Ordoñez Pérez - dordonezpe

#1. Creates the alphabets
def createAlphabets(): 
    global atbash, a1z26, alphabet
    alphabet = list(string.ascii_lowercase)
    
    atbash = alphabet[:]
    atbash.reverse()
    a1z26 = []
    [a1z26.append(number+1) for number in range(0, 26)]
createAlphabets()

#2. There's no supervillian without a presentation
def presentation(): 
        global phrase
        print("____________________________________________________________________________")
        print("\n\t\tWelcome to the Password Creator program")
        print("____________________________________________________________________________")
        print("\nPlease, enter a phrase ")
        userPhrase = input(": ")
        phrase = userPhrase.lower()
        #phrase = phrase.replace(" ", "")
        phrase = phrase.replace("ñ", "n")
        print("phrase: " + phrase)
presentation()

#3. Change string to list
def split(word):
    global lettersList
    lettersList = [char for char in word]
    return lettersList
print(split(phrase))

#4. Whole process!
def processCore():
    global finalList
    finalList = []
    i = lettersList #Take the value of the list of characters from the phrase

    for letter in lettersList:   #lettersList = k, a, l, o, s, k, a, g...
        #print()
        if letter.isspace(): #True
            pass
        else:
            letterInAlphabet = alphabet.index(letter) #Search the position in the alphabet
            indexNumber = letterInAlphabet+1 #Position - number in lettersList: 1, 2, 3, 4, 5...
        randomLetter_Number = random.randint(0, 1) #Create a value: 0 or 1
        #print(f"random number / letter: {randomLetter_Number}")

        #a. Assign a letter
        if randomLetter_Number == 0:   
        #   print("Reverse letter")
            if letter.isspace(): 
                letterNumberToAssign = " "
        #        print("Letter is space")
            else:
                letterNumberToAssign = atbash[indexNumber-1] #Assign a letter to the letter in letterList
        #        print(f'letterNumbertoAssign {letter}: {letterNumberToAssign}')
        #b. Assign a number
        if randomLetter_Number == 1:     
        #    print("Number") 
            if letter.isspace(): 
                letterNumberToAssign = " "
        #        print("Letter is space")
            else: 
                letterNumberToAssign = a1z26[indexNumber-1] #Assign a number to the letter in letterList
        #        print(f'letterNumbertoAssign {letter}: {letterNumberToAssign}')
        
        finalList.append(str(letterNumberToAssign))
        print(f'finalList: {finalList}')
processCore()

#5. Change list to string
def listToString(wordList): 
    finalList.insert(0, "@")
    listToStr = ""
    listToStr += ''.join(str(element) for element in wordList)
    return listToStr

while True: 
    
    #6. Answer to the user
    def answer(): 
        print(f"Here's your password: ")
        print(listToString(finalList))
    answer()
        
    print("\nWould you like to refresh the password?")
    option = input("Enter yes or no: ")
    option = option.lower()
    option.replace(" ", "")

    if option == "yes" or option == "y": 
        processCore()
        continue
    elif option == "no" or option == "n": 
        break
    else: 
        print("Invalid option")
        continue
    
print("\nThank you for use our program!")




#C:\Users\David Ordoñez\Desktop\Software Pillar\CodingPrograms\Password Creator