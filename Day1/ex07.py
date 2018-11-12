'''
module ex07
Adding a new record to the table with out sql injection
'''
from sqlite3 import connect

def main():
    name = input('enter Name: ')
    email = input('enter Email: ')
    Phone = input('enter Phone: ')

    # Proper way of doing no SQL injection
    cmd = 'insert into contacts (name, email, phone) values (?,?,?)'
    con = connect('sample_db.sqlite3')
    try:
        c1 = con.cursor()
        c1.execute(cmd, (name, email, Phone))
        con.commit()
        print ('Data Inserted')
    except Exception as ex:
        print('there was a error:- ', ex)
if __name__ == "__main__":
    main()
