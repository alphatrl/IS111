def check_string(s1, s2, s3):
    '''
    This function returns True if one of the three strings 
    (s1, s2  or s3) is a concatentation of the other two strings, 
    and False otherwise. 

    Parameters:
        - s1, a string in lowercase
        - s2, a string in lowercase
        - s3, a string in lowercase 
    '''
    # write your answer between #start and #end
    #start

    string_list = [s1, s2, s3]
    longest_string = ''
    index_longest = -1

    cat_short_string_list1 = []
    cat_short_string_list2 = []

    # find longest string

    for index in range(len(string_list)):
        string = string_list[index]

        if len(longest_string) < len(string):
            longest_string = string
            index_longest = index

    
    # cat shortest string
    for index in range(len(string_list)):
        string = string_list[index]

        if index != index_longest:
            cat_short_string_list1.append(string)
            cat_short_string_list2.insert(0, string)

    short_string_1 = ''.join(cat_short_string_list1)
    short_string_2 = ''.join(cat_short_string_list2)

    return (short_string_1 == longest_string) or (short_string_2 == longest_string)
    #end 