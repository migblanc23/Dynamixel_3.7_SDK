import serial
import time
# import rospy

# from sensor_msgs.msg import JointState


# Replace with the actual serial port name (e.g., 'COM5' on Windows)
serial_port = 'dev/ttyACMO'
# serial_port = '/dev/ttyACM0'
# Set the baud rate to match your Teensy configuration
baud_rate = 57600

# # Create ROS publisher
# pub = rospy.Publisher('joint_states', JointState, queue_size=10)
# rospy.init_node('joint_state_publisher', anonymous=True)


# Open the serial port

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=0.1)
    print(f"Connected to: {ser.portstr}")
except serial.SerialException:
    print(f"Failed to open serial port {serial_port}.")
    exit()
current_state = {"force": 0, "velocity": 0, "amps": 0}
time1 = time.time()

try:
    while True:
        # Read data from the Teensy
        
        for i in range(3):
            data = ser.readline().decode().strip()
            # only print out current data
            if data.startswith("Current force:"):
                data = ser.readline().decode().strip()
                current_state["force"] = float(data)
            if data.startswith("Current speed:"):
                data = ser.readline().decode().strip()
                current_state["velocity"] = float(data)
            if data.startswith("Current amps:"):
                data = ser.readline().decode().strip()
                current_state["amps"] = float(data)
        
    
        # ser.flushInput()  # Clear input buffer
        # ser.flushOutput()  # Clear output buffer
        # send new goal angle to teensy
        data_type = "A"
        value = 0.0
        raw_data = f"{data_type}:{value}\n"
        ser.write(raw_data.encode())
        ser.flush()
        dt = time.time() - time1
        time1 = time.time()
        print(f"Current state: {current_state}")
        print(f"Time: {dt}")
        if dt > 1e-6:
            print(f"Frequency: {1/dt}")
        # if dt > 1e-5:
            # Publish the current state
        # joint_state = JointState()
        # joint_state.header.stamp = rospy.Time.now()
        # joint_state.name = ['joint1']
        # joint_state.position = [current_state["angle"]]
        # joint_state.velocity = [current_state["velocity"]]
        # joint_state.effort = [current_state["amps"]]
        # pub.publish(joint_state)

            # print(f"Current state: {current_state}")
            # print(f"Time: {dt}")
            # print(f"Frequency: {1/dt}")
            # print("\n")
        # if dt > 0.1:
        #     print(f"Current state: {current_state}")
        #     print(f"Time: {dt}")
        #     print(f"Frequency: {1/dt}")
        #     print("\n")
except KeyboardInterrupt:
    print("\nExiting due to keyboard interrupt.")
    ser.close()