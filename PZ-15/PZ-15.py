# Вариант 16
# Программа работает с однотабличной БД SQLite (таблица "Поручения"):
# порядковый номер, название поручения, дата выдачи, срок исполнения, исполнитель.
# Функционал: ввод данных (10 позиций), поиск, удаление и редактирование
# записей (по три SQL-запроса на каждую операцию).

import sqlite3

DB_NAME = "porucheniya.db"


def create_connection():
    # создаём соединение с БД и возвращаем объекты connection и cursor
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    return connection, cursor


def create_table():
    # создаём таблицу "Поручения", если она ещё не существует
    connection, cursor = create_connection()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS porucheniya (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                nazvanie      TEXT    NOT NULL,
                data_vydachi  TEXT    NOT NULL,
                srok_isp      TEXT    NOT NULL,
                ispolnitel    TEXT    NOT NULL
            )
            """
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при создании таблицы: {error}")
    finally:
        connection.close()


def fill_initial_data():
    # заполняем таблицу 10 начальными записями, если она пуста
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT COUNT(*) FROM porucheniya")
        count = cursor.fetchone()[0]
        if count > 0:
            print("Таблица уже содержит данные, заполнение не требуется.")
            return

        records = [
            ("Подготовить квартальный отчёт",   "2026-06-01", "2026-06-15", "Иванов И.И."),
            ("Провести совещание с отделом",     "2026-06-02", "2026-06-10", "Петров П.П."),
            ("Закупить офисное оборудование",    "2026-06-03", "2026-06-30", "Сидоров С.С."),
            ("Согласовать договор с поставщиком","2026-06-04", "2026-06-20", "Иванов И.И."),
            ("Обучить новых сотрудников",        "2026-06-05", "2026-06-25", "Козлов К.К."),
            ("Проверить проектную документацию", "2026-06-06", "2026-06-12", "Петров П.П."),
            ("Разработать план на следующий квартал", "2026-06-07", "2026-06-22", "Иванов И.И."),
            ("Обновить программное обеспечение", "2026-06-08", "2026-06-18", "Новиков Н.Н."),
            ("Оформить акты выполненных работ",  "2026-06-09", "2026-06-14", "Сидоров С.С."),
            ("Провести инвентаризацию склада",   "2026-06-10", "2026-06-28", "Козлов К.К."),
        ]

        cursor.executemany(
            """
            INSERT INTO porucheniya (nazvanie, data_vydachi, srok_isp, ispolnitel)
            VALUES (?, ?, ?, ?)
            """,
            records,
        )
        connection.commit()
        print("Добавлено 10 начальных записей.")
    except sqlite3.Error as error:
        print(f"Ошибка при заполнении таблицы: {error}")
    finally:
        connection.close()


def show_all_records():
    # выводим все записи таблицы
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT * FROM porucheniya")
        rows = cursor.fetchall()
        if not rows:
            print("Таблица пуста.")
            return
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Ошибка при выводе записей: {error}")
    finally:
        connection.close()


def search_records():
    # Поиск записей по условию.
    # Реализованы три варианта поискового SQL-запроса:
    # 1. Поиск по исполнителю (точное совпадение)
    # 2. Поиск по ключевому слову в названии поручения (частичное совпадение)
    # 3. Поиск по сроку исполнения — все поручения до указанной даты
    print("\nВарианты поиска:")
    print("1 - по исполнителю")
    print("2 - по ключевому слову в названии")
    print("3 - по сроку исполнения (все записи до указанной даты)")
    choice = input("Выберите вариант поиска: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            ispolnitel = input("Введите ФИО исполнителя: ").strip()
            cursor.execute(
                "SELECT * FROM porucheniya WHERE ispolnitel = ?",
                (ispolnitel,)
            )
        elif choice == "2":
            keyword = input("Введите ключевое слово: ").strip()
            cursor.execute(
                "SELECT * FROM porucheniya WHERE nazvanie LIKE ?",
                (f"%{keyword}%",)
            )
        elif choice == "3":
            date = input("Введите дату в формате ГГГГ-ММ-ДД: ").strip()
            cursor.execute(
                "SELECT * FROM porucheniya WHERE srok_isp <= ?",
                (date,)
            )
        else:
            print("Некорректный вариант поиска.")
            return

        rows = cursor.fetchall()
        if not rows:
            print("Записи не найдены.")
        else:
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(f"Ошибка при поиске: {error}")
    finally:
        connection.close()


def delete_record():
    # Удаление записей по условию.
    # Реализованы три варианта удаляющего SQL-запроса:
    # 1. Удаление по id записи
    # 2. Удаление по ФИО исполнителя (удаляются все его поручения)
    # 3. Удаление всех записей с истёкшим сроком (раньше указанной даты)
    print("\nВарианты удаления:")
    print("1 - по id записи")
    print("2 - по ФИО исполнителя")
    print("3 - по сроку исполнения (удалить все записи раньше даты)")
    choice = input("Выберите вариант удаления: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            record_id = int(input("Введите id записи: ").strip())
            cursor.execute(
                "DELETE FROM porucheniya WHERE id = ?",
                (record_id,)
            )
        elif choice == "2":
            ispolnitel = input("Введите ФИО исполнителя: ").strip()
            cursor.execute(
                "DELETE FROM porucheniya WHERE ispolnitel = ?",
                (ispolnitel,)
            )
        elif choice == "3":
            date = input("Введите дату в формате ГГГГ-ММ-ДД: ").strip()
            cursor.execute(
                "DELETE FROM porucheniya WHERE srok_isp < ?",
                (date,)
            )
        else:
            print("Некорректный вариант удаления.")
            return

        connection.commit()
        print(f"Удалено записей: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as error:
        print(f"Ошибка при удалении: {error}")
    finally:
        connection.close()


def edit_record():
    # Редактирование записей по условию.
    # Реализованы три варианта обновляющего SQL-запроса:
    # 1. Изменение исполнителя по id записи
    # 2. Изменение срока исполнения по id записи
    # 3. Переназначение исполнителя сразу во всех его поручениях (по ФИО)
    print("\nВарианты редактирования:")
    print("1 - изменить исполнителя по id")
    print("2 - изменить срок исполнения по id")
    print("3 - переназначить исполнителя во всех его поручениях")
    choice = input("Выберите вариант редактирования: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            record_id = int(input("Введите id записи: ").strip())
            ispolnitel = input("Введите нового исполнителя: ").strip()
            cursor.execute(
                "UPDATE porucheniya SET ispolnitel = ? WHERE id = ?",
                (ispolnitel, record_id)
            )
        elif choice == "2":
            record_id = int(input("Введите id записи: ").strip())
            srok = input("Введите новый срок (ГГГГ-ММ-ДД): ").strip()
            cursor.execute(
                "UPDATE porucheniya SET srok_isp = ? WHERE id = ?",
                (srok, record_id)
            )
        elif choice == "3":
            old_isp = input("Введите текущее ФИО исполнителя: ").strip()
            new_isp = input("Введите новое ФИО исполнителя: ").strip()
            cursor.execute(
                "UPDATE porucheniya SET ispolnitel = ? WHERE ispolnitel = ?",
                (new_isp, old_isp)
            )
        else:
            print("Некорректный вариант редактирования.")
            return

        connection.commit()
        print(f"Изменено записей: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as error:
        print(f"Ошибка при редактировании: {error}")
    finally:
        connection.close()


def main():
    # главное меню программы
    create_table()
    fill_initial_data()

    menu = """
========== Контроль исполнения поручений ==========
1 - показать все записи
2 - найти записи
3 - удалить запись
4 - редактировать запись
0 - выход
====================================================
"""

    while True:
        print(menu)
        action = input("Выберите действие: ").strip()

        if action == "1":
            show_all_records()
        elif action == "2":
            search_records()
        elif action == "3":
            delete_record()
        elif action == "4":
            edit_record()
        elif action == "0":
            print("Завершение программы.")
            break
        else:
            print("Некорректный пункт меню, повторите ввод.")


if __name__ == "__main__":
    main()