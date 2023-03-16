from wlkata_mirobot import WlkataMirobot
import time
import sys

arm = WlkataMirobot(portname='COM3')
arm.home()


if sys.argv[1] == 'p2p':
    # Go to A
    arm.p2p_interpolation(x=130.0,y=150.0,z=10.0, wait_ok=True)
    time.sleep(2)
    # Interpolate to B
    arm.p2p_interpolation(x=-160.0, y=140.0, z=10.0)
if sys.argv[1] == 'linear':
    # Go to A
    arm.linear_interpolation(x=130.0,y=150.0,z=10.0)
    time.sleep(2)
    # Interpolate to B
    arm.linear_interpolation(x=-160.0, y=140.0, z=10.0)
if sys.argv[1] == 'door':
    # Set lift distance
    arm.set_door_lift_distance(50)
    # Go to A
    arm.set_tool_pose(x=130.0,y=150.0,z=10.0)
    time.sleep(2)
    # Interpolate to B
    arm.door_interpolation(x=-160.0, y=140.0, z=10.0)
if sys.argv[1] == 'circular':
    # Go to A
    arm.set_tool_pose(x=130.0,y=150.0,z=10.0, wait_ok=True)
    print(f"Arrived at {arm.pose}")
    time.sleep(2)
    # Interpolate to B
    arm.circular_interpolation(ex=-290, ey=-10, radius=300, is_cw=False, wait_ok=True)
    print(f"Interpolation complete! Now at {arm.pose}")