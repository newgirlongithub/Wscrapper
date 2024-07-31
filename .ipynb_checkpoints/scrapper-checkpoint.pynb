import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.theminiadhdcoach.es/'
output_file = 'scraped_content.txt'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all paragraph tags and print their text
    for paragraph in soup.find_all('p'):
        print(paragraph.get_text())
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        return paragraphs
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')
        return []

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line + '\n')