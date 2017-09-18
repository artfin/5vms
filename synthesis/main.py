import matplotlib as mpl 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
from dateutil import parser
import numpy as np
import scipy as sp

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'

mpl.rcParams['figure.titlesize'] = 'xx-large'
mpl.rcParams['legend.fontsize'] = 'large'
mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['axes.titlesize'] = 'large'

mpl.rcParams['xtick.labelsize'] = 'large'
mpl.rcParams['ytick.labelsize'] = 'large'

def read_file( filename ):
    with open( filename, mode = 'r' ) as inputfile:
        lines = inputfile.readlines()

    times = []
    vals = []

    for line in lines:
        if '#' not in line and len(line) > 1:
            # print("line: {0}; len(line): {1}".format(line, len(line)))
            data = line.split()
            
            times.append( parser.parse(data[0]) )
            vals.append( float(data[1]) )

    return times, vals 

times, vals = read_file( 'exp_12_09_17.txt' )

length_first_exp = 29
length_second_exp = 22
length_third_exp = 20 

# first exp
times1 = times[:length_first_exp]
vals1 = vals[:length_first_exp]
# second exp
times2 = times[(length_first_exp + 1) : (length_first_exp + length_second_exp)]
vals2 = vals[(length_first_exp + 1) : (length_first_exp + length_second_exp)]
# third exp
times3 = times[(length_first_exp + length_second_exp + 1) : (length_first_exp + length_second_exp + length_third_exp)]
vals3 = vals[(length_first_exp + length_second_exp + 1) : (length_first_exp + length_second_exp + length_third_exp)]

dt1 = [(t - times1[0]).seconds for t in times1]
dv1 = [v - min(vals1) for v in vals1] 

dt2 = [(t - times2[0]).seconds for t in times2]
dv2 = [v - min(vals2) for v in vals2]

dt3 = [(t - times3[0]).seconds for t in times3]
dv3 = [v - min(vals3) for v in vals3]

x1 = np.linspace( 0.0, max(dt1), 100 )
x2 = np.linspace( 0.0, max(dt2), 100 )
x3 = np.linspace( 0.0, max(dt3), 100 )

fp1, residual, rank, sv, rcond = sp.polyfit( dt1, dv1, 1, full = True )
fp2, residual, rank, sv, rcond = sp.polyfit( dt2[5:], dv2[5:], 1, full = True )
fp3, residual, rank, sv, rcond = sp.polyfit( dt3[6:], dv3[6:], 1, full = True )

f1 = sp.poly1d( fp1 )
f2 = sp.poly1d( fp2 )
f3 = sp.poly1d( fp3 )

fig = plt.figure()
ax = plt.subplot(111)

radius = 0.2 # cm
molar_mass = 100.12 # g / mol
volume0 = 10 * ( 1 + 0.001 * (70 - 20) ) / 1000.0 # l
deltam =  1 / 0.899 -1 / 1.190 # cm**3 / g

vp1 = np.pi * radius**2 / (volume0 * deltam * molar_mass ) * fp1[0] / 10.0 # fp is in mm/s
vp2 = np.pi * radius**2 / (volume0 * deltam * molar_mass ) * fp2[0] / 10.0
vp3 = np.pi * radius**2 / (volume0 * deltam * molar_mass ) * fp3[0] / 10.0 
print('vp1: {0}'.format(vp1))
print('vp2: {0}'.format(vp2))
print('vp3: {0}'.format(vp3))

# inic_concentrations = [ 2.0, 4.0, 8.0 ]
#inic_concentrations_log  = [ np.log(i / 242.23) for i in inic_concentrations ]

mma_concetrations = [ 1.872, 3.744, 7.488 ]
mma_concetrations_log = [ np.log( mma ) for mma in mma_concetrations ]
vp_log = [ np.log(vp1), np.log(vp2), np.log(vp3) ]

print(mma_concetrations_log)

#fp4, residual, rank, sv, rcond = sp.polyfit( inic_concentrations_log, vp_log, 1, full = True )
fp4, residual, rank, sv, rcond = sp.polyfit( mma_concetrations_log, vp_log, 1, full = True )
f4 = sp.poly1d( fp4 )
x4 = np.linspace(0, 2.5, 100 )
print('fp4[0]: {0}'.format(fp4[0]))

lw = 2.0

delta_t_23 = fp2[1] - fp3[1]
print('delta_t_23: {0}'.format(delta_t_23))
tempo_conc = 1.5 * 10**(-4)
inhib_velocity = tempo_conc / delta_t_23
print('inhib_velocity: {0}'.format(inhib_velocity))
#plt.plot( dt1, dv1, color = 'k', linewidth = lw )
#plt.plot( x1, f1(x1), color = 'r', linestyle = 'dotted', linewidth = lw )

plt.ylim((0, 7))

#plt.plot( dt2, dv2, color = 'k', linewidth = lw )
#plt.plot( x2, f2(x2), color = 'r', linestyle = 'dotted', linewidth = lw )
plt.plot( dt3, dv3, color = 'k', linewidth = lw )
plt.plot( x3, f3(x3), color = 'r', linestyle = 'dotted', linewidth = lw )

# plt.scatter( inic_concentrations_log, vp_log, color = 'k', marker = 'o', s = 40 )
# plt.scatter( mma_concetrations_log, vp_log, color = 'k', marker = 'o', s = 40 )
# plt.plot( x4, f4( x4 ), color = 'r', linestyle = 'dotted', linewidth = lw )

#plt.title(r'\Large First experiment')
# plt.title(r'\Large Second experiment')
plt.title(r'\Large Third experiment')
plt.xlabel(r'Time, s')
plt.ylabel(r'h, mm')

#plt.title(r'Log-Log plot')
#plt.xlabel(r'Log [M]')
#plt.ylabel(r'Log V$_\textup{p}$')

plt.grid( linestyle = ':', alpha = 0.7 )

plt.show()


