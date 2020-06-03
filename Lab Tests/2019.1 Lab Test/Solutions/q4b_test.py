from q4b import get_grouping

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
expected_results1 = [('Snow White', 'Dopey'), ('Grumpy', 'Queen'), ('Sneezy', 'Sleepy')]
expected_results2 = [('Snow White', 'Grumpy'), ('Dopey', 'Queen'), ('Sneezy', 'Sleepy')]
print('Expected:', expected_results1, 'or')
print('         ', expected_results2, 'in any ordering')
result = get_grouping(['Snow White','Dopey','Grumpy','Sneezy','Sleepy','Queen'], [('Sneezy','Sleepy')], [('Snow White','Queen')])
print('Actual:  ', result)
print()

########### TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', None)
result = get_grouping(['Snow White','Dopey','Grumpy','Sneezy','Sleepy','Queen'], [('Sneezy','Sleepy'), ('Dopey','Grumpy')], [('Snow White','Queen')]) 
print('Actual:  ', result)
print()