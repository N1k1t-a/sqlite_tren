import sqlite3


def main():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            create_inventory_table = '''CREATE TABLE IF NOT EXISTS Inventory (
                                                    itemID INTEGER PRIMARY KEY NOT NULL,
                                                    ItemName TEXT,
                                                    Price REAL)'''
            cur.execute(create_inventory_table)

            conn.commit()

    except sqlite3.Error as e:
        print(f'ошибка при работе с базами данных {e}')


if __name__ == '__main__':
    main()
