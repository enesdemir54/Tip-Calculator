print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? $"))

tip_perc = int(input("How much percent do you want to tip? 10, 12 or 15? %"))

c_people = int(input("How many people are you splitting the bills? "))

bill_with_tip = tip_perc / 100 * tot_bill + tot_bill

bill_pp = bill_with_tip / c_people

r_bill_pp = round(bill_pp, 2)

print(f"Total bill with the tip is {bill_with_tip}, Everyone needs to pay {r_bill_pp}.")

