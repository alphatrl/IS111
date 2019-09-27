# start of answer

def find_tags(sentence):
  tag_list = []
  length = len(sentence)
  count = 0

  while count < length:
    # if a [ is found case
    if sentence[count] == '[':
      count += 1
    
      tag = str(len(tag_list) + 1) + '-'
      while sentence[count] != ']':
        tag += sentence[count]
        count += 1
      tag_list.append(tag)

    else:
      count += 1
  return ','.join(tag_list)

# end of answer


print('Test 1')
actual = find_tags('Coding[Rocks]')
print('Expected:1-Rocks')
print('Actual  :' + actual )
print()

print('Test 2')
actual = find_tags('[apple]and[orange]and[apple]again!')
print('Expected:1-apple,2-orange,3-apple')
print('Actual  :' + actual)
print()

print('Test 3')
actual = find_tags('IAmTaking[mrt]To[SMU]ButThe[nel]IsDelayedAgain.')
print('Expected:1-mrt,2-SMU,3-nel')
print('Actual  :' + actual)
print()

print('Test 4')
actual = find_tags('')
print('Expected:><')
print('Actual  :>' +  actual + '<' )
print()

print('Test 5')
actual = find_tags('apple')
print('Expected:><')
print('Actual  :>' +  actual + '<' )
print()
