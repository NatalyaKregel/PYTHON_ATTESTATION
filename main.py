import notebook

def main():
    while True:
        print('----------------------------------- ')
        print('ДОБРО ПОЖАЛОВАТЬ В ЗАПИСНУЮ КНИЖКУ!')
        print('----------------------------------- ')

        print('Выберите действие, которое хотите сделать:\n1 - добавить заметку\n2 - изменить заметку\n3 - удалить заметку\n4 - вывести список всех заметок\n5 - просмотреть нужную заметку\n0 - выход')
        choice = input()
        if choice == '1':
            notebook.add_note()
        elif choice == '2':
            notebook.edit_note()
        elif choice == '3':
            notebook.delete_note()
        elif choice == '4':
            notebook.list_notes()
        elif choice == '5':
            notebook.view_note()
        elif choice == '0':
            break
        else:
            print('Некорректный ввод')

if __name__ == '__main__':
    main()