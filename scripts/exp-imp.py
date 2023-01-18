import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,2*np.pi)
y= np.sin(x)

# implicity
plt.plot(x,y,label="sin")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Plot")
plt.legend()
plt.show()

# explicity
fig = plt.figure(figsize=(6,6))
ax = plt.subplot(aspect=1)
ax.plot(x,y,label="sin") 
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y')  # Add a y-label to the axes.
ax.set_title("Plot")  # Add a title to the axes.
ax.legend() # Add a legend.
