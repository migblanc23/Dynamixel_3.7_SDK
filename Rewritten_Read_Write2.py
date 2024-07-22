import numpy as np
import dynamixel_client

PORT1 = '/dev/ttyUSB1'
PORT2 = '/dev/ttyUSB2'
BAUD = 57600
CALIBRATION = False
WRIST_CONTROL = False

motor_id = [1]
dxl_client = dynamixel_client(
 motor_id,PORT1, BAUD)
dxl_client.connect()
curr_pos = dxl_client.read_sync_pos(retries=10)
print(f"Motor ID: {motor_id}, Current Sync Position: {curr_pos}")

dxl_client.sync_write(
    motor_id, np.ones(len(motor_id))*5, 11, 1)  # 5 mode

def _read(self, event=None):
        for idx_port in [0, 1]:
            self.curr_pos[idx_port] = self.dxl_client[idx_port].read_sync_pos()

