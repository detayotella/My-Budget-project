import budget

food = budget.Category("Food")
food.deposit(100_000, "initial deposit")
food.withdraw(10_000, "groceries")

clothing = budget.Category("Clothing")
food.transfer(5000, clothing)
clothing.withdraw(2500, "jeans")
clothing.withdraw(1500, "Watch")
entertainment = budget.Category("Entertainment")
food.transfer(10_000, entertainment)
entertainment.withdraw(4500, "Music Subcription")
entertainment.withdraw(6000, "Concert")
auto = budget.Category("Auto")
auto.deposit(1000_000, 'initial deposit')
auto.withdraw(15)

print(food)
print(clothing)
print(entertainment)

print(food.check_balance())