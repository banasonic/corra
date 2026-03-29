import requests
from bs4 import BeautifulSoup
import json

def scrape_kooora_matches(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')
    next_data_script = soup.find('script', id='__NEXT_DATA__')

    if not next_data_script:
        return "__NEXT_DATA__ script tag not found."

    try:
        json_data = json.loads(next_data_script.string)
        competitions_data = json_data['props']['pageProps']['data']['scoreboard']['competitions']
    except (json.JSONDecodeError, KeyError) as e:
        return f"Error parsing JSON or navigating data structure: {e}"

    matches_list = []
    for competition in competitions_data:
        competition_name = competition['competition']['name']
        for match in competition['matches']:
            match_info = {
                'competition': competition_name,
                'round': match['round']['name'] if 'round' in match and match['round'] else 'N/A',
                'status': match['status'],
                'start_date': match['startDate'],
                'team_a': match['teamA']['name'] if 'teamA' in match and match['teamA'] else 'N/A',
                'team_b': match['teamB']['name'] if 'teamB' in match and match['teamB'] else 'N/A',
                'score_a': match['score']['teamA'] if 'score' in match and match['score'] else 'N/A',
                'score_b': match['score']['teamB'] if 'score' in match and match['score'] else 'N/A',
            }
            matches_list.append(match_info)

    return matches_list

if __name__ == '__main__':
    kooora_url = "https://www.kooora.com/%D8%A3%D8%AD%D8%AF%D8%A7%D8%AB-%D8%B1%D9%8A%D8%A7%D8%B6%D9%8A%D8%A9/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85"
    matches = scrape_kooora_matches(kooora_url)
    if isinstance(matches, str):
        print(matches)
    else:
        print(json.dumps(matches, indent=2, ensure_ascii=False))
