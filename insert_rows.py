import sqlite3


def main():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            again = input('а надо ли тебе вообще еще данные водить? (д/н)')

            while again.lower() == 'д':
                item_name = input('введите название инструмента')
                price = float(input('введите цену инструмента'))

                cur.execute('''INSERT INTO Inventory (ItemName, Price)
                               VALUES 
                                      ('Отвертка', 4.99),
                                      ('Молоток', 12.99),
                                      ('Плоскогубцы', 14.99),
                                      ('Пила', 24.99),
                                      ('Дрель', 89.99),
                                      (?, ?)''',
                            (item_name, price))

                again = input('хотите продолжить? (д/н)')

            conn.commit()
        tabl_select()
        tabl_select2()
        sred_znach1()

    except ValueError:
        print('а ты нахуй цену словами писать начал, дурачек!??')


def tabl_select():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT ItemName, Price FROM Inventory')
    results = cur.fetchall()
    conn.close()

    for row in results:
        print(f'{row[0]:50} {row[1]}')


def tabl_select2():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT ItemName, Price FROM Inventory')
    results = cur.fetchone()
    znachnone = 0

    while results is not None:
        if results[1] is not None:
            print(f'{results[0]:45} {results[1]:5}')

        else:
            print(f'{results[0]:45} {znachnone:5}')

        results = cur.fetchone()

    conn.close()


def sred_znach():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT AVG(Price) FROM Inventory')
    medium = cur.fetchone()[0]  # Извлекаем среднее значение из результата запроса
    cur.execute('SELECT MAX(Price) FROM Inventory')
    max_ch = cur.fetchone()[0]  # извлекаем максимальное значение
    cur.execute('SELECT MIN(Price) FROM Inventory')
    min_ch = cur.fetchone()[0]  # извлекаем минимальное значение
    cur.execute('SELECT SUM(Price) FROM Inventory')
    sum_ch = cur.fetchone()[0]  # извлекаем сумму чисел
    cur.execute('SELECT COUNT(Price) FROM Inventory')
    kol_str = cur.fetchone()[0]  # извлекаем количество строк
    result = [medium, max_ch, min_ch, sum_ch, kol_str]
    conn.close()
    return result


def sred_znach1():
    res = sred_znach()
    for i in res:
        print(i)


if __name__ == "__main__":
    main()
