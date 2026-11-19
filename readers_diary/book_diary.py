book_list = []

def book_add(list_to_add_to):
    list_to_add_to.append(input("напишите название книги: ").strip())

def statistics(list_to_stat):
    print(f"Всего книг прочитано: {len(list_to_stat)}")
    print(f"Первая книга: {list_to_stat[0]}")
    print(f"Последняя книга: {list_to_stat[len(list_to_stat)-1]}")

while True:
    print("="*7, "ЧИТАТЕЛЬСКИЙ ДНЕВНИК", "="*7)
    print("1 - Добавить книгу")
    print("2 - показать все книги")
    print("3 - показать последние 5 прочитанных")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("7 - Удалить книгу")
    print("0 - Выход")
    choice = input("Выберите действие: ")
    if choice.isdigit():
        if 0 <= int(choice) <= 7:
            choice = int(choice)
            if choice == 0:
                print("Досвидания!")
                break
            elif choice == 1:
                book_add(book_list)
            elif choice == 2:
                print(*book_list)
            elif choice == 3:
                if len(book_list) > 5:
                    print(*book_list[(len(book_list)-5)::])
                else:
                    print(book_list)
            elif choice == 4:
                while True:
                    replace_choice = input('введите название книги, которой надо заменить (напишите "выйти в меню" для отмены действия): ').strip()
                    if replace_choice in book_list:
                        book_index = book_list.index(replace_choice)
                        book_list.remove(replace_choice)
                        book_list.insert(book_index, input("Введите название новой книги: ").strip())
                        break
                    elif replace_choice not in book_list:
                        if replace_choice.lower() == "выйти в меню":
                            break
                        print("такой книги нет")
            elif choice == 5:
                while True:
                    book_to_find = input('введите название искомой книги (напишите "выйти в меню" для отмены действия): ').strip()
                    if book_to_find in book_list:
                        print(f"Номер искомой книги: {book_list.index(book_to_find)}")
                        break
                    else:
                        if book_to_find.lower() == "выйти в меню":
                            break
                        print("этой книги нет в списке")
            elif choice == 6:
                statistics(book_list)
            elif choice == 7:
                while True:
                    book_to_remove = input('Какую книгу удалить (напишите "выйти в меню" для отмены действия): ').strip()
                    if book_to_remove in book_list:
                        print(f'Книга "{book_to_remove}" удалена')
                        book_list.remove(book_to_remove)
                        break
                    else:
                        if book_to_remove.lower() == "выйти в меню":
                            break
                        print("Этой книги нет!")
        else:
            print("этого числа нет в списке!")
    elif not choice.isdigit():
        print("это не число!")