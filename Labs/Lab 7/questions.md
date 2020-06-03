# Lab 7 - File Handling

## Q6: [\*\*\*]

In this question, you need to read in a Python script and extract all the docstrings together with their function headers.

Assume the Python script you're processing contains several function defintions. For each function defintion, assume it is strictly written in the following way:

- The function header (i.e., ```def name_of_function(list_of_parameters):```) takes one line.

- Immediately below the function header, a docstring is presented to explain the function. 
  - The docstring may take one line or multiple lines. 
  - It always starts with ```"""``` (i.e., three double quotes), but there are 4 spaces in front of the ```"""``` for indentation purpose.
  - It always ends with ```"""```, but there may be some additional spaces behind the ```"""```.

For example, a file may look like the following:

```python
def my_test_func(param1, param2):
    """
    This is a test function that takes in two parameters and returns a number.
    The two parameters are compared. 0 or 1 is returned.
    """
    if (param1 < param2):
        return 0
    else:
        return 1
def another_function():
    """This is a function without any parameter."""
    pass
def third_funct():
    """This is a function
    that has two lines of docstring."""
    print("hello")
```

You can assume that inside the Python script you're processing, the keyword ```def``` occurs only for function definitions. Also, the pattern ```"""``` does not occur anywhere else in the file except for docstrings.

Write a function called ```extract_functions()``` that takes in two parameters:

- ```python_filename```: The name of a Python script, with .py as its extension.
- ```output_filename```: The name of an output file.
    
The function should read the Python script, extracts all function headers and docstrings, and write them into the output file. In the output file, the functions are numbered. The doctrings are indented with 4 spaces. The keyword ```def```, the colon, and ```"""``` are removed. A blank line is inserted after each function.

For example, given the file above, the generated output file should contain the following:

```
1. my_test_func(param1, param2)
    This is a test function that takes in two parameters and returns a number.
    The two parameters are compared. 0 or 1 is returned.

2. another_function()
    This is a function without any parameter.

3. third_funct()
    This is a function
    that has two lines of docstring.
```

You are given a file called "python_script.py" that can be used to test your program.

## Q7 [\*\*\*\*]

[This question is adapted from the book “The practice of Computing using Python” - Programming Project on Page 340.]

There is a belief that humans are able to read even when the order of the letters are misplaced. Try reading this:

  I cnduo't bvleiee taht I culod uesdtannrd waht I was rdnaieg 

Interesting read here: [https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/).

Write a program that reads text from a file called `"talk.txt"` and prints the content on the output screen scrambling the words in the content as described below:

- Scramble every word in the text. For each word, __scramble the letters in the middle only, leaving untouched the first and the last letters__.
- You may assume that every two consecutive words are separated by a single space. Maintain single space between every two consecutive words in the scrambled version.
- Challenge yourself to leave the punctuations [, ' ! .] in the content untouched in the original place.

As an example, if the text reads “Programming is really fun”, then one version after scrambling could be “Pgmnarirmog is rlelay fun”. Note that since we scramble only the letters in the middle of each word, the two words “is” and “fun” in the example are not scrambled.  

It helps if you define functions to help you with this question.

__Hint:__ To scramble the letters in the middle of a 6-lettered word, for example, you could take all the letters in the indices ranging from 1 to 4, and put them in random positions ranging from 1 to 4. A 6-letter word after scrambling should contain exactly the same six letters. Note that after you randomly scramble the letters in the middle, if the resulting word happens to be the same as the original word, you should discard this scrambled word and try again.

You probably want to use the ```random``` module to help you with scrambling letters.

Some partial output from a sample of your code with the given `"talk.txt"` file may look like the following:

```
We do not need miagc to chgnae the wlrod, we crray all the pwoer we need inisde oleeursvs aedlray: we have the pweor to imngiae betetr.
```

Note that your code will generate different output because of the randomness in the code.