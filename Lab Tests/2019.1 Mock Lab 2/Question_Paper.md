# Question Paper

## Question 1

### Part A (Difficulty Level: *)

In [q1a.py](./Questions/q1a.py), implement a function called `get_hashtags()`. The function takes in the following parameters:

- `post_list` (type: `list`): This is a list of strings. Each string contains 1 or more words, and each word may either be a hashtagged word (i.e., starts with ‘**#**’) or a non-hashtagged word (i.e., does not start with ‘**#**’).  

The function returns a list of all the hashtagged words in `post_list`. If there is no hastagged word in `post_list`, the function returns an empty list.

#### Examples

##### Example 1

```python
get_hashtags(["#smukitty #smucat #Meow If you see me around school please approach me slowly cos I am very shy and get scared easily", "The Official Instagram for Grumpy Cat. #TeamGrumpy #GrumpyCat", "#Meow Definitely not a #grumpycat"])
```

returns

```python
['#smukitty', '#smucat', '#Meow', '#TeamGrumpy', '#GrumpyCat', '#Meow', '#grumpycat'].
```

##### Example 2

```python
get_hashtags(["I'm writing a book. I've got the page numbers done.", "When nothing is going right, go left."])
```

returns

``` python
[]
```

##### Example 3

```python
get_hashtags(["A balanced diet means a cupcake in each hand.", "I'm never wrong. Just different levels of right."])
```

returns

```python
[]
```

##### Example 4

```python
get_hashtags(["SMU #SIS congratulates the #Classof2019 graduates for their accomplishments", "#Computing at #SIS"])
```

returns

```python
['#SIS', '#Classof2019', '#Computing', '#SIS']
```

### Part B (Difficulty Level: **)

In [q1b.py](./Questions/q1a.py), implement a function called `count_hashtags()`. The function takes in the following parameter:

- `hashtag_list` (type: `list`): This is a list of strings.  Each string in `hashtag_list` contains a hashtagged word (i.e., a word that starts with ‘**#**’).

The function should return a list of tuples, where each tuple has two elements – one containing the *unique* hashtagged word in lowercase and the other containing the number of times that this *unique* hashtagged word has appeared in the given `hashtag_list`. For example, the tuple **('#sis', 2)** means that the hashtagged word '**#sis**' has appeared two times in `hashtag_list`.

Your function should take into account words that are of different casings; for example, '**#GrumpyCat**' and '**#grumpycat**' should be considered as the same unique hashtag.

You can assume that each string in `hashtag_list` is always a hashtagged word (i.e., a word that starts with ‘#’). It is possible, though, for hashtag_list to be empty.

#### Example 1

```python
count_hashtags(["SMU #SIS congratulates the #Classof2019 graduates for their accomplishments", "#Computing at #SIS"])
```

returns

```python
[('#sis', 2), ('#classof2019', 1), ('#computing', 1)]
```

#### Example 2

```python
count_hashtags(["A balanced diet means a cupcake in each hand.", "I'm never wrong. Just different levels of right."])
```

returns

```python
[]
```

#### Example 3

```python
count_hashtags(["#smukitty #smucat #Meow If you see me around school please approach me slowly cos I am very shy and get scared easily", "The Official Instagram for Grumpy Cat. #TeamGrumpy #GrumpyCat", "#Meow Definitely not a #grumpycat"])
```

returns

```python
[('#smukitty', 1), ('#smucat', 1), ('#meow', 2), ('#teamgrumpy', 1), ('#grumpycat', 2)]
```

**Important Note:**

You should try to import and use the get_hashtags() function implemented in [q1a.py](./Questions/q1a.py) for Part (b) of Q1.  

## Question 2 (Difficulty Level: ***)

A bubbletea shop owner wants to keep track of her customers’ orders. For example, a customer who orders 1 Hawaii Fruit Tea will have his/her order represented as any of the following strings (due to the shop owner’s inconsistency in the use of spacings):

- "Hawaii Fruit Tea-1"
- "Hawaii Fruit Tea -1"
- "Hawaii Fruit Tea- 1"
- "Hawaii Fruit Tea - 1".  

Each order may also have multiple items; for example, a customer may order **2 Lime Green Teas** and **3 Black Teas**. This order will be represented as a string "**Lime Green Tea-2, Black Tea-3"**. Again, note that there may be inconsistent spacings in the string that represents this order.

### Part A

Implement a function called `get_order_amount()` inside [q2a.py](./Questions/q2a.py). This function takes in the following two parameters:

- `order_string` (type: `string`): This is a string that represents the order by a single customer. For example, the string "**Lime Green Tea -2, Black Tea - 3**" means that customer has ordered **2 Lime Green Teas** and **3 Black Teas**. You may assume that the `order_string` is always a valid order (i.e., it has a bubbletea name and the corresponding quantity). However, `order_string` may be an empty string.

- `price_list` (type: `list`): This is a list of tuples in the form (a, b), representing the unit price b of each bubbletea drink a. For instance, **[("Lime Green Tea", 3.60), ("Black Tea", 3.10)]** means that the **Lime Green Tea** costs **$3.60** each and **Black Tea** costs **$3.10** each. You may assume that all bubble teas that appear within the order_string will also appear in the price_list.

#### Examples

The function returns the total order amount for that customer.

##### Example 1

```python
get_order_amount("Lime Green Tea -2, Black Tea - 3", [("Lime Green Tea", 3.60), ("Black Tea", 3.10)])
```

returns

```python
16.50 #(given by 2*$3.60 + 3*$3.10)
```

##### Example 2

```python
get_order_amount("", [("Lime Green Tea", 3.60), ("Black Tea", 3.10)])
```

returns

```python
0
```

##### Example 3

```python
get_order_amount("Grapefruit Yakult -5, Black Tea - 3, Lime Green Tea-1", [("Lime Green Tea", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40)])
```

returns

```python
49.90 # (given by 5*$7.40 + 3*$3.10 + 1*$3.60)
```

**Important Note:**

You are not allowed to use the dictionary data type for this question.

### Part B

Implement a function called `get_total_revenue()` inside [q2b.py](./Questions/q2b.py). This function takes in the following two parameters:

- `order_list` (type: `list`): This is a list of strings that represents the list of orders made by all the customers in a single day. For example, the list `["Grapefruit Yakult -5, Black Tea - 3, Lime Green Tea-1", "Lime Green Tea -2, Black Tea - 3"]` means that the first customer ordered 5 Grapefruit Yakult, 3 Black Teas and 1 Lime Green Tea, while the second customer ordered 2 Lime Green Teas and 3 Black Teas.

- `price_list`: This is a list of tuples in the form (a, b), representing the unit price b of each bubbletea drink a. For instance, `[("Lime Green Tea", 3.60), ("Black Tea", 3.10)]` means that the Lime Green Tea costs $3.60 each and Black Tea costs $3.10 each. You may assume that all bubble teas that appear within the `order_string` will also appear in the price_list.

The function returns the total revenue collected from all the orders of that day.

#### Example

```python
get_revenue(["Grapefruit Yakult -5, Black Tea - 3, Lime Green Tea-1", "Lime Green Tea -2, Black Tea - 3"], [("Lime Green Tea", 3.60), ("Black Tea", 3.10), ("Grapefruit Yakult", 7.40)])
```

returns

```python
66.40

# the first customer’s order cost 49.90 and the second customer’s order cost 16.50
```

**Important Note:**

You should try to import and use the `get_order_amount()` function implemented in [q2a.py](./Question/q2a.py) for Part (b) of Q2.
