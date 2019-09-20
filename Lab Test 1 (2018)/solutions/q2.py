def represent_numbers (start, end):
    # write your answer between #startcode and #endcode
    #startcode
  dash_list = []

  for index in range(start, end + 1):
    dash = ''
    for index_dash in range(abs(index) + 1):
      if index_dash > 0:
        dash += '-'
    
    dash_list.append(dash)

  return '#'.join(dash_list)
    #endcode


print('Test 1')
print('Expected:-#--#---#----#-----')
print('Actual  :' + represent_numbers(1, 5))
print()

print('Test 2')
print('Expected:---#----#-----')
print('Actual  :' + represent_numbers(3, 5))
print()

print('Test 3')
print('Expected:-')
print('Actual  :' + represent_numbers(1, 1))
print()

print('Test 4')
print('Expected:[]')
print('Actual  :[' + represent_numbers(4, 1) + ']')
print()

print('Test 5')
print('Expected:----#---#--#-##-')
print('Actual  :' + represent_numbers(-4, 1))
print()
