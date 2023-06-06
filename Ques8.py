import requests
import json
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

def download_and_extract_data(url):
    # Download the data from the API link
    response = requests.get(url)
    data = response.json()

    # Extract the required data attributes for each episode
    episodes = []
    for episode_data in data['_embedded']['episodes']:
        episode_name = episode_data['name']
        season_number = extract_season_number(episode_name)

        summary = BeautifulSoup(episode_data['summary'], 'html.parser').get_text() if episode_data['summary'] else ''

        episode = {
            'id': episode_data['id'],
            'url': episode_data['url'],
            'name': episode_name,
            'season': season_number,
            'number': episode_data.get('number'),
            'type': episode_data['type'],
            'airdate': episode_data.get('airdate'),
            'airtime': episode_data.get('airtime'),
            'runtime': episode_data['runtime'],
            'average_rating': episode_data['rating']['average'],
            'summary': summary,
            'medium_image': episode_data['image']['medium'],
            'original_image': episode_data['image']['original']
        }
        episodes.append(episode)

    return episodes

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

# Get all the overall ratings for each season
season_ratings = {}
for episode in extracted_data:
    season = episode['season']
    rating = episode['average_rating']
    if season not in season_ratings:
        season_ratings[season] = [rating]
    else:
        season_ratings[season].append(rating)

# Compare the ratings for all the seasons using plots
seasons = list(season_ratings.keys())
ratings = [sum(season_ratings[season]) / len(season_ratings[season]) for season in seasons]

#plt.bar(seasons, ratings)
plt.xlabel('Season')
plt.ylabel('Average Rating')
plt.title('Average Ratings for Each Season')
plt.show()

# Get all the episode names whose average rating is more than 8 for every season
high_rated_episodes = []
for episode in extracted_data:
    if episode['average_rating'] > 8:
        high_rated_episodes.append(episode['name'])

print("Episodes with Average Rating > 8:", high_rated_episodes)

# Get all the episode names that aired before May 2019
episodes_before_may_2019 = []
for episode in extracted_data:
    airdate = episode['airdate']
    if airdate and airdate < '2019-05-01':
        episodes_before_may_2019.append(episode['name'])

print("Episodes Aired Before May 2019:", episodes_before_may_2019)

# Get the episode name from each season with the highest and lowest rating
highest_rated_episodes = {}
lowest_rated_episodes = {}

for episode in extracted_data:
    season = episode['season']
    rating = episode['average_rating']
    if season not in highest_rated_episodes or rating > highest_rated_episodes[season]['rating']:
        highest_rated_episodes[season] = {'name': episode['name'], 'rating': rating}
    if season not in lowest_rated_episodes or rating < lowest_rated_episodes[season]['rating']:
        lowest_rated_episodes[season] = {'name': episode['name'], 'rating': rating}

print("Highest Rated Episodes:")
for season, episode_data in highest_rated_episodes.items():
    print("Season", season, ":", episode_data['name'], "(Rating:", episode_data['rating'], ")")

print("Lowest Rated Episodes:")
for season, episode_data in lowest_rated_episodes.items():
    print("Season", season, ":", episode_data['name'], "(Rating:", episode_data['rating'], ")")

# Get the summary for the most popular (ratings) episode in every season
popular_episodes = {}
for episode in extracted_data:
    season = episode['season']
    rating = episode['average_rating']
    if season not in popular_episodes or rating > popular_episodes[season]['rating']:
        popular_episodes[season] = {'name': episode['name'], 'summary': episode['summary'], 'rating': rating}

print("Most Popular Episodes (Summary):")
for season, episode_data in popular_episodes.items():
    print("Season", season, ":", episode_data['name'])
    print("Summary:", episode_data['summary'])
    print("Rating:", episode_data['rating'])
