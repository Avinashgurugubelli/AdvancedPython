'''
A flask rest endpoint application
'''
from contacts_dao import ContactsDao, Contact
from flask import Flask, request, Response
import json

app = Flask(__name__)

custom_headers = {}
custom_headers['content-type'] = 'application/json'

@app.route('/')
def info():
    return 'this is a flask endpoint'

@app.route('/api/contacts')
def all_contacts():
    dao = ContactsDao()
    c1 = dao.getAllContacts()
    output = json.dumps(dao.getAllContacts(), default=lambda c: c.__dict__)
    return Response(output, headers = custom_headers)

@app.route('/api/contacts/<contact_id>', methods =['GET'])
def get_contact_by_id(contact_id):
    dao = ContactsDao()
    contact_id = int(contact_id)
    c1 = dao.getContact(contact_id)
    output = json.dumps(None) if c1==None else c1.as_json
    return Response(output, headers=custom_headers)

@app.route('/api/contacts/<contact_id>', methods =['DELETE'])
def delete_contact(contact_id):
    dao = ContactsDao()
    contact_id = int(contact_id)
    c1 = dao.deleteContact(contact_id)
    # ideally delete request should return th deleted state from the resource, in this case we are sending the remaining contacts
    return all_contacts();

@app.route('/api/contacts', methods =['POST'])
def add_contact():
    payload = request.data
    c1 = Contact()
    c1.as_json = payload
    dao = ContactsDao()
    c1 = dao.addContact(c1)
    return c1.as_json

@app.route('/api/contacts/<contact_id>', methods =['PUT'])
def update_contact(contact_id):
    c1 = Contact()
    c1.as_json = request.data
    c1.id = contact_id
    dao = ContactsDao()
    c1 = dao.updateContact(c1)
    return Response(c1.as_json, headers=custom_headers)

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=1234)