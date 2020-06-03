# Created by Amos Tan for students to reference their lab work
# Q6

# Write your code here:
FILE_NAME = "python_script.py"

# rewrite all content input_file to a string
with open(FILE_NAME, 'r') as input_file:
    function = ""
    for line in input_file:
        function += line
        
function_list = function.split('def')
function_list.pop(0) # remove empty space at index 0

count = 1

for function in function_list:
    func =  function.split("\"\"\"")
    
    # remove leading space and colon in function name
    function_name = func[0].lstrip(' ').replace(':\n', '')

    # debug docstring
    # print(func[1]) 

    # remove '    ' at the front
    # remove \n at front of docstring
    # add a tab if its a multi-line docstring
    docstring = func[1].lstrip('\n').replace('\n','\n\t').replace('    ','')
    
    
    print(f"{count}. {function_name}")
    print(f"\t{docstring}\n")
    
    count += 1
