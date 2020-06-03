def multiply_digits(str_list):
    '''
    This function multiplies all the characters that are digits in the given list.  
        
    Parameters:
        - str_list, a list of strings, whereby each string contains sequences of digits and sequences of non-digit characters that are separated by the hex '#', e.g., '1#a#33#b$b'. This string may be empty. 
    '''
    # write your answer between #start and #end
    #start

    sum = 0

    for string in str_list:
        str_split = string.split('#')

        for item in str_split:
            # check if char is a digit
            if item.isdigit():
                if sum == 0:
                    sum = int(item)
                else:
                    sum = sum* int(item)





    return sum
    #end 