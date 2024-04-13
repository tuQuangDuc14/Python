import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extract Latd = Vĩ Độ and Longd = Kinh Độ
cities = pd.read_csv('california_cities.csv')
cities.head()

lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

plt.style.use('seaborn')
plt.figure(figsize=(8,6))
# Plot using Pyplot API
plt.scatter(lon, lat, 
            c=np.log10(population), cmap='viridis',
            s=area, linewidths=0, alpha=0.5)

plt.axis('equal')
plt.xlabel('longlatitude')
plt.ylabel('latitude');
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,7)

#Create a legend for cities'sizes
area_range = [50, 100, 300, 500]

for area in area_range:
    plt.scatter([], [],  s=area, c='k', alpha=0.4,
                label=str(area) + ' km$^2$')

plt.legend(labelspacing=1, title='City Area')


plt.title('California Cities: Population and Area Distribution');
plt.show()