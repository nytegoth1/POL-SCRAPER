import requests
from bs4 import BeautifulSoup
import json

def scrape_site(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all li elements with the class name 'o-listicle__item'
    sections = soup.find_all('li', class_='o-listicle__item')

    # Extract information from each section
    data = []
    for section in sections:
        section_info = {}
        # Extract text content
        section_info['text'] = section.get_text(strip=True)
        # Extract img src if present
        img = section.find('img')
        if img and img.get('src'):
            section_info['img_src'] = img['src']
        data.append(section_info)

    return data

def write_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    url = 'https://www.politifact.com/personalities/donald-trump'  # Replace with the URL you want to scrape
    scraped_data = scrape_site(url)
    write_to_json(scraped_data, 'scrapeit.json')
    print(f"Data has been written to scrapeit.json")