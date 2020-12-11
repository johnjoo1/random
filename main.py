# Import dependencies
import random
import matplotlib.pyplot as plt

# Plot the values of random points
x = random.sample(range(1000), 100)
xbins = [0, len(x)]
plt.bar(range(0, 100), x)
plt.show()
plt.savefig('myHistogramFromPython.png', format='png')
