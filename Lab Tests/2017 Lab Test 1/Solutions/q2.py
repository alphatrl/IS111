# start of answer
def generate_digits(sentence):

  # if character found in letter_list, the index of letter_list equal to digit_list
  letter_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
  digit_list = [2, 3, 4, 5, 6, 7, 8, 9]
  digit_convert = ''

  for char in sentence:
    for index in range(len(letter_list)):
      letter_string = letter_list[index]
      # if equal or more than 0, letter is found
      if letter_string.find(char) >= 0:
        digit_convert += str(digit_list[index])
        break # exit for loop once found

  return digit_convert # added so that this script will run. feel free to modify it
# end of answer



print('Test 1: Check if the return value is a str object')
print('Expected:True')
print('Actual  :' + str(isinstance(generate_digits('A'), str)))
print()


print('Test 2')
print('Expected:2')
print('Actual  :' + generate_digits('A'))
print()

print('Test 3')
print('Expected:79846642')
print('Actual  :' + generate_digits('PYTHONIC'))
print()



print('Test 4')
print('Expected:53354448')
print('Actual  :' + generate_digits('LEDLIGHT'))
print()
