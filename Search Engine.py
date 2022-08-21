#The given code takes a text and a word as input and passes them to a function called search().
#The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
def search(x,y):
    if(y in x):
        return("Word found")
    else:
        return("Word not found")
text = input()
word = input()
print(search(text, word))
