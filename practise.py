import sqlite3


# db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Maru', 'scottish fold', 3)")
# db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Hana', 'tortoiseshell', 1)")

class Cat:

    all = []

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_all(self)

    @classmethod
    def add_cat_to_all(cls, cat):
        cls.all.append(cat)

    def save(self, cursor):
        cursor.execute(
            'INSERT INTO cats (name, breed, age) VALUES (?, ?, ?)', (self.name, self.breed, self.age)
        )

db_connection = sqlite3.connect('pets.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE IF NOT EXISTS cats (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS owners(id INTEGER PRIMARY KEY, name TEXT)")

Cat("Maru", "scottish fold", 3)
Cat("Hana", "tortoiseshell", 1)

for cat in Cat.all:
    cat.save(db_cursor)