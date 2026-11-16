book_list = []
while True:
    print("="*3, "ЧИТАТЕЛЬСКИЙ ДНЕВНИК", "="*3)
    print("1 - Добавить книгу")
    print("2 - показать все книги")
    print("3 - показать последние 5 прочитанных")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Выход")
    choice = input()
    if choice.isdigit():
        if 0 <= int(choice) <= 6:
            choice = int(choice)
            if choice == 0:
                print("Досвидания!")
                break
            elif choice == 1:
                book_list.append(input("напишите название книги: ").strip())
            elif choice == 2:
                print(*book_list)
            elif choice == 3:
                if len(book_list) > 5:
                    print(*book_list[(len(book_list)-5)::])
                else:
                    print(book_list)
            elif choice == 4:
                while True:
                    replace_choice = input("введите название книги, которой надо заменить: ").strip()
                    if replace_choice in book_list:
                        book_index = book_list.index(replace_choice)
                        book_list.remove(replace_choice)
                        book_list.insert(book_index, input("Введите название новой книги: ").strip())
                        break
                    elif replace_choice not in book_list:
                        print("такой книги нет")
            elif choice == 5:
                while True:
                    book_to_find = input("введите название искомой книги").strip()
                    if book_to_find in book_list:
                        print(f"Номер искомой книги: {book_list.index(book_to_find)}")
                        break
                    else:
                        print("этой книги нет в списке")
            elif choice == 6:
                print(f"Всего книг прочитано: {len(book_list)}")
                print(f"Первая книга: {book_list[0]}")
                print(f"Последняя книга: {book_list[len(book_list)-1]}")
        else:
            print("это не число!")
    elif not choice.isdigit():
        print("ЭТО НЕ ЧИСЛО")