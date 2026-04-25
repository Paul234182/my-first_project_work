expenses = [
    {"date": "2026-04-01", "category": "Food", "amount": 25.50, "item": "Lunch"},
    {"date": "2026-04-02", "category": "Transport", "amount": 12.00, "item": "Bus fare"},
    {"date": "2026-04-03", "category": "Food", "amount": 40.00, "item": "Groceries"},
    {"date": "2026-04-04", "category": "Entertainment", "amount": 60.00, "item": "Movie"},
    {"date": "2026-04-05", "category": "Bills", "amount": 120.00, "item": "Electricity"},
    {"date": "2026-04-06", "category": "Food", "amount": 18.75, "item": "Breakfast"},
    {"date": "2026-04-07", "category": "Transport", "amount": 20.00, "item": "Taxi"},
    {"date": "2026-04-08", "category": "Shopping", "amount": 80.00, "item": "Clothes"},
    {"date": "2026-04-09", "category": "Food", "amount": 30.00, "item": "Dinner"},
    {"date": "2026-04-10", "category": "Bills", "amount": 50.00, "item": "Internet"},
    {"date": "2026-04-11", "category": "Entertainment", "amount": 25.00, "item": "Games"},
    {"date": "2026-04-12", "category": "Transport", "amount": 15.00, "item": "Bus fare"},
    {"date": "2026-04-13", "category": "Food", "amount": 22.00, "item": "Snacks"},
    {"date": "2026-04-14", "category": "Shopping", "amount": 150.00, "item": "Shoes"},
    {"date": "2026-04-15", "category": "Food", "amount": 35.00, "item": "Restaurant"}
]


""""Your program will be able to answer:

What is the total amount spent?
What is the average expense per transaction?
Which category has the highest spending?
How much was spent per category?
What was the most expensive single purchase?
How many transactions happened per category?"""

print(type(expenses))
total_amount= sum(expense['amount']for expense in expenses)
print(f"Total amount spent: ${total_amount:.3f}")

# what is the average expense per transaction
average_expense= total_amount/ len(expenses)
print(f"Average expense per transaction: ${average_expense:.3f}")
# which category has the highest spending
from collections import defaultdict# to create a dictionary that will store the total amount spent per category
category_totals= defaultdict(float)# to initialize the total amount spent per category to 0.0
for expense in expenses:
    category_totals[expense['category']] += expense['amount']# to add the amount spent on each expense to the corresponding category total
    highest_category= max(category_totals, key= category_totals.get)# to find the category with the highest total spending
    print(f'category with the highest spending: {highest_category} with total spending of ${category_totals[highest_category]:.3f}')
# how much was spent per category
print("Amount spent per category:")
for category, total in category_totals. items():
    print(f'{category}: ${total:.3f}')
# what was the most expensive single purchase
most_expensive_purchase= max(expenses, key= lambda x: x['amount'])# to find the expense with the highest amount
print(f"most expensive single purchase: {most_expensive_purchase['item']}with amount of ${most_expensive_purchase['amount']:.3f}")
# how many transactions happened per category
transaction_counts= defaultdict(int)# to create a dictionary that will store the count of transactions per category
for expense in expenses:
    transaction_counts[expense['category']] += 1# to increment the count of transactions for each category
print("Number of transactions per category:")
for category, count in transaction_counts.items():
    print(f'{category}: {count}')   
