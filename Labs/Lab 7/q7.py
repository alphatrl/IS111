# Created by Amos Tan for students to reference their lab work
# Q7

# Write your code here:
import random

def shuffle_string(word):
    char = list(word)
    
    # return word if word is:
    # ee
    # h
    if (len(word) == 2 and char[0] == char[1]) or (len(word) == 1):
        return word
    
    random.shuffle(char)
    new_word = ''.join(char)
    
    # shuffle string again if it is the same
    if new_word == word:
        new_word = shuffle_string(word)
        
    return new_word

def reorder_string(word):
    # deal with special characters
    # save index of special char if found
    index = -1
    special_char = ".'!?,:"
    char_in_word = ''
    count = 0
    
    for char in word:
        if char in special_char:
            char_in_word = char
            index = count
        count += 1
    
    # remove special char in word
    # shuffle middle contents
    # save as new word
    word = word.replace(char_in_word, "")
    new_word = word[0] + shuffle_string(word[1:-1]) + word[-1]
    
    # add back the special char into word at the index saved
    if index != -1:
        word_list = list(new_word)
        word_list.insert(index, char_in_word)
        new_word = ''.join(word_list)

    return new_word


# MAIN METHOD
FILE_NAME = "talk.txt"
quotes = []

with open(FILE_NAME, 'r') as input_file:
    for line in input_file:
        line = line.rstrip('\n')
        col = line.split(' ')
        quotes.append(col)
        
# print(quotes)

for quote in quotes:
    new_quote = ''
    for word in quote:
        # if word is more than 2 char
        if len(word) > 2:
            # ignore numbers
            if not word.isnumeric():
                word = reorder_string(word)
        new_quote += word + ' '
        
    print(new_quote)
