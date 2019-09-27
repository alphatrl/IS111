def get_hashtags(post_list):
    '''
    This function returns the list of hashtagged words in post_list. 
    A hashtagged word is a word that begins with '#'  
    '''
    # write your answer between #start and #end
    #start
    return []
    #end 



########## TEST CASE 1 ##########
print('Test 1')
print('Expected:', ['#smukitty', '#smucat', '#Meow', '#TeamGrumpy', '#GrumpyCat', '#Meow', '#grumpycat'])
result = get_hashtags(["#smukitty #smucat #Meow If you see me around school please approach me slowly cos I am very shy and get scared easily", "The Official Instagram for Grumpy Cat. #TeamGrumpy #GrumpyCat", "#Meow Definitely not a #grumpycat"])
print('Actual:  ', result)
print()

########## TEST CASE 2 ##########
print('Test 2')
print('Expected:', [])
result = get_hashtags(["I'm writing a book. I've got the page numbers done.", "When nothing is going right, go left."])
print('Actual:  ', result)
print()

########## TEST CASE 3 ##########
print('Test 3')
print('Expected:', ['#SIS', '#Classof2019', '#Computing', '#SIS'])
result = get_hashtags(["SMU #SIS congratulates the #Classof2019 graduates for their accomplishments", "#Computing at #SIS"])
print('Actual:  ', result)
print()

########## TEST CASE 4 ##########
print('Test 4')
print('Expected:', [])
result = get_hashtags(["A balanced diet means a cupcake in each hand.", "I'm never wrong. Just different levels of right."])
print('Actual:  ', result)
print()