import matplotlib.pyplot as plt
import numpy as np

v = [ 115.0, 210.0, 460.0 ]
xi = [ 0.7723, 0.7171, 0.7167 ]
xi_tg = [ np.tan(_) for _ in xi ] 
print(xi_tg)

plt.plot( v, xi, color = 'k', linewidth = 2.0 )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()
