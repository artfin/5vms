import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# in minutes
t = [ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 18.0, 23.0, 28.0, 33.0, 38.0, 43.0, 48.0, 53.0, 58.0, 63.0 ]
ln_t = np.log( t )

h = [ 14.3, 14.3, 14.3, 14.2, 14.1, 14.0, 13.9, 13.8, 13.75, 13.7, 13.65, 13.6, 13.55, 13.5, 13.3, 13.25, 13.15, 13.10, 13.10, 13.05, 13.0, 13.0, 12.95 ]

#plt.scatter( t, h, s = 10, color = 'k', marker = '^' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

h0 = 14.5
h_inf = 12.5

difference = [ _ - h_inf for _ in h ]
difference0 = h0 - h_inf

begin = 3
end = 9

logs = [np.log( -np.log( diff / difference0 )) for diff in difference ]

fp, residual, rank, sv, rcond = sp.polyfit( ln_t[begin:end], logs[begin:end], 1, full = True )
f = sp.poly1d( fp ) 

x = np.linspace( min(ln_t[begin:end]), max(ln_t[begin:end]), 100 )

print("fp[0]: {0}; fp[1]: {1}".format(fp[0], fp[1]))
print(f(0))

#plt.plot( x, f(x), linewidth = 2.0, color = 'k')
#plt.scatter( ln_t[begin:end], logs[begin:end], marker = '^', color = 'k', s = 10 )
#plt.grid(linestyle = ':', alpha = 0.7)
#plt.show()
