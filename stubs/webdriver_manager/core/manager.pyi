from _typeshed import Incomplete
from webdriver_manager.core.download_manager import WDMDownloadManager as WDMDownloadManager
from webdriver_manager.core.driver_cache import DriverCache as DriverCache
from webdriver_manager.core.logger import log as log

class DriverManager:
    driver_cache: Incomplete
    def __init__(self, root_dir: Incomplete | None = ..., cache_valid_range: int = ..., download_manager: Incomplete | None = ...) -> None: ...
    @property
    def http_client(self): ...
    def install(self) -> str: ...
