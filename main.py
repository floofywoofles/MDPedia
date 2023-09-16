from src.scraper import Scraper

s: Scraper = Scraper("https://en.wikipedia.org/wiki/Abraham_Lincoln")

s.scrape()