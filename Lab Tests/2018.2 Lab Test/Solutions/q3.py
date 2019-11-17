# If needed, you can define your own additional functions here.
# Start of your additional functions.

def sanitise_month(month):
  # if month is '09/19'
  # function return '9/19'
  month_split = month.split('/')
  month_num = str(int(month_split[0]))
  year = month_split[1]
  
  return month_num + '/' + year

# End of your additional functions.

def get_total_transactions_in_month(trans_file, month):
  # Modify the code below
  trans_dict =  {}

  with open(trans_file, 'r') as in_file:
    for trans in in_file:
      trans = trans.rstrip('\n')
      trans_split = trans.split('\t')
      
      date_split = trans_split[0].split('/')
      date = sanitise_month(date_split[0] + '/' + date_split[2])

      cost =  float(trans_split[1][1:]) # remove $ sign

      # check if inside dict
      if date in trans_dict:
        cost += trans_dict[date]

      trans_dict[date] = cost

  print(trans_dict)

  month = sanitise_month(month)

  # search month in dict
  if month in trans_dict:
    return trans_dict[month]

  return 0.0
    
