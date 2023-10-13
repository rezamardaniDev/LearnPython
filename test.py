import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)  
p = np.pi/6  
y = 4 * np.cos(5*t + p)  

plt.plot(t, y)  
plt.xlabel('t')  
plt.ylabel('y')  
plt.title('نمودار 4cos(5t+p/6)') 

plt.show()
