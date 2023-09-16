from src.scraper import Scraper
import sys

print(len(sys.argv))

if len(sys.argv) == 1:
    print("Not enough arguments")
    exit()

url = sys.argv[1]

print(f"Scraping {url}")

s: Scraper = Scraper(url)

s.scrape()