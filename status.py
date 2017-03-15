import requests 
token = '0bfb458ccd40fc5fbc12bd95db5b4480fbb3162242b79e8b302e3780c82bdbc7a9bdb355344ecff00e86d'
url = 'http://www.vktops.com/statusy-o-zhenshchinakh/'
r = requests.get(url)
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('.statusesList .statusesList-item div.text')[0].text
#print(a)
url = 'https://api.vk.com/method/status.set?text=%s&v=5.52&access_token=0bfb458ccd40fc5fbc12bd95db5b4480fbb3162242b79e8b302e3780c82bdbc7a9bdb355344ecff00e86d' %a
r = requests.get(url)
print(r.json())