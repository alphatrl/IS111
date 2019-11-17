def get_prices_in_range(price_list, low, high):
  # Modify the code below    
  range_list = []

  for price in price_list:
    if price >= low and price <= high:
      range_list.append(price)
  return range_list