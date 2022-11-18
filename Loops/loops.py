old_balance = input('Enter your initial investment: $')
interest_rates = [0.02, 0.03, 0.015, 0.06]

for idx, interest in enumerate(interest_rates):
    new_balance = float(old_balance) + (float(old_balance) * interest)
    interest = interest * 100
    new_balance = "%.2f" % new_balance
    print(f"Your investment value after year {idx + 1} with an interest rate of {interest}% is ${new_balance}")
    old_balance = new_balance
print(f"Your final investment worth is ${new_balance}")   
      