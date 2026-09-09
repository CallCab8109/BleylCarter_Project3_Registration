print("Carter Bleyl Tip Calculator App") #display app name

costOfMeal = float(input("Cost of meal: ")) #enter cost of meal
tipPercentage = int(input("Tip percent: ")) #enter tip percentage
print()
tipAmount = costOfMeal * (tipPercentage / 100) # calculate tip amount
print("Tip amount: ", round(tipAmount, 2)) #print and round tip amount
print("Total Amount: ", round(tipAmount + costOfMeal, 2)) #print and round total amount