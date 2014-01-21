import matplotlib.pyplot as plt
from numpy import *
from matplotlib import rcParams
# rcParams dict
rcParams['axes.labelsize'] = 18
rcParams['axes.linewidth'] = 2
rcParams['xtick.labelsize'] = 18
rcParams['ytick.labelsize'] = 18
rcParams['axes.labelweight'] = 'medium'
rcParams['xtick.major.width'] = 2
rcParams['ytick.major.width'] = 2
rcParams['xtick.minor.width'] = 1
rcParams['ytick.minor.width'] = 1
rcParams['legend.fontsize'] = 18
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['font.weight'] = 'medium'
rcParams['lines.linewidth'] = 2
#rcParams['text.usetex'] = True

fig=plt.figure()
x = linspace(0.0,6.28,100)
y = sin(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
fig.tight_layout(pad=0.1)
fig.savefig("test.pdf")
