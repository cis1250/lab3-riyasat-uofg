#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

#!/usr/bin/env python3
import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# Prompt the user for a valid sentence
user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Split the sentence into words (lowercase, remove punctuation)
words = re.findall(r'\b\w+\b', user_sentence.lower())

# Create lists to store unique words and their frequencies
word_list = []
frequency_list = []

for word in words:
    if word in word_list:
        idx = word_list.index(word)
        frequency_list[idx] += 1
    else:
        word_list.append(word)
        frequency_list.append(1)

# Print the word frequencies
for i in range(len(word_list)):
    print(f"{word_list[i]}: {frequency_list[i]}")

