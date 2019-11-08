from indeed import IndeedClient
import pymysql
from database import addToDatabase

client = IndeedClient(publisher = ***************)

parameters = {'q' : "python developer",
			  'l' : "India",
			  'sort' : "date",
			  'fromage' : "5",
			  'limit' : "25",
			  'filter' : "1",
			  'userip' : "192.186.176.550:60409",
			  'useragent' : "Mozilla/5.0"
			 }

def get_offers(params):    
	search_results = client.search(**search_params)    
	for elm in search_results['results']:
				
		offer = (elm['jobtitle'], 
				 elm['formattedLocation'], 
				 elm['snippet'], 
				 elm['url'], 
				 elm['indeedApply'], 
				 elm['jobkey'], 
				 elm['date'])
		addToDatabase(offer)

def searchAllCities():
	current_city = 0
	with open('cities', 'r', encoding='utf8') as myfile:
		locations = myfile.read().split('\n')
	city_number = len(locations)
	while current_city < city_number:        
		params['l'] = locations[current_city]
		get_offers(params)
		current_city  += 1