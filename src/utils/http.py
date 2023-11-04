import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

lg = logging.getLogger(__name__)


def get_session():
    session = requests.Session()
    retry = Retry(total=5, connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    return session


def http_requests(url, method='GET', **kwargs):
    with get_session() as session:
        lg.info(f"Attempt hitting endpoint {url}")
        response = session.request(method, url, **kwargs)
        if response.status_code == requests.codes.ok:
            lg.info(f"received successful response from endpoint {url}")
            return response.json()
        else:
            logging.error(
                f"Failed to RUN request: {url} \n Reason: {response.reason} \n Error code: {response.status_code}")
