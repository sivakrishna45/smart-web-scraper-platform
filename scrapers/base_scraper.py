import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

from scrapers.utils.playwright_helper import PlaywrightHelper


class BaseScraper:

    def __init__(self):

        self.logger = logging.getLogger(
            self.__class__.__name__
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2)
    )
    def fetch(self, url, dynamic=False):

        self.logger.info(f"Fetching: {url}")

        if dynamic:

            return PlaywrightHelper.fetch(url)

        response = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/122.0 Safari/537.36"
                )
            },
            timeout=30
        )

        response.raise_for_status()

        return response.text

    def parse(self, html):

        return BeautifulSoup(
            html,
            "lxml"
        )