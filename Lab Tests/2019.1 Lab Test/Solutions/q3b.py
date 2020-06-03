def calculate_fees_2(n, m):
    '''
    This function returns the least amount of money that you will 
    expect to pay for the n Grab rides and m GrabFood orders that you have taken that month.  
        
    Parameters:
        - n, a non-negative integer which represents the number of Grab rides that you plan to take in a month. 
        - m, a non-negative integer which represents the number of GrabFood orders that you plan to place in a month. 
    '''
    # write your answer between #start and #end
    #start
    AVG_GRABRIDE = 10 
    AVG_GRABFOOD = 20 
    GRABFOOD_DELIVERY = 5 

    # commute ride variables
    commute_plan = 19
    max_commute_ride = 10
    commute_max_ride = n
    addition_rides = 0
    if n > max_commute_ride:
        addition_rides = n - max_commute_ride
        commute_max_ride = max_commute_ride


    # Food Plan Variables
    food_plan = 9.99
    no_delivery = 50
    delivery = m
    if m > 50:
        no_delivery = m - 50
        delivery = 50

    # All purpose 
    all_plan = 25

    # calculate no plan 
    no_plan = (n * AVG_GRABRIDE) + (m * AVG_GRABFOOD) + (m * GRABFOOD_DELIVERY) + (m * 5)

    # commute_plan
    commute_plan += (commute_max_ride * (AVG_GRABRIDE - 4)) + (addition_rides * AVG_GRABRIDE) + (m * GRABFOOD_DELIVERY) + (m * 5)

    # calculate food plan
    food_plan += (n * AVG_GRABRIDE) + (m * AVG_GRABFOOD) + (no_delivery * 5) - 10

    # calculate all plan 
    all_plan += (commute_max_ride * (AVG_GRABRIDE - 4)) + (addition_rides * AVG_GRABRIDE) + (m * AVG_GRABFOOD) + (no_delivery * 5)

    print(no_plan, commute_plan, food_plan, all_plan)

    return min(no_plan, commute_plan, food_plan, all_plan)
    #end 