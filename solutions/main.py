import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

c = [ 2.0, 1.0, 0.67, 0.40 ]
eta = [0.605, 0.480, 0.443, 0.425 ]

fp, residual, rank, sv, rcond = sp.polyfit( c, eta, 1, full = True )
f = sp.poly1d( fp ) 

print("fp[0]: {0}; fp[1]: {1}".format(fp[0], fp[1]))

print(f(0))

x = np.linspace( min(c), max(c), 100 )

plt.plot( x, f(x), color = 'k', linestyle = '-', linewidth = 2.0 ) 
plt.scatter( c, eta, s = 20, color = 'k', marker = '^' )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()


