# Question Paper

## Q1: Add First Odd Digits [**]

Define a function called `add_first_odd_digits` in [ql.py](./Questions/q1.py).

The function takes in a list of strings called `str_list` as its parameter. The function goes through all the strings in this list and for each string, it looks for a digit that is an odd number (i.e., 1, 3, 5, 7 or 9). The function adds up the first odd digit in each string and returns the sum. If a string doesn't contain any odd digit, then
nothing is added for that string.

### Example

```python
add_first_odd_digits(['abc123def', 'SMU2345 SIS', 'XYZO', '7777'])
```

returns

```code
11
```

This is because the first odd digit found in '**abc123def**' is **1**, the first odd digit found in '**SMU2345SIS**' is **3**, '**XYZ0**' doesn't contain any odd digit, and the first odd digit in **7777** is **7**. Therefore, we get **1 + 3 + 7 = 11**

If `str_list` is empty, then **0** is returned by the function.

Use the provided [q1_test.py](./Questions/q1_test.py) to test your code. DO NOT modify `q1_test.py`.

## Q2: Display Strings [**]

Define a function called `display_strings()` inside the file [q2.py](./Questions/q2.py).

The function takes in the following parameters:

- a list of strings called `str_list`
- a character called `ch`

The function prints out the strings in `str_list`, one in each row. However, each string will have some spaces in front such that the output looks like a staircase. Moreover, strings that are shorter than the longest string in `str_list` will be "padded" with `ch` in the end so that they reach the same length as the longest string.

### Example

#### Example 1

```python
display_strings(['Spider Man', 'Iron Man', 'Hulk', 'Thor',
'Captain America', 'Black Widow'], '-')
```

the output is

```code
     Spider Man-----
    Iron Man ------
   Hulk-----------
  Thor-----------
 Captain America
Black Widow----
```

**Note:**

We can see that the longest string in `str_list` is '**Captain America**', which has 13 characters. Therefore, each string is padded with some '**-**' such that it becomes 13-character long.

#### Example 2

```python
display_strings(['ABC', 'B', 'CD', 'D'], '*')
```

then the output is

```code
   ABC
  C**
 CD*
D**
```

#### Example 3

```python
display_strings([], '*')
```

then the output is

```code
```

**Note:**

- The last row of the output has no space in front
- You  can use `print(ch * n)` to  print out the character `ch` for `n` times. E.g., `print('@' * 3)` will print '`@@@`'
