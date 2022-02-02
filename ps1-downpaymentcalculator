annual_salary = float(input('What is your annual salary? (numbers only): '))
portion_saved = float(input('How much would you like to save each much? Enter a number from 0-100: '))/100
total_cost = float(input('What is the cost of your dream home? (numbers only): '))

portion_down_payment = 0.25
current_savings = 0
annualROI = 0.04
monthlyROI = annualROI/12
monthlySalary = annual_salary/12
down_payment_amount = total_cost * portion_down_payment
month = 0

while True:
	if current_savings >= down_payment_amount:
		print("It will take ", month, " months to save enough")
		break
	investmentIncrease = current_savings * monthlyROI
	savingsIncrease = investmentIncrease + monthlySalary * portion_saved
	current_savings += savingsIncrease
	month += 1
