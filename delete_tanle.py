import sqlite3


def drop():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            drop_table = 'DROP TABLE IF EXISTS Inventory'
            cur.execute(drop_table)

            conn.commit()

    except sqlite3.Error as e:
        print(f'ошибка при работе с базами данных {e}')


if __name__ == '__main__':
    drop()
