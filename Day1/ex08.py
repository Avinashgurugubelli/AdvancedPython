'''
module ex08

Retriveing data from DB Table
'''

from sqlite3 import connect

def main():
    email = input('Enter email for searching: ')
    cmd = 'select * from contacts where email = ?'
    conn = connect('sample_db.sqlite3')
    cur = conn.cursor()
    cur.execute(cmd, (email,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    print ('data contains {} values'.format(len(data)))
    print ('type of data {}' .format(type(data)))
    print (data)

def fetchRecords():
    conn = connect('sample_db.sqlite3')
    cmd = 'select * from contacts'
    cur = conn.cursor()
    cur.execute(cmd)
    data = cur.fetchall()
    for rec in data:
        print(rec)
if __name__ == "__main__":
    # main()
    fetchRecords()