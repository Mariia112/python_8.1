import time
import validate

def show_menu():
    print('---')
    time.sleep(1)
    print('Главное меню')
    mode = input('1. Внести данные в книгу\n2. Показать телефонную книгу\n3. Поиск контакта\n4. Выход из меню\nВведите 1, 2, 3 и 4: ')
    if mode in '1234':
        print('---')
        return int(mode)
    else:
        print('Ошибка! Введите 1, 2, 3 или 4!')

def write_data():
    phone_record = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    phone = ''
    while not validate.check_phone(phone):
        phone = input('Введите номер телефона: ')
        if not validate.check_phone(phone):
            print('Некорректный номер телефона.')
    phone_record.append(phone)
    description = input('Введите комментарий: ')
    if description:
        phone_record.append(description)
    print(f'Запись добавлена: {str.join(", ", phone_record)}')
    return phone_record

def search_data():
    return input('Введите ФИО или номер для поиска: ')


def show_data(data):
    print(f'Найдено записей: {len(data)}')
    for line in data:
        print(line)

def show_ext_data(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        for text in line:
            print(text)