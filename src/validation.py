"""
Docstring
"""

import re

from phone_book import Birthday

# todo rename module more appropriately

# todo merge input_name and input_surname as one function, they are almost the same
def input_name():
    print('Please, input attributes of the person.')
    while True:
        name = input('The name should consist only latin characters,'
                      'digits or white spaces e.g. Lena \n')
        if re.match(r'[A-Za-z\d\s]+', name):
            return name.capitalize()


def input_surname():
    while True:
        surname = input('The surname should consist only latin characters,'
                        'digits or white spaces e.g. Osipova \n')
        if re.match(r'[A-Za-z\d\s]+', surname):
            return surname.capitalize()


def validate_birthday(date):
    try:
        if date.today <= date.birth_date:
            print('birthday should be in the past')
        else:
            return True

    except ValueError as error:
        print(error)
        return False


def input_birth_date():
    birth_date = input('If you want to add birthday, please input it (e.g. 31/01/1999),'
                     'else press Enter \n')
    while birth_date:
        if re.match(r'\d{2}/\d{2}/\d{4}', birth_date):
            birth_date = Birthday(birth_date)
            if validate_birthday(birth_date):
                return birth_date

        birth_date = input('The birthday should be in next format DD/MM/YYYY \n')


def input_birthday():
    """
    Reimplement as:
    while True:
        get_user_input
        validation1 - as a function (outside input_birthday)
        validation2
        ...
        if all_ok:
            return True
    """
    birthday = input('Input birthday in next format DD/MM \n')
    birthday = Birthday(birthday + '/1000')
    # todo


def input_number():
    number = input('phone number (e.g. 89245548798) \n')
    number = re.sub(r'\+7', '8', number)
    is_number_correct = re.match(r'\d{11}', number)
    while not is_number_correct:  # -> while True
        number = input('The number should consist of 11 digits and start with 8 e.g. '
                       '89245548798 \n')
        is_number_correct = re.match(r'\d{11}', number)
    return number


def input_to_find():
    # todo reimplement as {'name': ..., ...}
    name, surname, birthday, number = None, None, None, None
    num = input('How many attributes to input? (e.g. 2) \n')

    while num not in {'1', '2', '3', '4'}:
        num = input('You have inputed not a number. Please, input the number between 1 and 4 \n')

    for i in range(int(num)):
        input_attr = input(
            'Input the command relevant attribute: \n n - Name \n s - Surname \n b - Birthday \n '
            'p - Phone Number \n')

        if input_attr == 'n':
            name = input_name()

        elif input_attr == 's':
            surname = input_surname()

        elif input_attr == 'b':
            birthday = input_birthday()

        elif input_attr == 'p':
            number = input_number()

    return name, surname, birthday, number
