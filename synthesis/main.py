import matplotlib as mpl 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
from dateutil import parser
import numpy as np
import scipy as sp

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

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

times1 = times[:length_first_exp]
vals1 = vals[:length_first_exp]

dt1 = [(t - times[0]).seconds for t in times1]
dv1 = [v - min(vals) for v in vals1] 

x = np.linspace( 0.0, max(dt1), 100 )

fp, residual, rank, sv, rcond = sp.polyfit( dt1, dv1, 1, full = True )
f = sp.poly1d( fp )

fig = plt.figure()
ax = plt.subplot(111)

lw = 2.0
plt.plot( dt1, dv1, color = 'k', linewidth = lw )
plt.plot( x, f(x), color = 'r', linestyle = 'dotted', linewidth = lw )

plt.grid( linestyle = ':', alpha = 0.7 )

plt.show()


