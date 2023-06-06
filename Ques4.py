import requests
import json
import csv

def download_and_convert_to_csv(url, csv_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract the required fields and create a list of dictionaries
    formatted_data = []
    for meteorite in data:
        meteorite_data = {
            'Name of Earth Meteorite': meteorite.get('name', ''),
            'ID of Earth Meteorite': meteorite.get('id', ''),
            'Nametype': meteorite.get('nametype', ''),
            'Recclass': meteorite.get('recclass', ''),
            'Mass of Earth Meteorite': float(meteorite.get('mass', 0)) if 'mass' in meteorite else 0.0,
            'Year': meteorite.get('year', '').split('T')[0],  # Extracting only the date part
            'Reclat': float(meteorite.get('reclat', 0)),
            'Reclong': float(meteorite.get('reclong', 0)),
            'Point Coordinates': meteorite.get('geolocation', {}).get('coordinates', []),
            'fall': (meteorite.get('fall',''))
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
