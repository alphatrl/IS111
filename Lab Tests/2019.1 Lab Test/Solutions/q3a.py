def calculate_fees_1(n):
    '''
    This function returns the least amount of money that you will 
    expect to pay for the n Grab rides that you have taken that month.  
        
    Parameters:
        - n, a non-negative integer which represents the number of Grab rides that you plan to take in a month. 
    '''
    # write your answer between #start and #end
    #start
    AVG_GRABRIDE = 10 
    GRAB_MAX_RIDE = 10
    COMMUTE_PLAN = 19

    with_commute_plan = 0
    no_plan_fee = 0
    addition_rides = 0
    commute_max_ride = n

    if n > 10:
        addition_rides = n - GRAB_MAX_RIDE
        commute_max_ride = GRAB_MAX_RIDE

    # calculate with plan 
    with_commute_plan = 19 + (commute_max_ride * (AVG_GRABRIDE - 4) + (addition_rides * AVG_GRABRIDE))
    
    # calculate without plan
    no_plan_fee = n * AVG_GRABRIDE

    return min(no_plan_fee, with_commute_plan)
    #end
