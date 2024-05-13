# this was used to merge the data from multiple csv files

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.signal import butter, filtfilt
from datetime import datetime
from scipy import integrate
#from plot import create_fig, save_fig, align_y_axes, remove_y_tick_labels


sensors = pd.read_csv('rf_main_board_sensors.csv')
merge = pd.DataFrame(columns=['time_stamp', 'baro_1','baro_2','height_baro_1', 'height_baro_2', 
                              'temperature_baro_1', 'temperature_baro_2', 
                              'acceleration_x_imu_1', 'acceleration_y_imu_1', 'acceleration_z_imu_1', 
                              'acceleration_x_imu_2', 'acceleration_y_imu_2', 'acceleration_z_imu_2', 
                              'gyro_x_imu_1', 'gyro_y_imu_1', 'gyro_z_imu_1', 
                              'gyro_x_imu_2', 'gyro_y_imu_2', 'gyro_z_imu_2'])

merge['time_stamp'] = sensors['timestamp']
merge['baro_1'] = sensors['bosch_barometer_1_pressure']
merge['baro_2'] = sensors['bosch_barometer_2_pressure']
merge['height_baro_1'] = 44330 * (1 - pow((sensors['bosch_barometer_1_pressure'] / 101325), (1.0 / 5.255)))
merge['height_baro_2'] = 44330 * (1 - pow((sensors['bosch_barometer_2_pressure'] / 101325), (1.0 / 5.255)))
merge['temperature_baro_1'] = sensors['bosch_barometer_1_temperature']
merge['temperature_baro_2'] = sensors['bosch_barometer_2_temperature']
merge['acceleration_x_imu_1'] = sensors['imu_1_accel_x']
merge['acceleration_y_imu_1'] = sensors['imu_1_accel_y']
merge['acceleration_z_imu_1'] = sensors['imu_1_accel_z']
merge['acceleration_x_imu_2'] = sensors['imu_2_accel_x']
merge['acceleration_y_imu_2'] = sensors['imu_2_accel_y']
merge['acceleration_z_imu_2'] = sensors['imu_2_accel_z']
merge['gyro_x_imu_1'] = sensors['imu_1_gyro_x']
merge['gyro_y_imu_1'] = sensors['imu_1_gyro_y']
merge['gyro_z_imu_1'] = sensors['imu_1_gyro_z']
merge['gyro_x_imu_2'] = sensors['imu_2_gyro_x']
merge['gyro_y_imu_2'] = sensors['imu_2_gyro_y']
merge['gyro_z_imu_2'] = sensors['imu_2_gyro_z']

merge = merge[merge['time_stamp'] >= 0]
merge = merge[merge['time_stamp'] <= 500]


merge.to_csv("halcyon_manching.csv")















