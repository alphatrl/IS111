# start of answer
def get_longest_word(first, second, third):

  longest_word = ''
  word_list = [first, second, third]

  for word in word_list:
    if len(word) > len(longest_word):
      longest_word = word

  return longest_word

# end of answer

print('Test 1')
print('Expected:abc')
result = get_longest_word ('', 'a', 'abc')
print('Actual  :' + result)
print()

print('Test 2')
print('Expected:abcd')
result = get_longest_word ('abcd', 'a', 'ab')
print('Actual  :' + result)
print()

print('Test 3')
print('Expected:strawberry')
result = get_longest_word ('orange', 'strawberry', 'x')
print('Actual  :' + result)
