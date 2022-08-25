# Background Reading

## Python Operators

Python Operators are special symbols in Python that carry out arithmetic or logical computation.

Comparison (equality) operators are used to compare values and return either `True` or `False` according to the condition.

### Comparison Operators

These are the comparison operators in Python:

- `>`: Greater than Operator - True if left operand is greater than the right eg. `x > y`
- `<`: Less than - True if left operand is less than the right eg. `x < y`
- `==`: Equal to - True if both operands are equal eg. `x == y` (We've used this a lot so far!)
- `!=`: Not equal to - True if operands are not equal eg. `x != y`
- `>=`: Greater than or equal to - True if left operand is greater than or equal to the right eg. `x >= y`
- `<=`: Less than or equal to - True if left operand is less than or equal to the right eg. `x <= y`

---
The logical operators in Python are `and`, `or`, `not` operators. These logical operators allow you to combine Boolean expressions and objects into more elaborate expressions.

### The `and` operator

Here is a Truth Table for the `and` operator:
| var1  | var2  |var1 `and` var2|
|:-----:|:-----:|:-------------:|
| True  | True  | True          |
| True  | False | False         |
| False | False | False         |
| False | True  | False         |

The `and` operator evaluates to `True` ONLY when all the conditions in the expression are `True`. If one of those conditions is `False`, the entire expression evaluates to `False`. For example:  
`5 > 3 and 5 == 3 + 2` evaluates to `True` but `5 < 3 and 5 == 5` evaluates to `False`.

### The `or` operator

Here is a Truth Table for the `or` operator:
| var1  | var2  |var1 `or` var2 |
|:-----:|:-----:|:-------------:|
| True  | True  | True          |
| True  | False | True          |
| False | False | False         |
| False | True  | True          |

The `or` operator evaluates to `True` as long as one of the conditions in the expression is `True`. If both of those conditions are `False`, the entire expression evaluates to `False`. For example:  
`5 > 3 or 5 == 3 + 2` evaluates to `True` and `5 < 3 or 5 == 5` also evaluates to `True`, but `5 < 3 or 5 == 6` evaluates to `False`

### The `not` operator

Python’s not operator allows you to invert the truth value of Boolean expressions and objects.

Here is a Truth Table for the `not` operator:
| var1  |not var1|
|:-----:|:-----: |
| True  | False  |
| False | True   |

The `not` operator negates the truth value of its operand. A true operand returns False. A false operand returns True. For example:

```python
>>> x = 2
>>> y = 5

>>> x > y
False

>>> not x > y
True
```

---

### Compound Boolean Expressions

You’ll typically use logical operators to build compound Boolean expressions, which are combinations of variables and values that produce a Boolean value as a result. In other words, Boolean expressions return `True` or `False`.

Comparisons and equality tests are common examples of this type of expression:

```python
>>> 5 == 3 + 2
True
>>> 5 > 3
True
>>> 5 < 3
False
>>> 5 != 3
True

>>> [5, 3] == [5, 3] # compare if two lists are the same
True

>>> "hi" == "hello" # compare if two strings are the same
False
```

All these expressions return `True` or `False`, which means they’re Boolean expressions. You can combine them using the `and` keyword to create compound expressions that test two—or more–subexpressions at a time:

```python
>>> (5 > 3) and (5 == 3 + 2)
True

>>> (5 < 3) and (5 == 5) and ((5 > 3) or (3 > 5))
False

>>> (5 == 5) and (not (5 != 5))
True

>>> ((5 < 3) and (5 != 5)) or (not (5 < 3) and (5 > 3))
True
```

When dealing with compound expressions, keep in mind that Python evaluates the expressions sequentially from left to right. Try to solve one expression completely and then move to the next, always ensure to respect all the above Truth Tables.

---
---

# Assignment Overview

James and Jane are bored and decide to play a game of cards against each other. Before they begin playing, they establish a few ground rules to ensure fairness:

- A standard deck of cards contains 52 cards divided into four suits: Hearts (H), Diamonds (D), Spades (S), and Clubs (C). The black cards are spades and clubs, while the red cards are hearts and diamonds. Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, and 2 are the cards in each suit.

- The cards are ranked from Ace to 2; so Ace beats King, which beats Queen, and so on. Jack is assigned a numerical value of 11, Queen is 12, King is 13, and Ace is 14.

- Each suit is given a numerical value based on the numerical equivalent of the letter it begins with. eg. In the Alphabet, A is the first letter and so is 1, Z is the last letter and is 26.

- The number on each card is added to the numerical value of its suit to determine how many points it's worth.  eg. 5 of Hearts will be worth 13 points.
  
- Each player will be dealt a deck of 5 cards and will take turns playing one card at a time, until the winner is determined at the end of the game. (Hint: each game will consist of 5 rounds of playing.)
  
- The order of play will be reversed if the second player's card beats the first player's card.

- The person who wins the most rounds of a game, wins the game.

- There will be three games. The person who wins the most games out of three is the overall winner of the card game.

During the final game of their card game, there appears to be a slight dispute so they consult their Python-savvy friend John. John decides that the best way to settle the dispute is to write a Python program to simulate their card game and then use the program to determine the winner. Each player secretly tells John their strategy of play, and John goes off to write an algorithm to simulate the game.

Given the game's complexity, John decides to use only Boolean expressions and NO conditionals to quickly simulate it. Read the comments in `card_game.py` to help John complete his algorithm for the simulation.

---

## Tasks

1. Create a new repo and name it:
`<your_name>-PyBools`. For example mine will be called: `fiifi-PyBools`
2. Place `card_game.py` in your repo and address all the comments in the file to complete the program.
3. Ensure the code runs with no errors.
4. Do not use any conditionals at all in the code. We haven't covered that yet. We're just using Boolean variables and expressions in this assignment.
5. Good luck! :)
