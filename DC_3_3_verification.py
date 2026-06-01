
import matplotlib.pyplot as plt

target_voltage = 3.3
allow_margin = 0.05
spec_limit_max = target_voltage + allow_margin

measured_voltage = [3.31, 3.28, 3.42, 3.35, 3.29]
time_points = ["T1", "T2", "T3", "T4", "T5"]

plt.figure(figsize=(8,5))

plt.plot(time_points, measured_voltage, marker = 'o', color = 'blue', linewidth = 2,
         label = 'Measured Vpp')

plt.axhline(y=spec_limit_max, color = 'red', linestyle = '--', linewidth = 2, label = f'Spec Limit Max({spec_limit_max}V)')
plt.axhline(y=target_voltage, color = 'green', linestyle = ':', linewidth = 1.5, label = f'Target({target_voltage}V)')

plt.title("3.3V Power Rail Margin Verification", fontsize = 14, pad = 15)
plt.xlabel("Measurement Points", fontsize = 12)
plt.ylabel("Voltage(V)", fontsize = 12)
plt.grid(True, linestyle ='--', alpha = 0.6)
plt.legend(loc = 'upper right')

plt.ylim(3.20, 3.50)

plt.show()