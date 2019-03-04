
import random
#text = open("harrypotter1.txt").read()

text = open("harrypotter1.txt").readlines()
for line in text:
    line = line.strip()
    words = line.split(" ") # Separates the lines by an empty space, getting a list of words

random_word = random.choice(words)  #Get a random item from the word list
new_line = " ".join(words) # Joins each element in the list by sticking the space character in between the words, outputs a string

print new_line


#print(text) # Outputs: the entire text
