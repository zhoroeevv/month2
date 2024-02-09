import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

def create_car(conn, car: tuple):
    sql = """ INSERT INTO cars_list
    (car_title, price, quanity)
    VALUES (?,?,?);"""
    cursor = conn.cursor()
    cursor.execute(sql, car)
    conn.commit()

def delete_car(conn, id: int):
    sql = "DELETE FROM cars_list WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()


def get_cheap_cars():
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars_list WHERE price < 100")
    cheap_cars = cursor.fetchall()
    if cheap_cars:
        print("Машины с ценой менее 100 долларов:")
        for car in cheap_cars:
            print(f"ID: {car[0]}, Название: {car[1]}, Цена: {car[2]}, Количество: {car[3]}")
    else:
        print("Машин с ценой менее 100 долларов не найдено.")

    conn.close()


sql_create_table = """
CREATE TABLE IF NOT EXISTS cars_list (
id INTEGER PRIMARY KEY AUTOINCREMENT,
car_title VARCHAR(100) NOT NULL,
price REAL DEFAULT 0.0,
quanity INTEGER DEFAULT 0 NOT NULL);
"""

connection = create_connection("cars.db")

if connection:
    print("Успешное соединение")
    create_table(connection, sql_create_table)
    create_car(connection, ('Toyota', 15000, 5))
    create_car(connection, ('Honda', 9500, 3))
    create_car(connection, ('Ford', 8500, 2))
    create_car(connection, ('BMW', 20000, 1))
    create_car(connection, ('Lexus', 9900, 4))
    create_car(connection, ('Lexus', 99, 4))
    create_car(connection, ('Mers', 20000000, 43))
    delete_car(connection, 1)

get_cheap_cars()
