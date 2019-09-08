import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,'r--',x,z,'b--')
plt.title('sin_cos')
plt.show()



