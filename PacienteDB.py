import sqlite3


conn = sqlite3.connect('exemplo.db')


cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   idade INTEGER)''')


cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('João', 25))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Maria', 30))


conn.commit()


conn.close()