def expand(text):
  # write your answer between #start and #end
  #start

  letter_index = []
  length = len(text)
  current = 0
  to_replace = []
  sub_strings = []
  text_without_append = ''
  new_text = ''
  
  while current < length:
    if text[current] == '&':
      letter_index.append(text[current])
      current += 1
      
      index_ref_string = ''
      while text[current].isdigit() or text[current] == '-':        
        index_ref_string += text[current]
        current += 1

        # exit if at the end of text        
        if current == length:
          break
      
      ref = index_ref_string.split('-')
      index_ref = (int(ref[0]), int(ref[1]))
      to_replace.append(index_ref)

    else:
      letter_index.append(text[current])
      text_without_append += text[current]
      current += 1

  # print(to_replace, letter_index)
  # print(text_without_append)

  # using the reference number, find the string to replace
  for index in to_replace:
    new_sub_string = ''
    for number in range(index[0],index[1] + 1):
      if number < len(text_without_append):
        new_sub_string += text_without_append[number]
      else:
        new_sub_string += '?'
    sub_strings.append(new_sub_string)

  # print(sub_strings)

  count = 0
  for string in letter_index:
    if string == '&':
      new_text += sub_strings[count]
      count += 1
    else: 
      new_text += string

  return new_text
  #end

print('Test 1')
print('Expected:ABC XYZ XYZ')
result = expand('ABC &5-7 XYZ')
print('Actual  :' + result)
print()

print('Test 2')
print('Expected:ABC XYZABC XYZ')
result = expand('&0-3&4-6ABC XYZ')
print('Actual  :' + result)
print()

print('Test 3')
print('Expected:C???ABC')
result = expand('&2-5ABC')
print('Actual  :' + result)
print()

print('Test 4')
print('Expected:[a b A B a b A a b A B ]')
result = expand('a b A B &0-5&0-7')
print('Actual  :[' + result + ']')
print()

print('Test 5')
print('Expected:[UVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ]')
result = expand('&20-25ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('Actual  :[' + result + ']')
print()

print('Test 6')
print('Expected:[]')
result = expand('')
print('Actual  :[' + result + ']')
print()

print('Test 7')
print('Expected:abc')
result = expand('abc')
print('Actual  :' + result)
print()