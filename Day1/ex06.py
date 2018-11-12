'''
module ex07
Adding a new record to the table - SQL injection breech
'''
from sqlite3 import connect

def main():
    name = input('enter Name: ')
    email = input('enter Email: ')
    Phone = input('enter Phone: ')

    # sql injection - breech
    cmd = 'insert into contacts (name, email, phone) values (\'{}\', \'{}\' , \'{}\' )'.format(name, email, Phone)
    con = connect('sample_db.sqlite3')
    try:
        c1 = con.cursor()
        c1.execute(cmd)
        con.commit()
        print ('Data Inserted')
    except Exception as ex:
        print('there was a error:- ', ex)
if __name__ == "__main__":
    main()
