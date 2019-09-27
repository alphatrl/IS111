def get_order_amount(order_string, price_list):
    '''
    This function returns the order amount, based on the items in the 
    order string, and the price of each item in the price list. 
    '''
    # write your answer between #start and #end
    #start
    return 0 
    #end 



########## TEST CASE 1 ##########
print('Test 1')
print('Expected:', 16.5)
result = get_order_amount("Lime Green Tea -2, Black Tea - 3", [("Lime Green Tea", 3.60), ("Black Tea", 3.10)]) 
print('Actual:  ', result)
print()

########## TEST CASE 2 ##########
print('Test 2')
print('Expected:', 0)
result = get_order_amount("", [("Lime Green Tea", 3.60), ("Black Tea", 3.10)]) 
print('Actual:  ', result)
print()

########## TEST CASE 3 ##########
print('Test 3')
print('Expected:', 49.9)
result = get_order_amount("Grapefruit Yakult -5, Black Tea - 3, Lime Green Tea-1", [("Lime Green Tea", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40)])
print('Actual:  ', result)
print()
