import random

text = open("kafka.rtf").readlines()

for line in text:
  line = line.strip()
  words = line.split(" ")
  random.shuffle(words)

  words = sorted(words) # Sort the words list alphabetically

  new_line = " ".join(words)

  print(new_line)
