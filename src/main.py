import csv
import os
import time
from dataclasses import dataclass
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@dataclass
class SiteFormat:
    name: str
    url: str


def get_webdriver() -> Union[ChromeWebDriver, FirefoxWebDriver, None]:
    driver: Union[ChromeWebDriver, FirefoxWebDriver, None] = None

    try:
        driver = webdriver.Firefox(  # type: ignore
            service=FirefoxService(executable_path=GeckoDriverManager().install())
        )
    except Exception as err:
        print(err)

    if not driver:
        try:
            driver = webdriver.Chrome(
                service=ChromeService(executable_path=ChromeDriverManager().install())
            )
        except Exception as err:
            print(err)

    return driver


def main() -> None:
    now = time.strftime("%Y%m%d_%H%M%S")
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(f"{base_path}/src/capture_list.csv") as csv_file:
        valid_sites: list[SiteFormat] = []
        csv_reader = csv.reader(csv_file, delimiter=",")

        for row in csv_reader:
            try:
                name = row[0]
                url = row[1]
                valid_sites.append(SiteFormat(name=name, url=url))
            except Exception as err:
                print(err)

        output_path = f"{base_path}/screenshots/{now}"

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        if len(valid_sites) == 0:
            f = open(f"{output_path}/NO_VALID_SITES", "x")
            f.close()
            return

        driver = get_webdriver()

        if not driver:
            f = open(f"{output_path}/NO_AVAILABLE_BROWSERS", "x")
            f.close()
            return

        driver.maximize_window()

        for site in valid_sites:
            driver.get(site.url)
            time.sleep(1)
            el = driver.find_element(by=By.TAG_NAME, value="html")
            el.screenshot(f"{output_path}/{site.name}.png")

        driver.quit()


if __name__ == "__main__":
    main()
