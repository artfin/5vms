import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import scipy as sp

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'
mpl.rcParams['text.latex.preamble'] = [
    r"\usepackage{amsmath}"
]

mpl.rcParams['figure.titlesize'] = "x-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"

mpl.rcParams['xtick.labelsize'] = "x-large"
mpl.rcParams['ytick.labelsize'] = "x-large"

#############################################################################

vhcl1 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 7.0, 8.0, 9.0, 10.0]
ph1 = [13.25, 13.32, 13.39, 13.43, 13.21, 13.25, 12.9, 12.7, 12.4, 12.0, 11.1, 9.2, 7.4, 6.9, 6.55, 3.23, 2.67, 2.44, 2.28]

#############################################################################

vhcl2 = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 7.0, 8.0, 9.0, 10.0]
ph2 = [13.51, 13.56, 13.61, 13.60, 13.58, 13.07, 11.06, 8.07, 7.4, 7.12, 6.96, 6.8, 6.68, 6.5, 6.36, 3.6, 2.78, 2.48, 2.33]

#############################################################################

vhcl3 = [0.0, 1.0, 2.0, 3.0, 3.5, 4.0, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 7.0, 8.0, 9.0, 10.0]
ph3 = [13.58, 13.65, 13.66, 13.56, 11.85, 8.52, 7.27, 7.11, 7.01, 6.93, 6.84, 6.71, 6.67, 6.52, 6.45, 6.36, 6.26, 4.04, 2.91, 2.52, 2.32]

############################################################################

vhcl4 = [0.0, 1.0, 2.0, 2.5, 2.9, 3.0, 3.1, 3.6, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0]
ph4 = [13.53, 13.45, 13.34, 12.61, 11.6, 10.14, 8.68, 7.72, 7.35, 7.27, 7.2, 7.12, 7.03, 6.93, 6.91, 6.82, 6.78, 6.66, 6.68, 6.63, 6.38, 6.09, 4.39, 2.76, 2.35, 2.31]

############################################################################

vhcl5 = [0.0, 1.0, 2.0, 2.26, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
ph5 = [13.45, 13.4, 12.23, 10.3, 8.34, 7.83, 7.72, 7.59, 7.48, 7.36, 7.3, 7.26, 7.2, 7.1, 7.07, 6.98, 6.91, 6.87, 6.81, 6.78, 6.55, 6.27, 5.78, 2.85, 2.53, 2.41, 2.28]

lw = 2.2
_size = 30
#plt.plot( vhcl1, ph1, color = 'red', linewidth = lw )
#plt.scatter( vhcl1, ph1, color = 'red', s = _size, marker = '^')

#plt.plot( vhcl2, ph2, color = 'blue', linewidth = lw )
#plt.scatter( vhcl2, ph2, color = 'blue', s = _size, marker = '^')

#plt.plot( vhcl3, ph3, color = 'green', linewidth = lw )
#plt.scatter( vhcl3, ph3, color = 'green', s = _size, marker = '^')

#plt.plot( vhcl4, ph4, color = 'black', linewidth = lw )
#plt.scatter( vhcl4, ph4, color = 'black', s = _size, marker = '^')

#plt.plot( vhcl5, ph5, color = 'orange', linewidth = lw )
#plt.scatter( vhcl5, ph5, color = 'orange', s = _size, marker = '^')

#plt.vlines( 6.1, 0.0, 14.0, color = 'red', linewidth = lw, linestyle = 'dotted' )
#plt.vlines( 5.6, 0.0, 14.0, color = 'blue', linewidth = lw, linestyle = 'dotted' )
#plt.vlines( 3.77, 0.0, 14.0, color = 'green', linewidth = lw, linestyle = 'dotted' )
#plt.vlines( 3.02, 0.0, 14.0, color = 'black', linewidth = lw, linestyle = 'dotted' )
#plt.vlines( 2.26, 0.0, 14.0, color = 'orange', linewidth = lw, linestyle = 'dotted' )

#plt.xlabel(r'V (HCl), ml')
#plt.ylabel(r'pH')

#plt.xlim((-0.1, 10.1))
#plt.ylim((0.0, 14.0))

#plt.grid( linestyle = ':', alpha = 0.7 )

#plt.show()

v0 = 0.03 # l
c_acid = 0.1 # mol / l
v0_naoh = 0.1901 / 5.0 / 40.0 / 30.0 * 1000.0 # mol /l
print('vo_naoh: {0}'.format(v0_naoh))

v_mediums = [0.0061, 0.0056, 0.00377, 0.00302, 0.00226] 

c_naoh = []
c_naoh.append( 0.1901 / 40.0 / 0.16 )
for v_acid in v_mediums:
    c_naoh.append( v_acid * c_acid / ( v0 + v_acid) )

print('c_naoh: {0}'.format(c_naoh))

times = [0.0, 7.0, 14.0, 21.0, 28.0, 35.0]

#plt.plot( times, c_naoh, color = 'black', linewidth = lw)
#plt.scatter( times, c_naoh, color = 'black', s = _size, marker = '^' )

#plt.xlabel(r'Time, min')
#plt.ylabel(r'C(NaOH), M')

#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()

t_prime = []
t_prime.append( (c_naoh[0] + c_naoh[1]) / 2.0 * times[1] )
t_prime.append( t_prime[-1] + ( c_naoh[1] + c_naoh[2]) / 2.0 * (times[2] - times[1]) )
t_prime.append( t_prime[-1] + ( c_naoh[2] + c_naoh[3]) / 2.0 * (times[3] - times[2]) )
t_prime.append( t_prime[-1] + ( c_naoh[3] + c_naoh[4]) / 2.0 * (times[4] - times[3]) )
t_prime.append( t_prime[-1] + ( c_naoh[4] + c_naoh[5]) / 2.0 * (times[5] - times[4]) )

print(t_prime)

c0_pva = 0.6048 / 86.09 / 0.16 # mol/l

A = []
for i in range(1, 6):
    A.append( 1 - (c_naoh[0] - c_naoh[i]) / c0_pva  )

print(A)

A_ln = np.log( A )

print(A_ln)

fp, residual, rank, sv, rcond = sp.polyfit( t_prime[1:], -A_ln[1:], 1, full = True )
print('fp[0]: {0}; fp1[]: {1}'.format(fp[0], fp[1]))
f = sp.poly1d( fp )

x = np.linspace( min(t_prime), max(t_prime), 100 )

plt.plot( t_prime, - A_ln, color = 'black', linewidth = lw )
plt.plot( x, f(x), color = 'black', linewidth = lw, linestyle = ':')
plt.scatter( t_prime, - A_ln, color = 'black', s = _size )

plt.xlabel(r't$^\prime$, M$\cdot$min')
plt.ylabel(r'- ln A')

plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()
