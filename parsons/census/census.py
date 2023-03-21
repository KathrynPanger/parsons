import logging
import urllib
from parsons.utilities.api_connector import APIConnector
from parsons.utilities import check_env
from parsons import Table
from parsons.census.helper import Helper

logger = logging.getLogger(__name__)

URI = "https://api.census.gov/data/"

class Census(object):
	"""
	Instantiate Connector class.

   	`Args:`
	"""

	def __init__(self, api_key=None, uri=None, dataset=None):
		
		self.api_key = check_env.check('CONNECTOR_API_KEY', api_key)
		self.uri = check_env.check('CENSUS_URI', uri, optional = True) or URI
		self.client = APIConnector(self.uri)

		
	def get_acs_1_year(self, year):
		# api.census.gov/data/2021/acs/acs1?get=NAME,group(B01001)&for=us:1&key=YOUR_KEY_GOES_HERE
		full_url = urllib.parse.urljoin(self.uri, f"{str(year)}/acs/acs1")
		results = self.client.get_request(full_url, params = {"get": "NAME,group(B01001)", "for" : "us:1", "key": self.api_key})
		results_dict = {}
		for i in range(len(results[0])):
			results_dict[results[0][i]] = Helper.cast_to_type(results[1][i])
		print(results_dict)
		return results_dict