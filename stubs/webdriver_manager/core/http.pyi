import requests
from _typeshed import Incomplete
from requests import Response as Response
from webdriver_manager.core.config import ssl_verify as ssl_verify, wdm_progress_bar as wdm_progress_bar
from webdriver_manager.core.utils import show_download_progress as show_download_progress

class HttpClient:
    def get(self, url, params: Incomplete | None = ..., **kwargs) -> Response: ...
    @staticmethod
    def validate_response(resp: requests.Response): ...

class WDMHttpClient(HttpClient):
    def __init__(self) -> None: ...
    def get(self, url, **kwargs) -> Response: ...
