def get_multiples_of(num_list, n):
    '''
    This function returns the number of numbers in num_list that are multiples of n. 
    If there is no number in num_list that is a multiple of n, the function returns 0.

    Parameters:
        - num_list, a list of positive integers; list may be empty
        - n, a positive integer
    '''
    # write your answer between #start and #end
    #start 

    number_multiples = 0

    if len(num_list) == 0:
        return number_multiples


    for number in num_list:
        if number % n == 0:
            number_multiples += 1

    return number_multiples 
    #end 