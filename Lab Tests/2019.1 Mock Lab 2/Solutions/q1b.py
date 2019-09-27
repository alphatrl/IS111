import q1a 

def count_hashtags(post_list):
    '''
    This function counts the number of hashtagged words in post_list
    and returns a list of tuples, where each tuple is of the form (a, b)
    where a is a unique hashtagged word, and b is the number of times
    that a appears in post_list 
    '''
    # write your answer between #start and #end
    #start
    return []
    #end 



########## TEST CASE 1 ##########
print('Test 1')
print('Expected:', [('#sis', 2), ('#classof2019', 1), ('#computing', 1)])
result = count_hashtags(["SMU #SIS congratulates the #Classof2019 graduates for their accomplishments", "#Computing at #SIS"])
print('Actual:  ', result)
print()

########## TEST CASE 2 ##########
print('Test 2')
print('Expected:', [])
result = count_hashtags(["A balanced diet means a cupcake in each hand.", "I'm never wrong. Just different levels of right."]) 
print('Actual:  ', result)
print()

########## TEST CASE 3 ##########
print('Test 3')
print('Expected:', [('#smukitty', 1), ('#smucat', 1), ('#meow', 2), ('#teamgrumpy', 1), ('#grumpycat', 2)])
result = count_hashtags(["#smukitty #smucat #Meow If you see me around school please approach me slowly cos I am very shy and get scared easily", "The Official Instagram for Grumpy Cat. #TeamGrumpy #GrumpyCat", "#Meow Definitely not a #grumpycat"])
print('Actual:  ', result)
print()