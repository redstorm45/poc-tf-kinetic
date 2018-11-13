#!/usr/bin/python
import rospy
import tf


def check_tfs(listener):
    try:
        (trans, rot) = listener.lookupTransform('world', 'turtle1')
        (trans, rot) = listener.lookupTransform('world', 'turtle1')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()

    rospy.Timer(rospy.Duration(0.1), lambda e:check_tfs(listener))

    rospy.spin()
