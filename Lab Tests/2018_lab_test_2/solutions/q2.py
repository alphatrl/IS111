def get_prices_in_range(price_list, low, high):
  # Modify the code below    
  price_range_list = []
  
  for price in price_list:
    if price >= low and price <= high:
      price_range_list.append(price)

  return price_range_list