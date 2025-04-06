import unittest
from unittest.mock import patch
from exammidterm.scraper import OpenLibraryScraper


class TestScraper(unittest.TestCase):

    @patch("exammidterm.scraper.requests.Session.get")
    def test_robots_txt_allows_scraping(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "User-agent: *\nDisallow: /restricted"

        scraper = OpenLibraryScraper()
        result = scraper.is_allowed_by_robots("/people/someuser")
        self.assertTrue(result)

    @patch("exammidterm.scraper.requests.Session.get")
    def test_robots_txt_disallows_scraping(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "User-agent: *\nDisallow: /telanoma"

        scraper = OpenLibraryScraper()
        result = scraper.is_allowed_by_robots("/telanoma/testigo")
        self.assertFalse(result)
