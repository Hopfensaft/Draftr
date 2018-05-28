from bs4 import BeautifulSoup
from selenium import webdriver as wd
import json
import datetime
import webdriver
import time


def scraping():

    if not webdriver.browser_session_id:
        webdriver.browser_session()
        time.sleep(3)

    browser = wd.Remote(command_executor=webdriver.browser_executor_url, desired_capabilities={})
    browser.session_id = webdriver.browser_session_id

    input('Press enter to continue: ')
    soup = BeautifulSoup(browser.page_source, "html5lib")
    soup = soup.find("div", class_="draft-container")

    with open("full_scrape.txt", "w") as file:
        file.write(soup.get_text())

    data = {"collection_timestamp": str(datetime.datetime.utcnow()),
            "title": soup.find("h3", class_="ContestInformation_contest-name"),
            "entry_fee": soup.find("li", class_="ContestInformation_entry-fee")}
    print(soup.find("h3", class_="ContestInformation_contest-name"))
    print(soup.find("li", class_="ContestInformation_entry-fee"))

    with open("scrape.txt", "w") as file:
        json.dump(data, file, ensure_ascii=False)

    return soup

if __name__ == "__main__":
    print(scraping())
