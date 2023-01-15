print("Welcome to the Tip Calculator.")
bill_total = input("What was the total bill? $")
num_people = input("How many people to split the bill? ")
tip_percentage = input(
    "What percent tip would you like to give? 10 12 15 20? ")

# payperperson = total / people * tip_percent
# total / people + papperperson

tip_amount = ((float(bill_total)/int(num_people))*int(tip_percentage))/10012
pay_amount = (float(bill_total)/int(num_people))+float(tip_amount)

print("Each person should pay: "+str("{:.2f}".format(pay_amount)))
