# Assignment 05: Loops I

## Problem Statement

Imagine you work for a financial firm and you are tasked with projecting future earnings on a client's investment over the next four years using the following variable interest rates for each consecutive year: 2%, 3%, 1.5%, and 6%.

Prompt the client for their desired initial investment and use the formula below to calculate how much the investment will be worth after four years.

Display the client's investment worth to them after each year, and display their very final investment value.

```
new balance = old balance + (old balance × interest rate)
```

> **_NOTE:_**  The first "old balance" is the client's initial investment.
>
> **USEFUL HINTS:**
>
> 1. Use %.2f to format numbers to 2 decimal places
> 2. Use %% to format percent sign in a print statement that includes %.2f formatter.

## Sample Output

```
Enter your initial investment amount: $1000
Your investment value after year 1 with an interest rate of 2.0% is $1020.00
Your investment value after year 2 with an interest rate of 3.0% is $1050.60
Your investment value after year 3 with an interest rate of 1.5% is $1066.36
Your investment value after year 4 with an interest rate of 6.0% is $1130.34
Your final investment worth is $1130.34
```

```
Enter your initial investment amount: $2000
Your investment value after year 1 with an interest rate of 2.0% is $2040.00
Your investment value after year 2 with an interest rate of 3.0% is $2101.20
Your investment value after year 3 with an interest rate of 1.5% is $2132.72
Your investment value after year 4 with an interest rate of 6.0% is $2260.68
Your final investment worth is $2260.68
```
