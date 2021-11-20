#Password Creator v1.0.
#David Fernando Ordoñez Pérez - dordonezpe
#20Nov21

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# TASKS: 
# [x] Create the basic (rudimentary) idea of how it works. 
# [x] Change a string to list.
# [x] Change list to string. Return with @ symbol.

# FEEDBACK: 
# You can always find the answer if you search for it.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#There's no supervillian without a presentation
print("____________________________________________________________________________")
print("\n\t\tWelcome to the Password Creator program")
print("____________________________________________________________________________")
print("\nPlease, enter a phrase ")
userPhrase = input(": ")
phrase = userPhrase.lower()
phrase = phrase.strip()

#Change string to list
def split(word):
    global lettersList
    lettersList = [char for char in word]
    return lettersList

#Change list to string
def listToString(wordList): 
    listToStr = "@"
    listToStr += ''.join(str(element) for element in wordList)
    return listToStr

#21Nov21
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# TASKS: 
# [] Create the Atbash and A1z26 cypher in a list. 
# [] .
# [] .

# FEEDBACK: 
# .
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""







#C:\Users\David Ordoñez\Desktop\CodingPrograms