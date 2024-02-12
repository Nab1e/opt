import matplotlib.pyplot as plt
import numpy as np

electric_kart_price = 90000  # Price of an electric kart in Dh
thermal_kart_price = 45000   # Price of a thermal kart in Dh
electric_kart_cost_per_minute = 1.39  # Cost per minute for riding an electric kart in Dh
thermal_kart_cost_per_minute = 6.52   # Cost per minute for riding a thermal kart in Dh
revenue_per_minute = 20  # Revenue per minute in Dh

riding_time = range(1, 10000)  # Riding time in minutes, range from 1 to 30 minutes

# Calculate the TCO for each riding time
electric_kart_tco = [electric_kart_price + electric_kart_cost_per_minute * t - revenue_per_minute * t for t in riding_time]
thermal_kart_tco = [thermal_kart_price + thermal_kart_cost_per_minute * t - revenue_per_minute * t for t in riding_time]

# Find the index of the intersection point
intersection_index = np.argmin(np.abs(np.array(electric_kart_tco) - np.array(thermal_kart_tco)))
intersection_time = riding_time[intersection_index]
intersection_tco = electric_kart_tco[intersection_index]

# Plot the TCO curve
plt.plot(riding_time, electric_kart_tco, label='Electric Kart')
plt.plot(riding_time, thermal_kart_tco, label='Thermal Kart')

# Mark the intersection point
plt.plot(intersection_time, intersection_tco, 'ro', label='Intersection')

# Add value text
plt.text(intersection_time, intersection_tco, f'({intersection_time} min)',
         verticalalignment='bottom', horizontalalignment='right')

# Add labels and title
plt.xlabel('Riding Time (minutes)')
plt.ylabel('Total Cost of Ownership (Dh)')
plt.title('TCO Comparison: Electric Kart vs Thermal Kart')

# Plot the intersection with the y-axis
intersection_index_y0 = np.argmin(np.abs(np.array(electric_kart_tco)))
intersection_time_y0 = riding_time[intersection_index_y0]
intersection_tco_y0 = electric_kart_tco[intersection_index_y0]

intersection_index_y0_thermal = np.argmin(np.abs(np.array(thermal_kart_tco)))
intersection_time_y0_thermal = riding_time[intersection_index_y0_thermal]
intersection_tco_y0_thermal = thermal_kart_tco[intersection_index_y0_thermal]

# Set the y-axis limits to provide space for the points
plt.ylim(-90000, max(max(electric_kart_tco), max(thermal_kart_tco)) + 5000)

# Plot the intersection points with y = 0
plt.plot(intersection_time_y0_thermal, 0, 'go', label='Intersection (Thermal) with y=0')
plt.text(intersection_time_y0_thermal, 0, f'({intersection_time_y0_thermal} min, 0 Dh)',
         verticalalignment='top', horizontalalignment='left')

plt.plot(intersection_time_y0, 0, 'bo', label='Intersection Electric with y=0')
plt.text(intersection_time_y0, 0, f'({intersection_time_y0} min, 0 Dh)',
         verticalalignment='bottom', horizontalalignment='right')

plt.legend()

# Show the plot
plt.show()
