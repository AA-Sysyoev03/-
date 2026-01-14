import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,99)
y = np.maximum(0,x)
plt.plot(x,y, color='red', lw=2)
plt.title('ReLU')
plt.grid(True)
plt.show()