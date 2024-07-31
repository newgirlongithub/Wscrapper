import requests
from bs4 import BeautifulSoup

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

''' Example usage
url = 'https://example.com'
output_file = 'scraped_content.txt'

print("Scraping the website...")
scraped_data = scrape_website(url)
if scraped_data:
    save_to_file(output_file, scraped_data)
    print(f"Scraped data has been saved to {output_file}")
else:
    print("No data scraped.")'''
