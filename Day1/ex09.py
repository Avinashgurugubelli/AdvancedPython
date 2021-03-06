'''
Module ex09

defines an entity class contact and a repository class contact
'''

class Contact(object):
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__email = kwargs.get('email')
        self.__phone = kwargs.get('phone')
        self.__city = kwargs.get('city', 'Bangalore')
        self.__picture = kwargs.get('picture')

    def __str__(self):
        return 'Contact [ID = {}, Name = {}, Email ={}, Phone ={}, City = {}, Picture = {}]'.format(
            self.__id,
            self.__name,
            self.__email,
            self.__phone,
            self.__city,
            self.__picture
        )

class ContactDao(object):

    def __getCursor(self):
        from sqlite3 import connect
        conn = connect('sample_db.sqlite3')
        cur = conn.cursor()
        return (conn, cur)
    
    def __cleanup(self, conn, cur):
        cur.close()
        conn.close()

    def addContact(self, Contact):
        pass
    
    def getContact(self, id):
        '''
        This method accepts an int id and returns an instance of contact class with the given id, searched and obtained from the database table 'contacts'. if not found, none is returned
        '''
        if id == None or type(id) != int:
            raise ValueError('id is required and must be int ')
        conn, cur = self.__getCursor()
        try:
            cur.execute('select * from contacts where id = ?', (id,))
            data = cur.fetchone()
            if data == None: return None
            return Contact(
                id = data[0],
                name = data[1],
                city = data[2],
                email = data[3],
                phone = data[4],
                picture = data[5]
            )
        finally:
            self.__cleanup(conn, cur)
    
    def updateContact(self, contact):
        pass
    
    def deleteContact(self, id):
        pass
    
    def getAllContact(self):
        pass
    
    def getContatsByCity(self):
        pass

def main():
    dao = ContactDao()
    c1 = dao.getContact(1)
    c2 = dao.addContact(10)
    print (c1)
    print (c2)

if __name__ == "__main__":
    main()