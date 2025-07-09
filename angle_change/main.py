import numpy as np
import matplotlib.pyplot as pp
import math as mt
pp.axes(projection="polar")
# alfa on figure1
plot_angle = mt.pi*12/20
ks = np.arange(0, plot_angle, 0.01)
for k in ks:
    pp.polar(k, 0.7, marker='o',color='m')
# target_bearing_angle is beta in figure1
target_bearing_angle = ((5*mt.pi/2)-plot_angle) % (2*mt.pi)
ks = np.arange(0, target_bearing_angle, 0.01)
for k in ks:
    pp.polar(k, 1,marker='x',color='c')

pp.show()
