


import matplotlib.pyplot as plt
import numpy as np

electric_kart_price = 65000  # Price of an electric kart in Dh
thermal_kart_price = 45000   # Price of a thermal kart in Dh
#0.9 dh 1kWh 14 dh 1L essence
electric_kart_cost_per_minute = 1.39  # Cost per minute for riding an electric kart in Dh
thermal_kart_cost_per_minute = 6.52    # Cost per minute for riding a thermal kart in Dh
#vitesse moyenne 70km/h 8min ca donne 9,33km -> 12.44kWh 11,19 DH, 3.73 litre essence 52,22 DH
riding_time = range(1, 90000)  # Riding time in minutes, range from 1 to 30 minutes 474 HOUR


# Calculate the TCO for each riding time
electric_kart_tco = [electric_kart_price + electric_kart_cost_per_minute * t for t in riding_time]
thermal_kart_tco = [thermal_kart_price + thermal_kart_cost_per_minute * t for t in riding_time]

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

# Add a legend
plt.legend()

# Show the plot
plt.show()
# si on suppose qu'on va rouler 3 heures par jour , on aura .. jours pour avoir 
# une depense en kart electrique qui depasse celle du thermique 
# cette etude n'a pas tenu en compte les frais de maintenance continu du kart thermique
