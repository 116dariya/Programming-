'''import vk
session = vk.Session(access_token = '2ec49de8d9ac96189ac8611d48f0d14fbeed668fedfb1124a0338b4687ad9ebbbcdb5f1bed7ce836670d5')
api = vk.API(session)
l = api.friends.get()
print(l)
r = messages.send()
print(r)

import vk
session = vk.Session()
api = vk.API(session)
print(api.users.get(user_ids="idmmm7777"))


https://oauth.vk.com/blank.html#access_token=2ec49de8d9ac96189ac8611d48f0d14fbeed668fedfb1124a0338b4687ad9ebbbcdb5f1bed7ce836670d5&expires_in=86400&user_id=162765493
'''
import vk
session = vk.Session(access_token = '2ec49de8d9ac96189ac8611d48f0d14fbeed668fedfb1124a0338b4687ad9ebbbcdb5f1bed7ce836670d5')
api = vk.API(session)
r = api.status.get()
print(r)
'''
f = api.messages.get()
print(f)
'''
