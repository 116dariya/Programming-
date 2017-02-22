import requests
'''url = "https://api.vk.com/method/users.get?user_ids=pshnpdrs666"
response = requests.get(url)
data = response.json()
print(data['response'][0]['uid'])
print(data['response'][0])

'''
url = "https://api.vk.com/method/users.get?user_ids=pshnpdrs666&fields=last_seen,status"
response = requests.get(url)
data = response.json()
'''
print(data['response'][0]['status'])
print(data['response'][0]['occupation']['name'])
'''
uid = data['response'][0]['uid']
url = 'https://api.vk.com/method/wall.get?owner_id=%d' %uid
print(url)
response = requests.get(url)
data = response.json()
posts = data['response'][1]
post_count= data['response'][0]
print(posts)
