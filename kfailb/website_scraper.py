"""
This module contains a scraper that fetches the webpage content.
"""

import random
import requests
import backoff

from requests import RequestException
from urllib3.exceptions import MaxRetryError


def _is_fatal_code(e):
    """
    Determines whether the backoff annotation should stop
    trying the request immediately.
    :param e: thrown exception
    :return: True, when backoff should stop immediately,
    otherwise False.
    """
    if isinstance(e.args[0], MaxRetryError):
        return False

    try:
        return 400 <= e.args[0] < 500
    except (AttributeError, TypeError):
        return True


class Scraper:
    """
    Fetches and website data content.
    """
    def __init__(self, urls, user_agents=None):
        if not urls:
            raise ValueError("No URLs defined")

        self._urls = urls
        self._user_agents = user_agents

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.RequestException,
                          max_time=10,
                          giveup=_is_fatal_code)
    def fetch_website(self):
        """
        Fetches the raw content of the website and returns it.
        :return: The content of the requested webpage.
        """
        url = random.choice(self._urls)
        headers = dict()

        if self._user_agents:
            headers['User-Agent'] = random.choice(self._user_agents)

        page = requests.get(url, headers=headers)
        if page.status_code >= 300:
            raise RequestException(page.status_code)

        return page.content
