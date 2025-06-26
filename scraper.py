# scraper.py

import os
import requests
from bs4 import BeautifulSoup

def save_text_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

def scrape_wikipedia_page(title, save_dir):
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve: {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = '\n'.join([para.get_text() for para in paragraphs])
    save_text_to_file(content, save_dir, f"{title.replace(' ', '_')}.txt")
    print(f"Saved: {title}")

def scrape_drdo_page(url, filename, save_dir):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs])
        save_text_to_file(content, save_dir, filename)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def run_scraper():
    # Wikipedia scraping
    wikipedia_titles = [
        "Defence_Research_and_Development_Organisation",
        "Sonar",
        "Missile",
        "Semiconductor",
        "Rock (geology)"
    ]
    for title in wikipedia_titles:
        scrape_wikipedia_page(title, "data/wikipedia_docs")

    # DRDO scraping (static)
    drdo_pages = {
        "drdo_overview.txt": "https://www.drdo.gov.in/about-drdo",
        "sspl_lab.txt": "https://www.drdo.gov.in/labs-and-establishments/solid-state-physics-laboratory-sspl"
    }
    for filename, url in drdo_pages.items():
        scrape_drdo_page(url, filename, "data/drdo_docs")

if __name__ == "__main__":
    run_scraper()
