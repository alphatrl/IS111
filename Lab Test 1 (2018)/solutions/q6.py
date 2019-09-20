def print_snake(sequence, w):
  # write your answer between #start and #end
  #start
  flip_snake_list = []
  snake_list = []
  row_list = []

  rev_sequence = sequence[::-1]
  insert_row_count = 0    # if 4 or 1 for not isalt or isalt, reset respectively
  is_alt_row = False

  # split character into their snake rows (but reverse)
  for index in range(len(rev_sequence)):
    char = rev_sequence[index]
    row_list.append(char)
    insert_row_count += 1

    
    if insert_row_count == w and not is_alt_row:
      flip_snake_list.append(row_list)
      row_list = []
      is_alt_row = not is_alt_row
      insert_row_count = 0
    elif insert_row_count == 1 and is_alt_row:
      for index in range(w - 1):
        row_list.append(' ') 
      flip_snake_list.append(row_list)
      row_list = []
      is_alt_row = not is_alt_row
      insert_row_count = 0

    # for the front of the snake, might not be the int w all the time
    # if last element
    if rev_sequence[index] == rev_sequence[-1] and insert_row_count != w:
      for index in range(w - len(row_list)):
        row_list.append(' ')
      flip_snake_list.append(row_list)

  # reset some declared variables
  row_list = []
  is_alt_row = False
  count = 1

  # reverse to what we are suppose to print out
  # flip direction of row when necessary is_alt_row == False
  # keep inserting row to front of snake_list,
  # since we are working backwards
  for flip_row_list in flip_snake_list:
    if not is_alt_row:
      for char in flip_row_list[::-1]:
        row_list.append(char)
      snake_list.insert(0, row_list)
      row_list = []
      count += 1
    else:
      for char in flip_row_list:
        row_list.append(char)
      snake_list.insert(0, row_list)
      row_list = []
      count += 1
    if count % 2 == 0:
      is_alt_row = not is_alt_row  

  for rows in snake_list:
    for char in rows:
      print(char, end = '')
    print()
  
  #end

print('Test 1')
print('Expected:')
print('abcd')
print('   e')
print('ihgf')
print('j   ')
print('klmn')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijklmn', 4)
print('\n')

print('Test 2')
print('Expected:')
print('cba')
print('d  ')
print('efg')
print('  h')
print('kji')
print('l  ')
print('mno')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijklmno', 3)
print('\n')

print('Test 3')
print('Expected:')
print('    a')
print('fedcb')
print('g    ')
print('hijkl')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijkl', 5)
print('\n')

print('Test 4')
print('Expected:')
print('   a')
print('   b')
print('fedc')
print('g   ')
print('hijk')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijk', 4)
print('\n')
    
print('Test 5')
print('Expected:')
print('a   ')
print('b   ')
print('cdef')
print('-' * 20)
print('Actual:')
print_snake('abcdef', 4)
print('\n')

print('Test 6')
print('Expected:')
print('a   ')
print('bcde')
print('-' * 20)
print('Actual:')
print_snake('abcde', 4)