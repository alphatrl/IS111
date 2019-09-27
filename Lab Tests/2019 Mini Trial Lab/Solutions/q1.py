def add_first_odd_digits(str_list):
  # modify the code below
  total_sum = 0
  
  for string in str_list:
    for char in string:
      # if character is a number
      if char.isdigit():
        number = int(char)

        # if odd number, add to total_sum , and exit second for-loop
        if number % 2 == 1:
          total_sum += number
          break
  
  return total_sum