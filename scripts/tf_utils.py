import tf
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Quaternion


class TFdiffGetter():
  def __init__(self):
    self.listener = tf.TransformListener()
  def get(self):
    try:
      target_link = "eef_link"
      source_link = "base_link"
      (trans,rot) = self.listener.lookupTransform(source_link, target_link, rospy.Time(0))
      x = trans[0]
      y = trans[1]
      z = trans[2]
      eef_point = [x,y,z]
      return eef_point
    except:
      return None

