from q4a import check_grouping

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', True)
result = check_grouping([['Snow White','Dopey','Grumpy'], ['Bashful','Sneezy','Sleepy'], ['Happy','Doc','Queen']], [('Sneezy','Sleepy'), ('Dopey','Grumpy')], [('Queen','Snow White')]) 
print('Actual:  ', result)
print()

########### TEST CASE 2 ##########
print()
print('-' * 20)
print()
print('Test 2')
print('Expected:', False)
result = check_grouping([['Snow White','Queen','Grumpy'], ['Bashful','Sneezy','Sleepy'], ['Happy','Doc','Dopey']], [('Sneezy','Sleepy'),('Dopey','Grumpy')], [('Queen','Snow White')]) 
print('Actual:  ', result)
print()

########### TEST CASE 3 ##########
print()
print('-' * 20)
print()
print('Test 3')
print('Expected:', False)
result = check_grouping([['Snow White','Dopey','Grumpy'], ['Bashful','Sneezy','Happy'], ['Sleepy','Doc','Queen']], [('Sneezy','Sleepy'),('Dopey','Grumpy')], [('Queen','Snow White')]) 
print('Actual:  ', result)
print()