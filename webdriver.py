from selenium import webdriver
from pathlib import Path
import pickle
import time


def browser_session():
    browser = webdriver.Chrome()
    browser.get("https://www.draftkings.co.uk")
    cookies_path = Path("cookies.pkl")
    if cookies_path.is_file():
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
    else:
        input('Press enter to continue: ')
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

    browser_executor_url = browser.command_executor._url
    browser_session_id = browser.session_id

    while browser.toString().contains(browser_session_id):
        time.sleep(10)

if __name__ == "__main__":
    browser_session()
