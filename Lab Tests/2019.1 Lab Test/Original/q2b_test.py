from q2b import multiply_digits

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', 400)
result = multiply_digits(['ice#10#tea', '20#2#bubble'])
print('Actual:  ', result)
print()

########### TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', 22)
result = multiply_digits(['a#2#c', 'dd#ee#11']) 
print('Actual:  ', result)
print()

########### TEST CASE 3 ##########
print()
print('-' * 20)
print()
print('Test 3')
print('Expected:', 15)
result = multiply_digits(['15#1', 'a']) 
print('Actual:  ', result)
print()

########### TEST CASE 4 ##########
print()
print('-' * 20)
print()
print('Test 4')
print('Expected:', 0)
result = multiply_digits([]) 
print('Actual:  ', result)
print()