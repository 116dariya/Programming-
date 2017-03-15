import vk
session = vk.Session(access_token = '0bfb458ccd40fc5fbc12bd95db5b4480fbb3162242b79e8b302e3780c82bdbc7a9bdb355344ecff00e86d')
api = vk.API(session)
l = api.friends.get()
print(l)
r = api.status.set(text = 'Hi')
print(r)