from q1 import check_string

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', False)
result = check_string('sleep', 'in', 'school')
print('Actual:  ', result)
print()

########## TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', True)
result = check_string('think', 'thinkpad', 'pad') 
print('Actual:  ', result)
print()

########## TEST CASE 3 ##########
print()
print('-' * 20)
print()
print('Test 3')
print('Expected:', False)
result = check_string('i', 'love', 'sis') 
print('Actual:  ', result)
print()

########## TEST CASE 4 ##########
print()
print('-' * 20)
print()
print('Test 4')
print('Expected:', True)
result = check_string('labtest', 'lab', 'test') 
print('Actual:  ', result)
print()

########## TEST CASE 5 ##########
print()
print('-' * 20)
print()
print('Test 5')
print('Expected:', True)
result = check_string('tea', 'bubble', 'bubbletea')  
print('Actual:  ', result)
print()