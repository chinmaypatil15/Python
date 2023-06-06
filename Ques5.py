import requests
import json
from bs4 import BeautifulSoup
import re

def download_and_extract_data(url):
    # Download the data from the API link
    response = requests.get(url)
    data = response.json()

    # Extract the required data attributes
    episode_name = data['name']
    season_number = extract_season_number(episode_name)

    episode_data = {
        'id': data['id'],
        'url': data['url'],
        'name': episode_name,
        'season': season_number,
        'number': data.get('number'),  # Use get() method to handle missing 'number' attribute
        'type': data['type'],
        'airdate': data.get('airdate'),
        'airtime': data.get('airtime'),
        'runtime': data['runtime'],
        'average_rating': data['rating']['average'],
        'summary': BeautifulSoup(data['summary'], 'html.parser').get_text(),
        'medium_image': data['image']['medium'],
        'original_image': data['image']['original']
    }

    return episode_data

def extract_season_number(episode_name):
    # Extract the season number from the episode name using regular expressions
    season_pattern = r'season\s*(\d+)'
    matches = re.findall(season_pattern, episode_name, flags=re.IGNORECASE)

    if matches:
        return int(matches[0])
    else:
        return None

# Specify the API link to download the data
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Call the function to download and extract the data
extracted_data = download_and_extract_data(api_link)

# Print the extracted data
print("ID:", extracted_data['id'])
print("URL:", extracted_data['url'])
print("Name:", extracted_data['name'])
print("Season:", extracted_data['season'])
print("Number:", extracted_data.get('number'))  # Use get() method to handle missing 'number' attribute
print("Type:", extracted_data['type'])
print("Airdate:", extracted_data['airdate'])
print("Airtime:", extracted_data['airtime'])
print("Runtime:", extracted_data['runtime'])
print("Average Rating:", extracted_data['average_rating'])
print("Summary:", extracted_data['summary'])
print("Medium Image Link:", extracted_data['medium_image'])
print("Original Image Link:", extracted_data['original_image'])
