# start of answer

def reverse_num(number):

  is_negative = False
  
  # remember the number is a -ve number
  # then convert it to a +ve number
  if number < 0:
    is_negative = True
    number = number * -1

  # convert int to string
  # reverse string
  # convert reversed string back to int
  reverse_number = int((str(number))[::-1])

  # if it is originally a -ve number
  # convert it back
  if is_negative:
    reverse_number = reverse_number * -1

  return reverse_number

# end of answer

print("Test 1: Test that the return value is an int value")
print("Expected:True")
print("Actual  :" + str(isinstance(reverse_num(123), int)))
print()

print("Test 2")
print("Expected:2017")
print("Actual  :" + str(reverse_num(7102)))
print()

print("Test 3")
print("Expected:32")
print("Actual  :" + str(reverse_num(230)))
print()

print("Test 4")
print("Expected:0")
print("Actual  :" + str(reverse_num(0)))
print()

print("Test 5")
print("Expected:-21")
print("Actual  :" + str(reverse_num(-12)))
print()

