import os
import sqlite3

import bcrypt


def init(path, randomize, file_challenge_name=None):

    db = os.path.join(os.path.sep, "tmp", "race_condition.db")
    context_db = db

    if file_challenge_name:
        context_db = os.path.join(path, "race_condition.db")
        file_challenge_path = os.path.join(path, file_challenge_name)
        with open(file_challenge_path, "r") as chall:
            file_chall_content = chall.read()
            new_file_chall_content = file_chall_content.replace(db, context_db)
        with open(file_challenge_path, "w") as chall:
            chall.write(new_file_chall_content)

    need_chmod = False
    if db == context_db:
        need_chmod = True

    conn = sqlite3.connect(context_db)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP TABLE IF EXISTS forbidden_ids")
    conn.commit()
    cur.execute("""CREATE TABLE users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		login TEXT NOT NULL UNIQUE,
		password TEXT NOT NULL)""")

    cur.execute("""CREATE TABLE forbidden_ids (user_id INTEGER NOT NULL UNIQUE)""")
    conn.commit()

    hashed_randomize = bcrypt.hashpw(randomize.encode("utf-8"), bcrypt.gensalt(8)).decode('utf-8')
    hashed_randomize = hashed_randomize.replace("$2b$", "$2a$")
    cur.execute("INSERT INTO users(login, password) VALUES(?, ?)", [randomize, hashed_randomize])

    conn.commit()
    conn.close()

    if need_chmod:
        os.system('chown race_condition:race_condition ' + context_db)
        os.system('chmod 640 ' + context_db)

    with open(os.path.join(path, 'secret'), "w") as secret:
        secret.write(randomize)
