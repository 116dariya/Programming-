'''
import requests 
from bs4 import BeautifulSoup

url = "http://kurstenge.kz"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("#content table table tr")[:3]
for tr in rows:
	name = tr.select("td a")[0].text
	rate = float(tr.select("td span.today")[0].text.replace(",", "."))
print("%s\t%f" % (name, rate))
'''
'''
import requests 
from bs4 import BeautifulSoup

url = "https://mig.kz/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.informer table tr")[:5]
for tr in rows:
	rate = tr.select("td")[0].text
	name = tr.select("td")[1].text
	print(name + " " + rate)
	print("\n")
'''
'''
import requests 
from bs4 import BeautifulSoup

url = "http://helios.kz/toplivo/tseny-na-benzin/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
search = soup.select("#petroil-prices li")[0]
petroil = search.select("span.name")[0].text
price = search.select("span.value")[0].text
print(petroil + " - " + price)
'''
import requests 
from bs4 import BeautifulSoup

url = "http://kino.kz/cinema.asp?cinemaid=140&type=2&day=0#top"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
seance = soup.select("table.time_schedule tr.seance_active")[:1]

for tr in seance:
	time  = tr.select("td")[0].text
	name = tr.select("td strong a")[0].text 
	print(time + ' - ' + name)


