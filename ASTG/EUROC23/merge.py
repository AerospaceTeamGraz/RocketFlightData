# this was used to merge the data from multiple csv files

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.signal import butter, filtfilt
from datetime import datetime
from scipy import integrate
#from plot import create_fig, save_fig, align_y_axes, remove_y_tick_labels


baro1 = pd.read_csv('bosch_barometer_1_data.csv')
baro2 = pd.read_csv('bosch_barometer_2_data.csv')
baro_te1 = pd.read_csv('te_barometer_1_data.csv')
baro_te2 = pd.read_csv('te_barometer_2_data.csv')
imu1 = pd.read_csv('imu_1_data.csv')
imu2 = pd.read_csv('imu_2_data.csv')
merge = pd.DataFrame(columns=['time_stamp', 'height_baro_1', 'height_baro_2', 'height_baro_te_1', 'height_baro_te_2', 
                              'temperature_baro_1', 'temperature_baro_2', 
                              'acceleration_x_imu_1', 'acceleration_y_imu_1', 'acceleration_z_imu_1', 
                              'acceleration_x_imu_2', 'acceleration_y_imu_2', 'acceleration_z_imu_2', 
                              'gyro_x_imu_1', 'gyro_y_imu_1', 'gyro_z_imu_1', 
                              'gyro_x_imu_2', 'gyro_y_imu_2', 'gyro_z_imu_2'])

merge['time_stamp'] = baro1['time_stamp']
merge['baro_1'] = baro1['pressure']
merge['baro_2'] = baro2['pressure']
merge['baro_te_1'] = baro_te1['pressure']
merge['baro_te_2'] = baro_te1['pressure']
merge['height_baro_1'] = 44330 * (1 - pow((baro1['pressure'] / 101325), (1.0 / 5.255)))
merge['height_baro_2'] = 44330 * (1 - pow((baro2['pressure'] / 101325), (1.0 / 5.255)))
merge['height_baro_te_1'] = 44330 * (1 - pow((baro_te1['pressure'] / 101325), (1.0 / 5.255)))
merge['height_baro_te_2'] = 44330 * (1 - pow((baro_te2['pressure'] / 101325), (1.0 / 5.255)))
merge['temperature_baro_1'] = baro1['temperature']
merge['temperature_baro_2'] = baro2['temperature']
merge['acceleration_x_imu_1'] = imu1['accel_x']
merge['acceleration_y_imu_1'] = imu1['accel_y']
merge['acceleration_z_imu_1'] = imu1['accel_z']
merge['acceleration_x_imu_2'] = imu2['accel_x']
merge['acceleration_y_imu_2'] = imu2['accel_y']
merge['acceleration_z_imu_2'] = imu2['accel_z']
merge['gyro_x_imu_1'] = imu1['gyro_x']
merge['gyro_y_imu_1'] = imu1['gyro_y']
merge['gyro_z_imu_1'] = imu1['gyro_z']
merge['gyro_x_imu_2'] = imu2['gyro_x']
merge['gyro_y_imu_2'] = imu2['gyro_y']
merge['gyro_z_imu_2'] = imu2['gyro_z']

merge = merge[merge['time_stamp'] >= 0]
merge = merge[merge['time_stamp'] <= 1000]


merge.to_csv("halcyon.csv")















