from q2a import get_multiples_of

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', 2)
result = get_multiples_of([14,11,30,28,50], 7) 
print('Actual:  ', result)
print()

########## TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', 3)
result = get_multiples_of([300,13,10,555,29], 5)  
print('Actual:  ', result)
print()

########## TEST CASE 3 ##########
print()
print('-' * 20)
print()
print('Test 3')
print('Expected:', 0)
result = get_multiples_of([27,83,10,3,8], 11) 
print('Actual:  ', result)
print()

########## TEST CASE 4 ##########
print()
print('-' * 20)
print()
print('Test 4')
print('Expected:', 0)
result = get_multiples_of([23333], 109) 
print('Actual:  ', result)
print()

########## TEST CASE 5 ##########
print()
print('-' * 20)
print()
print('Test 5')
print('Expected:', 0)
result = get_multiples_of([], 2) 
print('Actual:  ', result)
print()
