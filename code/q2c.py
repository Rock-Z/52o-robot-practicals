from wlkata_mirobot import WlkataMirobot
import sys

arm = WlkataMirobot(portname='COM3')
#arm.home()


if sys.argv[1] == '1e':
    arm.set_tool_pose(x=130,y=150,z=10)
if sys.argv[1] == '1f':
    angles = {1:135.0, 2:55.0, 3:10.0}
    arm.set_joint_angle(angles)