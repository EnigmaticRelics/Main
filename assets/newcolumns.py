#used to add more columns
import sqlite3

sqlite_file = 'userdb.sqlite'
table_name = 'users'
new_column1 = 'email address'
new_column2 = 'age'
new_column3 = 'password'
new_column4 = 'username'

column_type = 'INTEGER'
column_type2 = 'TEXT'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column4, ct=column_type2))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type2))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column2, ct=column_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column3, ct=column_type2))

conn.commit()
conn.close()
