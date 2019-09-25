def count_names_with_space(name_list):
  # Modify the code below
  count = 0
  
  for name in name_list:
    # if index found is 0 or more, a space is found
    if name.find(' ') >= 0:
      count += 1

  return count
