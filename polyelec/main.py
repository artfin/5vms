import matplotlib.pyplot as plt
import numpy as np

v_prop = np.linspace( 0.0, 14.5, 30 )

ph_prop = [ 1.54, 2.03, 2.35, 2.51, 2.71, 2.83, 3.03, 3.17, 3.37, 3.51, 3.67, 3.81, 4.00, 4.20, 4.41, 4.72, 5.14, 5.60, 7.18, 8.10, 8.40, 8.62, 8.83, 9.04, 9.24, 9.44, 9.61, 9.81, 9.95, 10.11]

alpha_prop = [ _ / 8.75 for _ in v_prop[1:18] ]
print(len(alpha_prop)) 

pk_prop = [ ph - np.log10( alpha / (1 - alpha) ) for ph, alpha in zip(ph_prop[1:], alpha_prop)]
print(pk_prop)

v_pak = np.linspace( 0.0, 12.0, 25 )

ph_pak = [ 2.08, 3.00, 3.32, 3.82, 4.13, 4.34, 4.68, 4.85, 5.22, 5.40, 5.47, 5.65, 5.80, 6.10, 6.21, 6.41, 6.65, 6.84, 7.22, 7.46, 8.18, 8.90, 9.34, 9.73, 10.18 ]

alpha_pak = [ _ / 10.0 for _ in v_pak[1:20] ]
print(alpha_pak)

pk_pak = [ ph - np.log10( alpha / (1 - alpha) ) for ph, alpha in zip(ph_pak[1:], alpha_pak) ]

alpha_eta = [ 0.0, 0.05, 0.20, 0.40, 0.65, 0.90, 1.0, 1.05, 1.20 ]
eta = [ 0.34, 0.66, 2.46, 3.34, 3.17, 2.83, 2.56, 2.25, 1.68 ]

################################################################
#plt.scatter( v_prop, ph_prop, s = 30, marker = '^', color = 'r' )
#plt.scatter( v_pak, ph_pak, s = 30, marker = '^', color = 'b' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()
################################################################

################################################################
#plt.scatter( alpha_prop, pk_prop, s = 40, marker = '^', color = 'r' )
#plt.scatter( alpha_pak, pk_pak, s = 40, marker = '^', color = 'b' )
#plt.grid( linestyle = ':', alpha = 0.7 )
#plt.show()
################################################################

################################################################
plt.scatter( alpha_eta, eta, s = 40, marker = '^', color = 'k' )
plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()
################################################################

