#!/usr/bin/python
import rospy
import tf


def make_tf(name):
    br = tf.TransformBroadcaster()
    br.sendTransform((0, 0, 0), (1, 0, 0, 0), rospy.Time.now(), name, 'world')

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    name = rospy.get_param('~name')
    rospy.Timer(rospy.Duration(0.01), lambda e:make_tf(name))
    rospy.spin()


