import pytest

from kfailb import Scraper
from requests.exceptions import ConnectionError


class TestScraper:
    def test_fetch_website_error(self):
        urls = ["http://localhost:54345/1"]
        scraper = Scraper(urls=urls)
        with pytest.raises(ConnectionError):
            content = scraper.fetch_website()

    def test_fetch_website(self):
        urls = ["http://localhost:8080/itworks"]
        scraper = Scraper(urls=urls)
        content = scraper.fetch_website()

        assert content == b"horrayitworks"

    def test_fetch_website_retries(self):
        urls = ["http://localhost:8080/retries"]
        scraper = Scraper(urls=urls)
        content = scraper.fetch_website()

        assert content == b"horray"
