from matplotlib.pyplot import *
from numpy import *

# t = arange(0, 1, 0.01)
# y = sin(2*pi*t)
#
# figure(1)
# clf()
# plot(t, y)
#
# xlabel('Time (sec)')
# ylabel('y(t)')
#
# show()

t = arange(1, 3, 0.02)
T = 6*log(t) - 7*exp(0.2*t)

figure(1)
clf()
plot(t, T)

title('Monroe-Plot')
xlabel('Time (min)')
ylabel('Degrees (Celsius)')

print('Hello World! I just wrote my first Python program. Yayyyyyyyy')
print('Nick Monroe')

show()
