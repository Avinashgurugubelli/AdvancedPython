'''
module ex05

creating a database table
'''

from sqlite3 import connect

def main():
    cmd = '''create table contacts (
        id integer primary key autoincrement,
        name varchar(50) not null,
        city varchar (50) default 'Bangalore',
        email varchar(50) unique,
        phone varchar(50) unique,
        picture varchar(555)
    )
    '''
    conn = connect('sample_db.sqlite3')
    c1 = conn.cursor()
    try:
        c1.execute(cmd)
        print ('table created')
    except Exception as ex:
        print ('error occurred while creating table')
        print (ex)
    conn.close()
if __name__ == "__main__":
    main()