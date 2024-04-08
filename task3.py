#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

f = float(input("Enter the price of your first item> "))
s = float(input("Enter the price of your second item> "))
t = float(input("Enter the price of your third item> "))
fourth = float(input("Enter the price of your fourth item> "))
fifth = float(input("Enter the price of your fifth item> "))

sub = ( f + s + t + fourth + fifth )
tot = ( f + s + t + fourth + fifth ) * 1.12
tax = ( f + s + t + fourth + fifth ) * 0.12

sub = round(sub, 2)
tot = round(tot, 2)
tax = round(tax, 2)
print(f"You subtotal is ${sub} and your taxes total to ${tax} for a total of ${tot}")

