def print_snake(sequence, w):
    # write your answer between #start and #end
    #start
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