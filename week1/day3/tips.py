# Program that calculates tips and tax on a restaurant bill
# by Anthony Rodriguez
# 11072023

meal = 53.48
tax_rate = .07
tip_rate = .18

tip = (meal * tip_rate)
tax_amt = (meal * tax_rate)
total_cost = (meal + tax_amt + tip)
print ("Restaurant Receipt")
print()
print("Meal: $", meal)
print()
print("Tax: $", tax_amt)
print()
print("Tip: $", tip)
print()
print("Total: $", total_cost)