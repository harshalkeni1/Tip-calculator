#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}.format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

# ****Alternate Aproach*****

# total_bill_float = float(total_bill)
# tip_float = float(tip)
# people_int = int(people)
# tip_float_percent = tip_float / 100
# tip_float_percent_total = total_bill_float * tip_float_percent
# total_bill_float_tip = total_bill_float + tip_float_percent_total
# total_bill_float_tip_people = total_bill_float_tip / people_int
# total_bill_float_tip_people_round = round(total_bill_float_tip_people, 2)
# total_bill_float_tip_people_round = "{:.2f}".format(total_bill_float_tip_people)
# print(f"Each person should pay: ${total_bill_float_tip_people_round}")

                   
