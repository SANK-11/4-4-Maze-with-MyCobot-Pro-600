import time
from pymycobot.mycobot import MyCobot

# Initialize the MyCobot Pro 600 connection
# Update the port to match your setup (e.g., "/dev/ttyUSB0" for Linux or "COM3" for Windows)
robot = MyCobot(port="COM3", baudrate=115200)

# Define an array of joint angle configurations
# Each row corresponds to a set of joint angles (in degrees) for joints 1 to 6
joint_angles_list = [
    [-57.7382, -44.4341, 107.7240, 26.7094, 90.0002, 32.2625],
    [-30.0000, -50.0000, 100.0000, 30.0000, 85.0000, 40.0000],
    [-45.0000, -30.0000, 110.0000, 25.0000, 90.0000, 35.0000],
]

# Define the speed (1-100)
movement_speed = 50

# Function to move the robot to each set of joint angles
def move_robot_to_joint_angles(robot, joint_angles_list, speed):
    for index, angles in enumerate(joint_angles_list):
        print(f"Moving to position {index + 1}: {angles}")
        
        # Send joint angles to the robot
        robot.send_angles(angles, speed)
        
        # Wait for the robot to reach the position
        # Adjust the sleep duration based on the movement complexity
        time.sleep(3)
        
        # Optionally, verify the robot's position
        current_angles = robot.get_angles()
        print(f"Current Joint Angles: {current_angles}\n")

# Execute the movement sequence
print("Starting movement sequence...")
move_robot_to_joint_angles(robot, joint_angles_list, movement_speed)
print("Movement sequence completed.")

# Disconnect the robot
robot.release_all_servos()
print("Robot released and program completed.")
