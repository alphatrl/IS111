def get_order_amount(order_string, price_list):
    '''
    This function returns the order amount, based on the items in the 
    order string, and the price of each item in the price list. 
    '''
    # write your answer between #start and #end
    #start


    if len(order_string) == 0:
      return 0
    
    order_list_inconsistent = order_string.split(',')
    order_list = []
    total_price = 0.0
  
    # split order_string into (order, quantity)
    for order in order_list_inconsistent:
      order_split = order.split('-')
      # strip remove whitespaces in front or behind
      # convert order qty to int
      order_list.append(((order_split[0]).strip(), int((order_split[1]).strip())))

    for price_tuple in price_list:
      for order in order_list:
        if price_tuple[0] == order[0]:
          price = price_tuple[1] * order[1]
          total_price += price

    return total_price
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
