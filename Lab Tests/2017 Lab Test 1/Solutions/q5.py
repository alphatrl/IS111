# start of answer

def print_triangle(sentence):
  length = len(sentence)
  number_of_list = 0
  last_row_length = round((length / 2) + 1)
  is_triangle = (length % 4 == 0)
  triangle_list = []

  if not is_triangle:
    return False

  # recreate a new string of letters rearranged
  string_rearrange = ''
  count = 0             # count is used to escape the loop when equal to row length 
  index = 0
  use_negative = False

  while count < length:
    if count == length - last_row_length:
      # if last row,
      # we save the string sentence[index:(length-index)]
      # why (length-index)? because to get a char at the back of the string,
      # sentence(-index) is the same as sentence(length-index)
      string_rearrange += sentence[index:(length-index) + 1 ]
      number_of_list += 1
      break

    else:
      if count == 0:
        string_rearrange += sentence[index]
        number_of_list += 1
        index += 1
      else:
        # is use_negative is False
        # get char from front of string
        if not use_negative:
          string_rearrange += sentence[index]
        # if use_negative is True
        # get char from back of string
        else:
          string_rearrange += sentence[-index]
          number_of_list += 1
          index += 1
        use_negative = not use_negative

      count += 1

  # round this to be our position of the first letter in list
  first_pos = round(last_row_length / 2) - 1# this will be the position to put char, also my index start from 0
  last_pos = first_pos   # update this when row_list > 1

  # write respective char to indiviual row
  count = 0
  for index in range(number_of_list):
    row = ''

    if index == 0:
      for i in range(last_row_length):
        if i == first_pos:
          row += string_rearrange[count]
          count += 1
        else: 
          row += ' '
    # else if index is > 0 or not last index in number_of_list
    elif index < number_of_list - 1:
      for i in range(last_row_length):
        if i == first_pos or i == last_pos:
          row += string_rearrange[count]
          count += 1
        else: 
          row += ' '
    
    # when at last row in number_of_list
    else:
      row += string_rearrange[count::]

    triangle_list.append(row)
    first_pos -= 1
    last_pos += 1

  # print row in triangle_list
  # note that i could just print out in the previous for loop 
  for row in triangle_list:
    print(row)    

  return is_triangle # added so that this script will run. feel free to modify it


# end of answer


print('Test 1')
print('Expected output:')
print('   a')
print('  b l')
print(' c   k')
print('defghij')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('abcdefghijkl')
print('Actual return value  :' + str(result))
print()

print('Test 2')
print('Expected output:')
print('         A')
print('        B 9')
print('       C   8')
print('      D     7')
print('     E       6')
print('    F         5')
print('   G           4')
print('  H             3')
print(' I               2')
print('JKLMNOPQRSTUVWXYZ01')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print('Actual return value  :' + str(result))
print()

print('Test 3')
print('Expected output:')
print('Expected return value:False')
print('Actual output:')
result = print_triangle('abcdefghij')
print('Actual return value  :' + str(result))
print()

print('Test 4')
print('Expected output:')
print('Expected return value:False')
print('Actual output:')
result = print_triangle('abc')
print('Actual return value  :' + str(result))
print()

print('Test 5')
print('Expected output:')
print(' a')
print('bcd')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('abcd')
print('Actual return value  :' + str(result))
print()