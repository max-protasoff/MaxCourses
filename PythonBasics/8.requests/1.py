import requests
import json

# Ignore SSL certificate errors???? Почему-то работает и без него, почему?
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

# ENTER YOUR API KEY HERE !!!!!!!!!! IT SHOULD BE API KEY EXACTLY FOR YOUR VK ID!!!!
api_key = ''


#url = 'https://api.vk.com/method/friends.getMutual'
#your_id = int(input('Enter your ID: '))
#check_id = input("Enter friend's VK ID: ")
#params = {'v':'5.52', 'target_uid': check_id, 'access_token': api_key}
#response = requests.get(url, params=params)


class User:
    def __init__(self, id):
        self.id = id
        r = requests.get('https://api.vk.com/method/users.get', params={'user_id':self.id, 'v': '5.52', 'access_token': api_key})
        user_json = json.loads(r.text)
        self.first_name = user_json['response'][0]['first_name']
        self.last_name = user_json['response'][0]['last_name']
        self.link = 'vk.com/id' + str(self.id)

    def __str__(self):
        return f'Name is {self.first_name}, last name is {self.last_name}, link is {self.link}'

    def __and__(self, other):
        url = 'https://api.vk.com/method/friends.getMutual'
        your_id = self.id
        check_id = other.id
        params = {'v':'5.52', 'target_uid': check_id, 'access_token': api_key}
        response = requests.get(url, params=params)
        json_file = json.loads(response.text)

        ids = json_file['response']

        objs = list()
        for i in ids:
            objs.append(User(i))

        print('Your mutual friends are:')
        for i in objs:
            print(i)

your_vkid = int(input('Enter your VK ID: '))
you = User(your_vkid)

fr_vkid = int(input("Enter your friend's VK ID: "))
friend = User(fr_vkid)

you & friend
