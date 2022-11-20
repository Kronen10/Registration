import sqlite3
import json
conn = sqlite3.connect('users2.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users2(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   login TEXT,
   comment TEXT);
""")
conn.commit()

user_id = None
user_login = input('Login : ')
user_comment = input('Comment : ')


cur.execute("SELECT id FROM users2 WHERE id = '{user_id}'")
if cur.fetchone() is None:
    cur.execute(f"INSERT INTO users2 VALUES(?,?,?)",(user_id,user_login,user_comment))
    conn.commit()
    print("Запись добавлена")
else:
    print("Такая запись уже имеется")


    for value in cursor.execute("SELECT * FROM users2"):
        print(value)

cur.execute("SELECT * FROM users2;")
all_results = cur.fetchall()
print(all_results)

to_json = ("Вся строка: ",all_results)

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates.json') as f:
    print(f.read())
