#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('topics_quiz_node', anonymous=True)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

msg = Twist()
def callback(msg): 
    print (msg)

    if msg.ranges[360]>1:#change the laser from 300 to 360 since that is the forward pointing laser

        print('Forward',msg.ranges[359])

        msg.linear.x = 0.3   #keep the speed small giving the robot more reaction time

        msg.angular.z = 0

        pub.publish(msg)

    elif msg.ranges[360]<1:#change the laser from 300 to 360 since that is the forward pointing laser

        print('move left')

        msg.linear.x = 0

        msg.angular.z = 0.6

        pub.publish(msg)

    elif msg.ranges[0]<1:#change the laser from 300 to 360 since that is the forward pointing laser

        print('move left')

        msg.linear.x = 0

        msg.angular.z = 0.6

        pub.publish(msg)

    elif msg.ranges[719]<1:#change the laser from 300 to 360 since that is the forward pointing laser

        print('move right')

        msg.linear.x = 0

        msg.angular.z = -0.6

        pub.publish(msg)






       
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
     
rospy.spin()