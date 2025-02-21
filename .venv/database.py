import sqlite3


connection = sqlite3.Connection('roots&words.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roots(
id_root INTEGER,
roots_group TEXT PRIMARY KEY,
root TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Words(
id INTEGER PRIMARY KEY,
word TEXT NOT NULL,
id_root TEXT
)
''')

def filling_roots(args):
    s = list
    roots_list = list(args.split(' '))
    id_ = cursor.execute("SELECT id_root FROM Roots;").fetchall()
    new_id_root = max(id_) + 1
    print (new_id_root)
    for i in range(len(roots_list)):
        id_root_group = args
        root = roots_list[i]
        cursor.execute(f'INSERT INTO Roots (id_root_group, id_root, root) VALUES({root_group}, {id_root}, {root});')
    connection.commit()

def filling_words(args):
    word_list = list(args.split(' '))
    id_ = cursor.execute("SELECT id FROM Words;").fetchall()
    new_id = max(id_) + 1
    for i in range(len(word_list)):
        check_word = cursor.execute(f"SELECT COUNT(*) FROM Words WHERE word = {word_list[i]};")
        if check_word > 0:
            print ((f"Word |{word_list[i]}| already exist. Check please manualy or update root special procedure."))
            continue
        else:
            id = id_ + i
            word = word_list[i]
            cursor.execute(f'INSERT INTO Words (id, word) VALUES({id}, {word});')
    connection.commit()

def update_word_and_root(word, root):
    check_word = cursor.execute(f"SELECT COUNT(*) FROM Words WHERE word = {word} and id_root not Null;").fetchall()
    if int(check_word) > 0:
        print ((f"Root for the word |{word}| already exist. Check please manualy"))
    else:
        id_root = id_roots_group
        cursor.execute(f'UPDATE Words SET id_root = {id_root} WHERE id = {id_word};')
    connection.commit()

def word_connect_root(word, root, id_root):
    id_word = cursor.execute(f"SELECT id FROM Words WHERE word = {word};")
#    id_root = cursor.execute(f"SELECT id_root_group FROM Roots WHERE root = {root};")
    cursor.execute(f'UPDATE Words SET id_root = {id_root} WHERE id = {id_word}')
    connection.commit()

# def get_all():
#     s = cursor.execute("SELECT * FROM users;").fetchall()
#     connection.commit()
#     return s
#
# def count():
#     s = cursor.execute("SELECT COUNT(*) FROM users;").fetchone()
#     connection.commit()
#     return s[0]
#
# def get_id():
#     s = cursor.execute("SELECT id FROM users;").fetchall()
#     connection.commit()
#     return s
#
# def check_block(id):
#     s = cursor.execute("SELECT * FROM block; ").fetchall()
#     connection.commit()
#     return (id,) in s
#
# def block(id):
#     cursor.execute(f"INSERT INTO block VALUES({id}); ").fetchall()
#     connection.commit()

def delete_root(id):
    cursor.execute(f"DELETE FROM Root WHERE id_root = {id}; ").fetchall()
    connection.commit()

def delete_word(id):
    cursor.execute(f"DELETE FROM Word WHERE id = {id}; ").fetchall()
    connection.commit()
