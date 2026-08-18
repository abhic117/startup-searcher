from src.techsydney_scraper import scrape_techsydney
from src.parser import parse_techsydney
from src.database import insert_startup

raw_startups = scrape_techsydney()

for startup in raw_startups:
    parsed_startup = parse_techsydney(startup)
    insert_startup(parsed_startup)