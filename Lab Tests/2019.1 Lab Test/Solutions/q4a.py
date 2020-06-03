def check_grouping(grouping_list, must_list, cannot_list):
    '''
    This function returns True if the given arrangement in grouping_list 
    satisfies both types of constraints specified by must_list and cannot_list. 
    Otherwise, the function returns False
        
    Parameters:
        - grouping_list, a list of 3 lists representing the 3 groups of n students each
        - must_list, a list of tuples, where each tuple has two strings representing the names of two students who MUST be in the same group; the list might be empty.
        - cannot_list, a list of tuples, where each tuple has two strings representing the names of two students who CANNOT sit next to each other; the list might be empty.
    '''
    # write your answer between #start and #end
    #start

    can_seat = True
    final_must = True
    final_cannot = True

    for groups in grouping_list:

        must_condition = True
        cannot_condition = True

        # must_list
        for must in must_list:
            if must[0] in groups:
                must_condition = must[1] in groups
            elif must[1] in groups:
                must_condition = must[0] in groups
            
        final_must = final_must and must_condition

        # cannot seat 
        # must_list
        for cant in cannot_list:
            if cant[0] in groups:
                cannot_condition = not cant[1] in groups
            elif must[1] in groups:
                cannot_condition = not cant[0] in groups

        final_cannot = final_cannot and cannot_condition


    return (final_must and final_cannot)
    #end 