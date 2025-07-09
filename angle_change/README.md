z# Consider a robot:
1. It's geographic heading (angle between current meridian and the direction at which it points with it's face clockwise)
   is 0-360 degrees from meridian clockwise.
2. The waypoints that are targets for this robot are plotted with matplotlib and numpy modules for visualization.
   These waypoints on the graph are plotted relative to the Ox and Oy axes.
   Angles between these points and Ox axis are 0-360 degrees counterclockwise.
3. Our robot's face on this plot points upwards vertically, it is it's 0 degrees direction.
   ![fig1]{angle_change/Fig1.png}
5. In order to obtain the needed relative bearing angle for each of the waypoints,
   you have to substract the point's angle on the plot from (180*5/2) degrees and divide it by 360 degrees.
   The remainder that results from this division is the 0-360 deg angle measured clockwise from the face of the robot.
   the bearing of this robot relative to it's face direction.
6. To get the global bearing, you add this obtained angle to the current heading of your robot and divide it with remainder by 360 deg
   (% - modulo division), the remainder will be your target bearing.
