from numpy import *

# Need to make it 10.5 because arange does not include the last number
# so if it was 10 then program would not match the matlab version
x = arange(0, 10.5, 0.5)      # x = 0:0.5:10;

for i in x: 			      # for i = 1:length(x)
	y = i;					  #	y = x(i)
	print("y = " + str(y))
	z = i*i                   # z = x(i)^2
	print("z = " + str(z))
