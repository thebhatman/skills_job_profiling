from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE_URL = "http://www.indeed.com"
states_URL = "http://www.indeed.com/find-jobs.jsp"
states_URL_list = []
cities_name_list = []

def getStateLinks(states_URL):
	html = urlopen(states_URL).read()
	soup = BeautifulSoup(html, "lxml")
	states_page = soup.find_all(id="states")
	for states in states_page:
		links = states.findAll('a')
		for a in links:
			if a.text != '':
				states_URL_list.append(BASE_URL + a['href'])
	return states_URL_list

def getCityNames():
    states_URL_list = getStateLinks(states_URL)
    for page in states_URL_list:
        html = urlopen(page).read()
        soup = BeautifulSoup(html, "lxml")
        cities_page = soup.find_all('p', attrs={'class':'city'})
        for p in cities_page:
            links = p.findAll('a')
            f = open('cities','a', encoding='utf8')
            for a in links:
                city_state = a['href']
                if city_state[:5] == '/jobs' or '%' in city_state:
                    f.write(a.text + '\n')
                else:
                    city_state = city_state.lstrip('/l-').replace('-', ' ').split(',')
                    city = city_state[0]
                    state_raw= city_state[1]
                    state = ''
    
                    for char in state_raw:
                        if char.isupper():
                            state += char
                    location = city + ', ' + state
                    f.write(location + '\n')
    f.close()