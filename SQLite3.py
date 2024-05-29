import sqlite3


conn = sqlite3.connect('expenses.db')
c = conn.cursor()


c.execute('''
CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')



def add_expense():
    date = input("Enter date :")
    category = input("Enter category :")
    amount = input("Enter amount :")
    description = input("Enter description :")
    c.execute('INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)',(date, category, amount, description))
    conn.commit()
    print("add successfully")


def view_expenses():
    c.execute('SELECT * FROM Expenses')
    expenses = c.fetchall()
    for expense in expenses:
        print(expense)



def update_expense(id):
    date = input("Enter date :")
    category = input("Enter category :")
    amount = input("Enter amount :")
    description = input("Enter description :")
    c.execute('''
    UPDATE Expenses
    SET date = ?, category = ?, amount = ?, description = ?
    WHERE id = ?
    ''', (date, category, amount, description, id))
    conn.commit()
    print("update successfully")



def delete_expense(id):
    c.execute('DELETE FROM Expenses WHERE id = ?', (id))
    conn.commit()
    print("Delete successfully")


while True:
    x = int(input(
        "Select one of 4 options\n1 = Add expenses\n2 = View Charge\n3 = Update Charge\n4 = Delete_expense\n5 = Exit\nchoose: "))
    if x == 1:
        add_expense()
    elif x == 2:
        view_expenses()
    elif x == 3:
        update_expense(e := input("id :"))
    elif x == 4:
        delete_expense(q := input("id :"))
    elif x == 5:
        break
    else:
        continue

conn.close()
