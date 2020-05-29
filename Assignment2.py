# Nick Monroe
# ECE 492
# Assignment 2

def computepay(hours, rate):
	totalpay = 0
	overtimehours = 0
	if hours > 40:
		overtimehours = hours - 40
		totalpay = 40 * rate
		totalpay += overtimehours * (rate * 1.5)
	else:
		totalpay = hours * rate
	return overtimehours, totalpay



Hours = int(input("Please enter the number of hours:")) 
RPH = int(input("Please enter the rate per hour:"))

overtime, total = computepay(Hours, RPH)

print("\nThe number of hours worked is: " + str(Hours))
print("The number of overtime hours worked is: " + str(overtime))
print("The gross pay is: " + str(total))
