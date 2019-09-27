def print_dancing_string(sentence, start):
  # write your answer between #start and #end
  #start
  
  # list_top, list_mid, list_btm is stored in a list in that order

  list_top = []
  list_mid = []
  list_btm = []
  string_list = [list_top, list_mid, list_btm]

  # point will be used to keep track of where to save the character into the string
  # if point = 0, save char into string_list[0]
  # else save a space ' ' into the other strings stored in string_list

  # go_up is used to determine whether the character is 'moving up' to the line above
  # is true, point = point - 1, this means the next character in sentence should be store in string_list[point - 1]
  # if false. point = point + 1, this means the next character should be stored in string_list[point + 1]

  # save position and goUp accordingly
  if start =='T':
    go_up = False
    point = 0
  elif start =='M':
    go_up = True
    point = 1
  elif start == 'B':
    go_up = True
    point = 2

  for char in sentence:
    
    # add character into string
    for string_index in range(len(string_list)):
      add_char = ' '
      if string_index == point:
        add_char = char
      # now add char to the respective list
      string_list[string_index].append(add_char)

    # update next position of char
    # if going_up and point = 0, means i have reach the top,
    # update going_up to false, and point to point + 1
    if go_up:
      if point == 0:
        point += 1
        go_up = False
      else:
        point -= 1
    
    # go_up is False
    elif not go_up:
      if point == 2:
        point -= 1
        go_up = True
      else:
        point += 1
  
  # all characters in text have been added in this point in time
  # now we add the '|' at the front and back of each string and print 
  for a_list in string_list:
    a_list.insert(0, '|')
    a_list.append('|')

    for char in a_list:
      print(char, end='')
    
    # at end of string, break to next line
    print()
  #end


print('Test 1')
print('Expected:')
print('| |')
print('|a|')
print('| |')
print('-' * 20)
print('Actual:')
print_dancing_string('a', 'M') 
print()

print('Test 2')
print('Expected:')
print('| b|')
print('|a |')
print('|  |')
print('-' * 20)
print('Actual:')
print_dancing_string('ab', 'M') 
print()

print('Test 3')
print('Expected:')
print('| b |')
print('|a c|')
print('|   |')
print('-' * 20)
print('Actual:')
print_dancing_string('abc', 'M') 
print()

print('Test 4')
print('Expected:')
print('| b  |')
print('|a c |')
print('|   d|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcd', 'M') 
print()

print('Test 5')
print('Expected:')
print('| b   f   |')
print('|a c e g i|')
print('|   d   h |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'M')
print()

print('Test 6')
print('Expected:')
print('|a   e   i|')
print('| b d f h |')
print('|  c   g  |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'T')
print()

print('Test 7')
print('Expected:')
print('|  c   g  |')
print('| b d f h |')
print('|a   e   i|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'B')
print()

print('Test 8')
print('Expected:')
print('||')
print('||')
print('||')
print('-' * 20)
print('Actual:')
print_dancing_string('', 'T') 
print()


