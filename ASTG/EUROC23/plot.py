import pandas as pd
import matplotlib.pyplot as plt

# Read the merged data from the CSV file
merge = pd.read_csv("halcyon_euroc.csv")

# Plot the height baro values
plt.figure(figsize=(10, 6))
plt.plot(merge['time_stamp'], merge['height_baro_1'], label='Height Baro 1')
plt.plot(merge['time_stamp'], merge['height_baro_2'], label='Height Baro 2')
# plt.plot(merge['time_stamp'], merge['height_baro_te_1'], label='Height Baro TE 1') #these are weird 
# plt.plot(merge['time_stamp'], merge['height_baro_te_2'], label='Height Baro TE 2') #these are weird
plt.xlabel('Timestamp')
plt.ylabel('Height Barometer')
plt.title('EUROC 2023 - HALCYON')
plt.legend()
plt.grid(True)
plt.savefig('halcyon_euroc.png')
plt.show()
