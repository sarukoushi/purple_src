# In order to obtain bearing, add current heading
#   to the waypoint azimuth and modulo divide (%) it by 360

# BoxyShelly class:
#  Methods:
#    plot_it()
#       plots waypoints using matplotlib
#    r_buffer()
#        returns r_buffer with waypoints radiuses relative to the current position
#    r_azi_buffer()
#        returns azimuths of waypoints relative to the current heading, 
#        clockwise 0-360 degrees
#    print_r()
#       prints contents of the main two buffers with radiuses and azimuths
#       relative to the current heading
#     


import matplotlib.pyplot as plt
# import matplotlib.patches as Circle
import math as mt
# import numpy as np

class  BoxyShelly:
    def __init__(self):
        # Initialize starting point
        self.x, self.y = [0], [0]
        self.start_r = 1
        self.off = 1
        # Directions: right, up, left, down
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        self.current_direction = 0  # Start moving right
        self.counter = 1
        # Build the spiral with two steps per r
        self.x.append(self.x[-1] + (self.start_r+self.off)/2)
        self.y.append(self.y[-1] - (self.start_r+self.off)/2)
        
        self.r_azi_buff = []
        self.r_buff = []

        for r in range(self.start_r, 12):
            # r += self.off
            for _ in range(2):  # Take two turns for each r
                if self.counter < (12*2) -2: 
                    dx, dy = self.directions[self.current_direction % 4]
                    self.x.append(self.x[-1] + dx * r)
                    self.y.append(self.y[-1] + dy * r)
                    self.current_direction += 1
                    self.counter += 1
        
        for i in range(1,len(self.x)):
            bearing = mt.atan2(self.y[i],self.x[i]) 
            bearing = ( bearing if bearing >= 0 else bearing + (2*mt.pi) ) * 180 / mt.pi
            bearing = ((5*180/2)-bearing) % (360)
            self.r_azi_buff.append(bearing)
            r = mt.sqrt( ((self.x[i])**2) + ((self.y[i])**2) )
            self.r_buff.append(r)

    def r_buffer(self):
        return self.r_buff
    def r_azi_buffer(self):
        return self.r_azi_buff
        # Plot the spiral
    def plot_it(self):
        fig,ax = plt.subplots()
        area = plt.Circle((self.x[1],self.y[1]),5,fill=False)
        ax.add_artist(area)
        for i in range(0,len(self.r_buff)+1):
            errcircle = plt.Circle((self.x[i],self.y[i]),0.5,fill=True)
            ax.add_artist(errcircle)
        plt.scatter(self.x,self.y,marker='o',color='m')
        plt.grid(True)
        plt.axis('equal')     
        plt.show()

    def print_r(self):
        print("r is {}: \n{}\nr_azi: \n{}".format(len(self.r_buff),self.r_buff,self.r_azi_buff))
