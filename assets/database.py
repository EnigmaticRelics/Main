#This will by the python script that creates tables and inserts data into sqlite database

import sqlite3

sqlite_file = 'userdb.sqlite'
table_name1 = 'users'
new_field = 'primary_key'
field_type = 'INTEGER'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

conn.commit()
conn.close()
