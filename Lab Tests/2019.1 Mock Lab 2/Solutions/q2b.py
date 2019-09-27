import q2a

def get_revenue(order_list, price_list):
    '''
    This function computes the total revenue collected from the sales
    of the bubble tea, and returns this total revenue.  
    '''
    # write your answer between #start and #end
    #start
    return 0
    #end 



########## TEST CASE 1 ##########
print('Test 1')
print('Expected:', 66.4)
result = get_revenue(["Grapefruit Yakult -5, Black Tea - 3, Lime Green Tea-1", "Lime Green Tea -2, Black Tea - 3"], [("Lime Green Tea", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40)])
print('Actual:  ', result)
print()

# ########## TEST CASE 2 ##########
print('Test 2')
print('Expected:', 70.75)
result = get_revenue(["Oolong Milk Tea-2,Caramel Milk Tea-3", "Grapefruit Yakult-2, Oolong Milk Tea- 1", "Lime Green Tea -2, Black Tea- 3", "Caramel Milk Tea-3"], [("Lime Green Tea", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40), ("Oolong Milk Tea", 3.25), ("Caramel Milk Tea", 4.95)])
print('Actual:  ', result)
print()

# ########## TEST CASE 3 ##########
print('Test 3')
print('Expected:', 117.6)
result = get_revenue(["Oolong Milk Tea-1,Caramel Milk Tea-5", "Chocolate-3", "Grapefruit Yakult-5, Oolong Milk Tea- 1", "Chocolate-1,  Lime Green Tea -2, Black Tea - 3", "Caramel Milk Tea-3,   Lime Green Tea-1"], [("Lime Green Tea", 3.60), ("Chocolate", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40), ("Oolong Milk Tea", 3.25), ("Caramel Milk Tea", 4.95)])
print('Actual:  ', result)
print()