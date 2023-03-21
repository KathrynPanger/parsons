import unittest
import requests_mock
import json
import urllib

from parsons.census.census import Census

def escape_url_args(url):
    '''Escape URL arguments so that requests_mock matches the URL'''
    data = urllib.parse.urlsplit(url)
    data = data._replace(query = urllib.parse.urlencode(urllib.parse.parse_qsl(data.query)))
    print(urllib.parse.urlunsplit(data))
    return urllib.parse.urlunsplit(data)

class TestCensus(unittest.TestCase):

    def setUp(self):
        self.api_key = "api_key"
        self.census = Census(api_key = self.api_key)
        self.fake_1_year_data = [["NAME","B01001_001E","B01001_001EA","B01001_001M","B01001_001MA"], ["United States", "331893745", None, "-555555555","*****"]]
        self.expected_1_year_data = {"NAME":"United States", "B01001_001E": 331893745, "B01001_001EA": None, "B01001_001M": -555555555, "B01001_001MA": "*****"}

    @requests_mock.Mocker()
    def test_get_acs_1_year(self, mocker):
        mocker.get(escape_url_args(f"https://api.census.gov/data/2021/acs/acs1?get=NAME,group(B01001)&for=us:1&key={self.api_key}"), text=json.dumps(self.fake_1_year_data))
        self.assertEqual(self.census.get_acs_1_year(year = 2021), self.expected_1_year_data)
