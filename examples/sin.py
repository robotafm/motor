# robotafm/motor/tests/sin.py

import math
import numpy as np
import matplotlib.pyplot as plt


rads = math.radians(120)
#print("sin:", math.sin(rads), math.sin(2*rads))
rads = math.radians(180)
#print("sin:", math.sin(0), math.sin(2*math.pi), math.sin(rads))

x = np.arange(1000)
y = np.sin(x/30)

plt.step(x+120, y, label='A')
plt.plot(x+120, y, 'o--', color='grey', alpha=0.3)

plt.step(x+240, y, where='mid', label='B')
plt.plot(x+240, y, 'o--', color='grey', alpha=0.3)

plt.step(x, y, where='post', label='C')
plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend(title='Parameter where:')
plt.title('Motor phases')
plt.show()

# PWM phases:
x = np.arange(40)
period = 10
time = np.zeros(40)

index = 0
for element in time:
	if (index % 2) == 1:
	    time[index] = 1
	x[index] = index + math.sin(index)
	index = index + 1

print(x)

plt.step(x, time, label="phase A")
plt.show()

