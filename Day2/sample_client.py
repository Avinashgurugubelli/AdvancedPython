'''
Module sample_client

using 'request' to consume rest api
'''

import requests

def get_contact(contact_id):
    
    url = 'http://127.0.0.1:1234/api/contacts/{}'.format(contact_id)
    resp = requests.get(url)
    print(resp.text)
    c1 = resp.json()

    if c1==None: 
        print('No data found for id', contact_id)
    else:
        print('Name     =', c1['name'])
        print('Email    =', c1['email'])
        print('Phone    =', c1['phone'])
        print('City     =', c1['city'])

def add_contact():
    c1 = {}
    c1['name'] = input('Enter name: ')
    c1['city'] = input('Enter city: ')
    c1['email'] = input('Enter email: ')
    c1['phone'] = input('Enter phone: ')
    c1['picture'] = None

    url = 'http://127.0.0.1:1234/api/contacts'
    resp = requests.post(url, json=c1)
    print(resp.json())

def main():
    contact_id = input('Enter id: ')
    get_contact(contact_id)

if __name__ == '__main__':
    add_contact()
    # main()