import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

def download_and_convert_to_excel(url, excel_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract the required fields and create a list of dictionaries
    formatted_data = []
    for pokemon in data['pokemon']:
        pokemon_data = {
            'ID': pokemon['id'],
            'Number': pokemon['num'],
            'Name': pokemon['name'],
            'Image URL': pokemon['img'],
            'Type': ', '.join(pokemon['type']),
            'Height': pokemon['height'],
            'Weight': pokemon['weight'],
            'Candy': pokemon['candy'],
            'Candy Count': pokemon.get('candy_count', 0),
            'Egg': pokemon['egg'],
            'Spawn Chance': pokemon['spawn_chance'],
            'Average Spawns': pokemon['avg_spawns'],
            'Spawn Time': pokemon['spawn_time'],
            'Weaknesses': ', '.join(pokemon['weaknesses']),
            'Next Evolution': ', '.join([evolution['num'] + ': ' + evolution['name'] for evolution in pokemon.get('next_evolution', [])]),
            'Previous Evolution': ', '.join([evolution['num'] + ': ' + evolution['name'] for evolution in pokemon.get('prev_evolution', [])])
        }
        formatted_data.append(pokemon_data)

    # Convert the formatted data into a DataFrame
    df = pd.DataFrame(formatted_data)

    # Save the DataFrame as an Excel file
    df.to_excel(excel_file, index=False)

    print("Data downloaded and converted to Excel successfully!")


# Specify the link to download the data and the name of the Excel file to be generated
data_link = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
excel_file_name = "pokemon_data.xlsx"

# Call the function to download and convert the data
download_and_convert_to_excel(data_link, excel_file_name)

# Read the data from the Excel file
df = pd.read_excel(excel_file_name)

# Get all Pokemons whose spawn rate is less than 5%
spawn_rate_threshold = 5
pokemons_low_spawn_rate = df[df['Spawn Chance'] < spawn_rate_threshold]

# Plot: Pokemons with low spawn rate
plt.figure(figsize=(8, 6))
plt.bar(pokemons_low_spawn_rate['Name'], pokemons_low_spawn_rate['Spawn Chance'])
plt.xlabel('Pokemon')
plt.ylabel('Spawn Rate')
plt.title('Pokemons with Low Spawn Rate')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Get all Pokemons that have less than 4 weaknesses
max_weaknesses = 4
pokemons_few_weaknesses = df[df['Weaknesses'].apply(lambda x: len(x.split(','))) < max_weaknesses]

# Plot: Pokemons with few weaknesses
plt.figure(figsize=(8, 6))
plt.bar(pokemons_few_weaknesses['Name'], pokemons_few_weaknesses['Weaknesses'].apply(lambda x: len(x.split(','))))
plt.xlabel('Pokemon')
plt.ylabel('Number of Weaknesses')
plt.title('Pokemons with Few Weaknesses')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Get all Pokemons that have no multipliers at all
pokemons_no_multipliers = df[df['Candy Count'] == 0]

# Plot: Pokemons with no multipliers
plt.figure(figsize=(8, 6))
plt.bar(pokemons_no_multipliers['Name'], 1)  # Plotting a constant value for visualization
plt.xlabel('Pokemon')
plt.ylabel('No Multipliers')
plt.title('Pokemons with No Multipliers')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Get all Pokemons that do not have more than 2 evolutions
max_evolutions = 2
pokemons_few_evolutions = df[df['Next Evolution'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0) <= max_evolutions]

# Plot: Pokemons with few evolutions
plt.figure(figsize=(8, 6))
plt.bar(pokemons_few_evolutions['Name'], pokemons_few_evolutions['Next Evolution'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0))
plt.xlabel('Pokemon')
plt.ylabel('Number of Evolutions')
plt.title('Pokemons with Few Evolutions')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Get all Pokemons whose spawn time is less than 300 seconds
spawn_time_threshold = pd.to_datetime("00:05:00", format="%H:%M:%S").time()
df['Spawn Time'] = pd.to_datetime(df['Spawn Time'], format="%M:%S").dt.time
pokemons_low_spawn_time = df[df['Spawn Time'] < spawn_time_threshold]

# Plot: Pokemons with low spawn time
plt.figure(figsize=(8, 6))
plt.bar(pokemons_low_spawn_time['Name'], pokemons_low_spawn_time['Spawn Time'].apply(lambda x: x.minute * 60 + x.second))
plt.xlabel('Pokemon')
plt.ylabel('Spawn Time (Seconds)')
plt.title('Pokemons with Low Spawn Time')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Get all Pokemon who have more than two types of capabilities
min_capabilities = 2
pokemons_multiple_capabilities = df[df['Type'].apply(lambda x: len(x.split(','))) > min_capabilities]

# Plot: Pokemons with multiple capabilities
plt.figure(figsize=(8, 6))
plt.bar(pokemons_multiple_capabilities['Name'], pokemons_multiple_capabilities['Type'].apply(lambda x: len(x.split(','))))
plt.xlabel('Pokemon')
plt.ylabel('Number of Capabilities')
plt.title('Pokemons with Multiple Capabilities')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
