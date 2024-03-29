from _typeshed import Incomplete
from webdriver_manager.core.driver import Driver as Driver
from webdriver_manager.core.logger import log as log

class OperaDriver(Driver):
    opera_release_tag: Incomplete
    def __init__(self, name, version, os_type, url, latest_release_url, opera_release_tag, http_client) -> None: ...
    def get_latest_release_version(self) -> str: ...
    def get_url(self) -> str: ...
    @property
    def latest_release_url(self): ...
    def tagged_release_url(self, version): ...
    def get_browser_type(self): ...
    def get_browser_version(self): ...
