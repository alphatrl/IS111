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

  hashtag_list = q1a.get_hashtags(post_list)
  unique_list = []
  count_list = []
  
  # get unique hashtag (ignore upper or lowercase)
  for hashtag in hashtag_list:
    
    # if there is nothing in unique_list, don't need to compare
    if len(unique_list) == 0:
      unique_list.append(hashtag.lower())
    else:
      # compare in lowercase
      if not hashtag.lower() in unique_list:
        unique_list.append(hashtag.lower())
  
  # compare unique against hashtag list
  for unique in unique_list:
    count = 0
    for hashtag in hashtag_list:
      if hashtag.lower() == unique:
        count += 1
    count_list.append((unique, count))

  return count_list
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