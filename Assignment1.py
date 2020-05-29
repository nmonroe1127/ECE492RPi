# Nick Monroe
# ECE 492
# Assignment 1

Hours = int(input("Please enter the number of hours:")) 
RPH = int(input("Please enter the rate per hour:"))

print("The user given hours are equal to: " + str(Hours))
print("The user given rate per hour is equal to: " + str(RPH))
overtime = 1.5 * RPH
print("This gives an overtime pay rate of: " + str(overtime))