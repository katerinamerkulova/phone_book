'''
Docstring
'''

from datetime import date
import re

from phone_book import Birthday


def input_name():
    print('Please, input attributes of the person.')
    while True:
        name = input('The name should consist only latin characters,'
                      'digits or white spaces, first letter must be capital e.g. Lena \n')  
        if re.match(r'[A-Za-z\d\s]+', name):
            return name.capitalize()


def input_surname():
    while True:
        surname = input('The surname should consist only latin characters,'
                        'digits or white spaces, first letter must be capital e.g. Osipova \n')
        if re.match(r'[A-Za-z\d\s]+', surname):
            return surname.capitalize()


def input_birthday(year=False):
    if year: # ???
        birthday = input('Input birthday in next format DD/MM \n') + '/1000'
    else:
        birthday = input('If you want to add birthday, please input it (e.g. 31/01/1999),'
                         'else press Enter \n')

    while birthday:
        if re.match(r'\d{2}\/\d{2}\/\d{4}', birthday):
            birthday = Birthday(birthday)
        else:

        try:
            if birthday.today <= birthday.birth_date:
                print('birthday should be in the past')
            else:
                return birthday

        except ValueError as error:
            print(error)
            is_birthday_correct = False
        
        while not is_birthday_correct:
            birthday = Birthday(input('The birthday should be in next format DD/MM/YYYY \n'))
            is_birthday_correct = re.match(r'\d{2}\/\d{2}\/\d{4}', birthday)

            try:
                if birthday.today <= birthday.birth_date:
                    print('birthday should be in the past')
                    is_birthday_correct = False
                else:
                    is_birthday_correct = True

            except ValueError as error:
                print(error)
                is_birthday_correct = False
    return birthday

def input_number():
    number = input('number (e.g. 89245548798) \n')
    print(1, number)
    number = re.sub(r'\+7', '8', number)
    print(2, number)
    is_number_correct = re.match(r'\d{11}', number)
    while not is_number_correct:
        number = input('The number should consist 11 digits and start with 8 e.g. 89245548798 \n')
        is_number_correct = re.match(r'\d{11}', number)
    return number


def input_to_find():
    name, surname, birthday, number = None, None, None, None
    num = input('How many attributes to input? (e.g. 2) \n')

    while num not in '1234':
        num = input('You have inputed not a number. Please, input the number between 1 and 4 \n')

    for i in range(int(num)):
        input_attr = input('Input the command relevant attribute: \n n - Name \n s - Surname \n b - Birthday \n nb - Number \n')

        if input_attr == 'n':
            name = input_name()

        elif input_attr == 's':
            surname = input_surname()

        elif input_attr == 'b':
            birthday = input_birthday()

        elif input_attr == 'nb':
            number = input_number()

    return name, surname, birthday, number

