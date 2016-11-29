#!/usr/python

import tools
import shodan

class Shodapi:

	def __init__(self):
		api_key = tools.getAPIKey()
		self.api = shodan.Shodan(api_key)	
		
	def search(self, terms):
		results = self.api.search(terms)
		return results
