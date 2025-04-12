import sqlite3
EXIT = 5


def main():
    while True:
        answer_user = display_meny()
        if answer_user == EXIT:
            print('выход из программы')
            break

        if answer_user == 1:
            create_table()

        if answer_user == 2:
            read()

        if answer_user == 3:
            update_position()

        if answer_user == 4:
            delete_position()


def display_meny():
    print('----- Меню ведения учета инструментов -----')
    print('1. Создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. Удалить позицию')
    print('5. Выйти из программы')
    answer_user = int(input('Введите свой вариант: '))

    if 0 < answer_user < 6:
        return answer_user
    else:
        print('совсем даун, смотри куда тыкаешь')


def create_table():
    print('создать новую позицию')

    with sqlite3.connect('inventory.db') as conn:
        cur = conn.cursor()
        name_user = input('Название позиции: ')
        price_position = float(input('Цена: '))

        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES 
                            (?, ?)''',
                    (name_user, price_position))
        conn.commit()


def read():
    read_user = input('Введите название искомой позиции: ').strip().lower()
    print(f'Ищем позицию: {read_user}')
    num_found = display_item(read_user)
    print(f'{num_found} строк(а) найдено.')


def update_position():
    pass


def delete_position():
    pass


def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                            WHERE ItemName == ?''',
                    (name,))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} название: {row[1]:<15}'
                  f'Цена: {row[2]:<6}')
    except sqlite3.Error as err:
        print('ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()

            return len(results)


if __name__ == '__main__':
    main()
