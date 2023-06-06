import requests
import json
import csv
import matplotlib.pyplot as plt
import numpy as np

def download_and_convert_to_csv(url, csv_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract the required fields and create a list of dictionaries
    formatted_data = []
    for meteorite in data:
        year = meteorite.get('year', '')
        if year:
            try:
                year = int(year.split('T')[0])  # Extracting only the date part and convert to integer
            except ValueError:
                continue  # Skip this meteorite if the year cannot be converted to an integer

        meteorite_data = {
            'Name of Earth Meteorite': meteorite.get('name', ''),
            'ID of Earth Meteorite': meteorite.get('id', ''),
            'Nametype': meteorite.get('nametype', ''),
            'Recclass': meteorite.get('recclass', ''),
            'Mass of Earth Meteorite': float(meteorite.get('mass', 0)) if 'mass' in meteorite else 0.0,
            'Year': year,
            'Reclat': float(meteorite.get('reclat', 0)),
            'Reclong': float(meteorite.get('reclong', 0)),
            'Point Coordinates': meteorite.get('geolocation', {}).get('coordinates', []),
            'fall': meteorite.get('fall', '')
        }
        formatted_data.append(meteorite_data)

    # Define the field names for the CSV file
    field_names = formatted_data[0].keys()

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(formatted_data)

    print("Data downloaded and converted to CSV successfully!")


# Specify the link to download the data and the name of the CSV file to be generated
data_link = "https://data.nasa.gov/resource/y77d-th95.json"
csv_file_name = "meteorite_data.csv"

# Call the function to download and convert the data
download_and_convert_to_csv(data_link, csv_file_name)

# Read the data from the CSV file
with open(csv_file_name, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Get all the Earth meteorites that fell before the year 2000
meteorites_before_2000 = [meteorite for meteorite in data if meteorite['Year'] and int(meteorite['Year']) < 2000]

# Plot: Earth meteorites that fell before 2000
years = [int(meteorite['Year']) for meteorite in meteorites_before_2000]
plt.hist(years, bins=range(1800, 2001, 10), edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Earth Meteorites that Fell Before 2000')
plt.xticks(range(1800, 2001, 50))
plt.tight_layout()
plt.show()

# Get all the earth meteorites coordinates that fell before the year 1970
meteorites_before_1970 = [meteorite for meteorite in data if meteorite['Year'] and int(meteorite['Year']) < 1970]
coordinates = [(float(meteorite['Reclong']), float(meteorite['Reclat'])) for meteorite in meteorites_before_1970]

# Plot: Earth meteorites coordinates before 1970
longitudes = [coord[0] for coord in coordinates]
latitudes = [coord[1] for coord in coordinates]
plt.scatter(longitudes, latitudes, color='red', alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorites Coordinates Before 1970')
plt.tight_layout()
plt.show()

# Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg
meteorites_high_mass = [meteorite for meteorite in data if meteorite.get('Mass of Earth Meteorite', 0) and float(meteorite['Mass of Earth Meteorite']) > 10000]

# Plot: Earth meteorites with mass more than 10000kg
masses = [meteorite['Mass of Earth Meteorite'] for meteorite in meteorites_high_mass]
plt.hist(masses, bins=10**np.arange(4, 9), edgecolor='black', log=True)
plt.xscale('log')
plt.xlabel('Mass (kg)')
plt.ylabel('Count (log scale)')
plt.title('Earth Meteorites with Mass > 10000kg')
plt.tight_layout()
plt.show()
