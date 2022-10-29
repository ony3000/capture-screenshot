import csv
import os
import re
import sys
import time
from dataclasses import dataclass
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class SiteFormat:
    name: str
    url: str


def get_webdriver() -> Union[ChromeWebDriver, None]:
    driver: Union[ChromeWebDriver, None] = None

    try:
        options = ChromeOptions()
        options.headless = True

        driver = webdriver.Chrome(
            service=ChromeService(executable_path=ChromeDriverManager().install()),
            options=options,
        )
    except Exception as err:
        print(err)

    return driver


def main() -> None:
    MIN_WIDTH = 320
    DEFAULT_WIDTH = 1920
    DEFAULT_HEIGHT = 1080

    now = time.strftime("%Y%m%d_%H%M%S")
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for arg in sys.argv[1:]:
        result = re.match(r"^--width=([0-9]+)$", arg)

        if result:
            parsed_width = int(result[1])

            if parsed_width >= MIN_WIDTH:
                DEFAULT_WIDTH = parsed_width

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
            f = open(f"{output_path}/CHROME_BROWSER_REQUIRED", "x")
            f.close()
            return

        for site in valid_sites:
            driver.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
            driver.get(site.url)
            time.sleep(1)

            site_height = driver.execute_script(  # type: ignore
                "return document.body.parentNode.scrollHeight"
            )
            assert type(site_height) is int

            driver.set_window_size(DEFAULT_WIDTH, site_height)
            driver.find_element(by=By.TAG_NAME, value="html").screenshot(
                f"{output_path}/{site.name}.png"
            )

        driver.quit()


if __name__ == "__main__":
    main()
