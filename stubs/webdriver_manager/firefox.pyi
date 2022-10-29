from _typeshed import Incomplete
from typing import Optional
from webdriver_manager.core.download_manager import DownloadManager as DownloadManager
from webdriver_manager.core.manager import DriverManager as DriverManager
from webdriver_manager.drivers.firefox import GeckoDriver as GeckoDriver

class GeckoDriverManager(DriverManager):
    driver: Incomplete
    def __init__(self, version: Optional[str] = ..., os_type: Optional[str] = ..., path: Optional[str] = ..., name: str = ..., url: str = ..., latest_release_url: str = ..., mozila_release_tag: str = ..., cache_valid_range: int = ..., download_manager: Optional[DownloadManager] = ...) -> None: ...
    def install(self) -> str: ...
