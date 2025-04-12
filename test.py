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
            read_position()

        if answer_user == 3:
            update_position()

        if answer_user == 4:
            delete_position()


def display_meny():
    print('\n ----- Меню ведения учета инструментов -----')
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


def read_position():
    read_user = input('Введите название искомой позиции: ').strip()
    print(f'ищем позицию {read_user}')
    result = display_open(read_user)
    if result:
        print(f'{result} строк(а) найдено')


def update_position():
    upt_position = input('введите название искомой позиции: ')
    found = display_open(upt_position)
    if found:
        update = int(input('Введите ID искомой позиции: '))
        new_name = input('Введите новое название позиции: ')
        new_price = float(input('введите новую цену: '))
        upt(update, new_name, new_price)
        print(f'{found} строк(а) обновлена')


def delete_position():
    del_position = input('введите название искомой позиции: ')
    found = display_open(del_position)
    if found:
        id_del = int(input('Введите ID удаляемой позиции'))
        question = input('Вы точно хотите удалить позицию? (д/н): ')
        if question.lower() == 'д':
            delete_pos(id_del)


def display_open(name):
    print(f'Ищем позицию: {name}')
    with sqlite3.connect('inventory.db') as conn:
        cur = conn.cursor()
        cur.execute('''
                SELECT * FROM Inventory
                WHERE upper (ItemName) == ?
            ''', (name,))

        results = cur.fetchall()
        print(f'Найдено записей: {len(results)}')

        if results:
            print('Найденные позиции:')
            for row in results:
                print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
        else:
            print('Позиции с таким названием не найдены.')
    return len(results)


def upt(id_new_pos, new_name, new_price):
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE Inventory
                           SET ItemName = ?,
                               Price = ?
                           WHERE itemID = ?
                           ''', (new_name, new_price, id_new_pos))
            conn.commit()
            if cur.rowcount > 0:
                print("Обновление успешно выполнено.")
            else:
                print("Запись не найдена или данные не изменены.")

    except sqlite3.Error as err:
        print(f'ошибочка {err}')


def delete_pos(id_del):
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            cur.execute('''DELETE FROM Inventory WHERE ItemId == ?
                        ''', (id_del,))
            conn.commit()
    except sqlite3.Error as err:
        print(f'ошибочка вышла {err}')


if __name__ == '__main__':
    main()
