import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the provided link
data_url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(data_url)

# Check if the columns exist before accessing them
if 'Qualified' in df.columns:
    # Get all the cars and their types that do not qualify for clean alternative fuel vehicle
    non_clean_cars = df.loc[df['Qualified'] == 'No', ['Make', 'Vehicle Type']]
    print("Cars and Types that do not qualify for clean alternative fuel vehicle:")
    print(non_clean_cars)
    print()
else:
    print("Column 'Qualified' not found in the dataset.")

if 'Make' in df.columns and 'City' in df.columns:
    # Get all TESLA cars with the model year and made in Bothell City
    tesla_cars_bothell = df.loc[(df['Make'] == 'TESLA') & (df['City'] == 'BOTHELL'), ['Make', 'Model Year']]
    print("TESLA cars with Make and Model Year made in Bothell City:")
    print(tesla_cars_bothell)
    print()
else:
    print("Columns 'Make' or 'City' not found in the dataset.")

if 'Electric Range' in df.columns and 'Model Year' in df.columns:
    # Get all the cars that have an electric range of more than 100 and were made after 2015
    electric_cars_range_100 = df.loc[(df['Electric Range'] > 100) & (df['Model Year'] > 2015), :]
    print("Cars with Electric Range > 100 and made after 2015:")
    print(electric_cars_range_100)
    print()
else:
    print("Columns 'Electric Range' or 'Model Year' not found in the dataset.")

# Draw plots to show the distribution between city and electric vehicle type
if 'City' in df.columns:
    plt.figure(figsize=(10, 6))
    df['City'].value_counts().plot(kind='bar')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.title('Distribution of Electric Vehicles by City')
    plt.show()
else:
    print("Column 'City' not found in the dataset.")

if 'Electric Vehicle Type' in df.columns:
    plt.figure(figsize=(10, 6))
    df['Electric Vehicle Type'].value_counts().plot(kind='bar')
    plt.xlabel('Electric Vehicle Type')
    plt.ylabel('Count')
    plt.title('Distribution of Electric Vehicles by Type')
    plt.show()
else:
    print("Column 'Electric Vehicle Type' not found in the dataset.")