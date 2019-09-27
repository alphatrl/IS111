def display_strings(str_list, ch):
  # Modify the code below

  longest_length = 0
  new_string_list = []
  number_padding = len(str_list) - 1

  # find longest string length
  for string in str_list:
    if len(string) > longest_length:
      longest_length = len(string)

  # move string to another list
  # add number of spaces required at front, 'number_padding'
  # and add number of characters at back accordingly 'number_character'
  for string in str_list:
    number_character = longest_length - len(string)
    new_string = (' ' * number_padding) + string + (number_character * ch)
    number_padding -= 1

    new_string_list.append(new_string)

  # print if not empty
  for string in new_string_list:
    print(string)
