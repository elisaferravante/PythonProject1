
gross = (input("Please provide your gross salary:"))
gross = int(gross)
children = (input("How many children do you have?"))
children = int(children)

if gross < 1000:
    tax = 0.1
elif gross < 2000:
    tax = 0.12
elif gross < 4000:
    tax = 0.14
else:
    tax = 0.18

if gross < 2000:
    tax_cut = children * 0.01
else:
    tax_cut = children * 0.005

effective_tax_rate = max(0, tax - tax_cut)


net_salary = gross * (1 - effective_tax_rate)

print(f"Your net salary is: {net_salary:.2f}")
print("Invalid input. Please enter numeric values for gross salary and number of children.")

