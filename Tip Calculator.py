# ---------------Project Tip Calculator--------------
bill = input("what was the total bill? $: ")
tip_percent = input("What percentage tip would you like to give?: ")
split_bill = input("How many people to split the bill?: ")
to_pay = ((int(bill) * (int(tip_percent) / 100)) + int(bill)) / int(split_bill)
print(f"Each person should pay: {round(to_pay,2)} $")