import sqlite3
import json
import uuid # uuid используется для генерации случайного числа
import hashlib
conn = sqlite3.connect('users2.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS visitors(
   login PRIMARY KEY,
   password TEXT);
""")
conn.commit()

user_login = input('Login : ')
user_password = input('Password : ')

salt = uuid.uuid4().hex
user_password = hashlib.sha256(salt.encode() + user_password.encode()).hexdigest() + '$' + salt

cur.execute("SELECT login FROM visitors")
cur.execute(f"INSERT INTO visitors VALUES(?,?)",(user_login,user_password))
conn.commit()
    
cur.execute("SELECT * FROM visitors;")

all_results2 = cur.fetchall()
print(all_results2)

to_json = ("Вся строка: ",all_results2)

with open('sw_templates2.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates2.json') as f:
    print(f.read())

