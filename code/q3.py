from wlkata_mirobot import WlkataMirobot, WlkataMirobotTool
import time
import sys

arm = WlkataMirobot(portname='COM3')
arm.home()

if sys.argv[1] == 'gripper':
    arm.set_tool_type(WlkataMirobotTool.GRIPPER)
    arm.gripper_open()
    arm.set_tool_pose(x=200, y=0, z=10, wait_ok=True)
    arm.gripper_close()
    arm.linear_interpolation(x=200, y=0, z=100, wait_ok=True)
    print(f"Lifted! Now at {arm.pose}")
if sys.argv[1] == 'soft':
    arm.set_tool_type(WlkataMirobotTool.FLEXIBLE_CLAW)
    arm.pump_suction()
    arm.set_tool_pose(x=230, y=0, z=10, wait_ok=True)
    arm.pump_blowing()
    arm.linear_interpolation(x=230, y=0, z=100, wait_ok=True)
    print(f"Lifted! Now at {arm.pose}")
if sys.argv[1] == 'suction':
    arm.set_tool_type(WlkataMirobotTool.SUCTION_CUP)
    arm.set_tool_pose(x=210, y=0, z=-10, wait_ok=True)
    arm.pump_suction()
    arm.linear_interpolation(x=210, y=0, z=100, wait_ok=True)
    print(f"Lifted! Now at {arm.pose}")