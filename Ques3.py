import requests
import json
import pandas as pd

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
