"""
Docstring
"""

import re

from phone_book import BirthDate


def input_name(message: str) -> str:
    """
    Docstring
    """
    while True:
        name = input(message)
        if re.match(r'[A-Za-z\d\s]+', name):
            return name.capitalize()


def input_firstname() -> str:
    """
    Docstring
    """
    print('Please, input attributes of the person.')
    message = 'The firstname should consist only latin characters, digits or white spaces e.g. Lena \n'
    return input_name(message)


def input_lastname() -> str:
    """
    Docstring
    """
    message = 'The lastname should consist only latin characters, digits or white spaces e.g. Osipova \n'
    return input_name(message)


def validate_birth_date(date: BirthDate) -> bool:
    """
    Docstring
    """
    try:
        if date.today <= date.birth_date:
            print('birth date should be in the past')
        else:
            return True

    except ValueError as error:
        print(error)
        return False


def input_birth_date() -> BirthDate:
    """
    Docstring
    """
    birth_date = input(
        'If you want to add birth date, please input it (e.g. 31/01/1999),'
        'else press Enter \n'
        )
    while birth_date:
        if re.match(r'\d{2}/\d{2}/\d{4}', birth_date):
            birth_date = Birth_date(birth_date)
            if validate_birth_date(birth_date):
                return birth_date

        birth_date = input('The birth date should be in next format DD/MM/YYYY \n')
    
    return birth_date


def input_birthday() -> str:
    """
    Docstring
    """
    birthday = input('Input birthday in next format DD/MM \n')

    while True:
        if re.match(r'\d{2}/\d{2}', birthday):
            try:
                BirthDate.date_obj(birthday + '/1000')
                return birthday

            except ValueError as error:
                birthday = input(error)


def input_number() -> str:
    """
    Docstring
    """
    number = input('phone number (e.g. 89245548798) \n')

    while True:
        number = re.sub(r'\+7', '8', number)
        if re.match(r'\d{11}', number):
            return number
        else:
            number = input('The number should consist of 11 digits and start with 8'
                           'e.g. 89245548798 \n')


def input_to_find() -> dict:
    """
    Docstring
    """
    actual = dict()
    num = input('How many attributes to input? (e.g. 2) \n')

    while num not in {'1', '2', '3', '4'}:
        num = input('You have inputed not a number. Please, input the number between 1 and 4 \n')

    for i in range(int(num)):
        input_attr = input(
            'Input the command relevant attribute: \n'
            'f - Firstname \n'
            'l - Lastname \n'
            'b - Birth date \n'
            'p - Phone Number \n'
            )

        if input_attr == 'n':
            actual['Firstname'] = input_firstname()

        elif input_attr == 's':
            actual['Lastname'] = input_lastname()

        elif input_attr == 'b':
            actual['Birth date'] = input_birth_date()

        elif input_attr == 'p':
            actual['Phone number'] = input_number()

    return actual
