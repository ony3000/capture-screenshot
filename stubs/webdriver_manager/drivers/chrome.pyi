from webdriver_manager.core.driver import Driver as Driver
from webdriver_manager.core.logger import log as log
from webdriver_manager.core.utils import ChromeType as ChromeType, is_arch as is_arch, is_mac_os as is_mac_os

class ChromeDriver(Driver):
    def __init__(self, name, version, os_type, url, latest_release_url, http_client, chrome_type=...) -> None: ...
    def get_os_type(self): ...
    def get_url(self): ...
    def get_browser_type(self): ...
    def get_latest_release_version(self): ...