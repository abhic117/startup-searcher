from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

BASE_URL = 'https://www.techsydney.com.au'
STARTUPS_URL = 'https://www.techsydney.com.au/startups'

def scrape_techsydney():
    raw_startups = []

    with sync_playwright() as pw:
        # Opens a browser
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigates to specified url
        page.goto(STARTUPS_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        # Finds all links on startups page
        links = page.locator('a')
        profiles = []

        while True:
            # Loop through all loaded links
            for i in range(links.count()):

                # Get each individual link and href
                link = links.nth(i)
                href = link.get_attribute('href')

                # If its a link to a startup, add it to the list
                if href and '/s/' in href:
                    profile_url = urljoin(BASE_URL, href)

                    if profile_url not in profiles:
                        profiles.append(profile_url)

            next_button = page.get_by_role("link", name="Next", exact=True)

            if next_button.count() == 0:
                break

            if not next_button.first.is_enabled():
                break

            next_button.first.click()
            page.wait_for_timeout(800)

        print(f"There are {len(profiles)} properties")

        for index, url in enumerate(profiles):
            print(f"Scraping {index} of {len(profiles)}")
            startup_text = ''
            page.goto(url, wait_until='domcontentloaded')
            
            page.wait_for_timeout(2000)

            startup_info = page.locator('div.p-3')
            startup_overview = page.locator('div.small.mb-3.row')
            startup_description = page.locator("div.readonly")

            try:
                startup_link = page.get_by_role("link", name="Website")
                if startup_link.count() > 0:
                    href = startup_link.get_attribute("href")
                else:
                    continue
            except Exception:
                startup_link = '-'

            for a in range(startup_info.count()):
                line = startup_info.nth(a)
                startup_text += line.inner_text()
                
            for b in range(startup_overview.count()):
                line = startup_overview.nth(b)
                startup_text += '\n'
                startup_text += line.inner_text()

            startup_text += '\n'
            if startup_description.count() > 0:
                startup_text += startup_description.inner_text()
            else:
                startup_text += '-'
            startup_text += '\n'
            startup_text += href

            raw_startups.append(startup_text)

        # Close browser
        browser.close()
    return raw_startups
