# BRIEF INTRODUCTION

My name is Edmund Annobil. Originally from Ghana but have lived in US for about 6 years.
I have been in IT field for abt 4 years and currently working as a IT analyst.
Currently, I am aspiring to gain more skills in the field of Big Data Engineering. 
My hobbies include: 
  * Riding motorcycles
  * Reading tech blogs 
  * Swimming
*********************

# THREE PYTHON KEYWORDS
## The "while" statement
The "while" statement is used for repeated execution as long as an
expression is true:

   while_stmt ::= "while" assignment_expression ":" suite
                  ["else" ":" suite]

This repeatedly tests the expression and, if it is true, executes the
first suite; if the expression is false (which may be the first time
it is tested) the suite of the "else" clause, if present, is executed
and the loop terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause’s suite.  A "continue" statement
executed in the first suite skips the rest of the suite and goes back
to testing the expression.
## Class definitions
A class definition defines a class object (see section The standard
type hierarchy):

   classdef    ::= [decorators] "class" classname [inheritance] ":" suite
   inheritance ::= "(" [argument_list] ")"
   classname   ::= identifier

A class definition is an executable statement.  The inheritance list
usually gives a list of base classes (see Metaclasses for more
advanced uses), so each item in the list should evaluate to a class
object which allows subclassing.  Classes without an inheritance list
inherit, by default, from the base class "object"; hence,

   class Foo:
       pass

is equivalent to

   class Foo(object):
       pass



## The "for" statement

The "for" statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object:

   for_stmt ::= "for" target_list "in" expression_list ":" suite
                ["else" ":" suite]

## Further Elaboration

1. The expression list is evaluated once; it should yield an iterable
object. An iterator is created for the result of the
"expression_list". The suite is then executed once for each item
provided by the iterator, in the order returned by the iterator.  Each
item in turn is assigned to the target list using the standard rules
for assignments (see Assignment statements), and then the suite is
executed.  When the items are exhausted (which is immediately when the
sequence is empty or an iterator raises a "StopIteration" exception),
the suite in the "else" clause, if present, is executed, and the loop
terminates.

2. A "break" statement executed in the first suite terminates the loop
without executing the "else" clause’s suite.  A "continue" statement
executed in the first suite skips the rest of the suite and continues
with the next item, or with the "else" clause if there is no next
item.

3.  b The for-loop makes assignments to the variables in the target list.
This overwrites all previous assignments to those variables including
those made in the suite of the for-loop:

   for i in range(10):
       print(i)
       i = 5            
       
        this will not affect the for-loop
        because i will be overwritten with the next
        index in the range

For more python syntax, please visit [w3schools](http://www.w3schools.com)