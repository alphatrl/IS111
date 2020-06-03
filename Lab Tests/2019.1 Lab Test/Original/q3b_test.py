from q3b import calculate_fees_2

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', 325)
result = calculate_fees_2(10,12) 
print('Actual:  ', result)
print()

########### TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', 1280)
result = calculate_fees_2(12,57) 
print('Actual:  ', result)
print()

########### TEST CASE 3 ##########
print()
print('-' * 20)
print()
print('Test 3')
print('Expected:', 49.99)
result = calculate_fees_2(3,1) 
print('Actual:  ', result)
print()