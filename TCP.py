import socket
import time

# Robot's IP and port
robot_ip = "192.168.1.159"  # Replace with your robot's IP
robot_port = 5001           # Replace with the robot's TCP port

# Define joint angle configurations
joint_angles_list = [
    [-157.0567, 86.1409, 147.4224, 36.4356, -90.0002, 112.9435],
   
]

# Function to send joint angles over TCP
def send_joint_angles(sock, angles):
    # Construct a command string (format depends on robot's protocol)
    command = f"MOVEJ {','.join(map(str, angles))}\n"
    sock.sendall(command.encode())
    print(f"Sent command: {command.strip()}")

    # Optionally receive a response (if the robot sends acknowledgments)
    response = sock.recv(1024).decode()
    print(f"Response: {response}")

# Connect to the robot
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as robot_socket:
    robot_socket.connect((robot_ip, robot_port))
    print(f"Connected to robot at {robot_ip}:{robot_port}")

    # Send each set of joint angles
    for angles in joint_angles_list:
        send_joint_angles(robot_socket, angles)
        time.sleep(3)  # Adjust delay as needed

print("All movements completed.")
