"""
Docstring
"""

import os

from phone_book import Birthday, PhoneBook, Person
import validation


if __name__ == '__main__':

    is_continue = True
    print("Hello, dear User! I'm your pleasant programm to work with phone books.")
    phone_book = PhoneBook()

    while is_continue:
        user_input = input('\nPlease, input the command relevant desired operations: \n'
                           'p - print phone book \n'
                           'pa - print age of the person \n'
                           'a - add new record \n'
                           'u - update record \n'
                           'f - find person \n'
                           'fb - find person by birthday \n'
                           'fm - find people with birthdays in next month \n'
                           'fy - find people who are younger \n'
                           'fo - find people who are older \n'
                           'fa - find people with the age \n'
                           'dns - delete record by name and surname \n'
                           'dn - delete record by number \n'
                           'c - clear screen \n'
                           'e - exit the programm \n')

        if user_input == 'p':  # print phone book
            phone_book.print_book()

        elif user_input == 'pa':  # print age
            name = validation.input_name()
            surname = validation.input_surname()
            
            idx = phone_book.find_record(name=name,
                                         surname=surname).index[0]
            birthday = Birthday(phone_book.data.loc[idx, 'Birthday'])

            print(f'{name} {surname} is {birthday.age} years old.') 

        elif user_input == 'a':  # add new record
            name = validation.input_name()
            surname = validation.input_surname()

            try:
                record = phone_book.find_record(name=name,
                                                surname=surname).index[0]
                user_input = input('The person already has been in the phone book.'
                                   'Please, choose what you want to do with it: \n'
                                   'u - update current record \n'
                                   'c - change name and surname of current record \n'
                                   'r - return to main menu \n')
                
                if user_input == 'u':  # update current record
                    idx = phone_book.find_record(name=name,
                                                 surname=surname).index[0]
                    birthday = validation.input_birthday()
                    number = validation.input_number()

                    phone_book.update_record(birthday=birthday,
                                             number=number,
                                             idx=idx)
   
                elif user_input == 'c':  # change name and surname of current record
                    new_name = validation.input_name()
                    new_surname = validation.input_surname()

                    idx = phone_book.find_record(name=name,
                                                 surname=surname).index[0]

                    phone_book.update_record(name=new_name,
                                             surname=new_surname,
                                             idx=idx)

                elif user_input == 'r':  # return to main menu
                    is_continue = True

            except IndexError:
                birthday = validation.input_birthday()
                number = validation.input_number()

                person = Person(name, surname, birthday, number)
                phone_book.add_record(person)

        elif user_input == 'u':  # update record
            print('Which person do you want to update?')
            name, surname, birthday, number = validation.input_to_find()

            idx = phone_book.find_record(name=name,
                                         surname=surname,
                                         birthday=birthday,
                                         number=number,
                                         ).index[0]
            print('What attribute do you want to update?')
            name, surname, birthday, number = validation.input_to_find()

            phone_book.update_record(name=name,
                                     surname=surname,
                                     birthday=birthday,
                                     number=number,
                                     idx=idx)

        elif user_input == 'f':  # find person
            print('Search it by which column(s)?')
            name, surname, birthday, number = validation.input_to_find()

            res = phone_book.find_record(name=name,
                                         surname=surname,
                                         birthday=birthday,
                                         number=number)
            print(res)

        elif user_input == 'fb':  # find person by birthday
            birthday = Birthday(validation.input_birthday(year=True))

            idx_list = []
            for idx, bd in enumerate(phone_book.data['Birthday']):
                bd = Birthday(bd)
                if bd.month == birthday.month and bd.day == birthday.day:
                    idx_list.append(idx)
            print(phone_book.data.loc[idx_list, :])

        elif user_input == 'fm':  # find people with birthdays in next month

            idx_list = []
            for idx, bd in enumerate(phone_book.data['Birthday']):
                bd = Birthday(bd)
                if abs((bd.datetime - bd.today).days) < 31:
                    idx_list.append(idx)
            print(phone_book.data.loc[idx_list, :])

        elif user_input == 'fy':  # find people who are younger
            age = int(input('Input age (e.g. 27) \n'))

            idx_list = []
            for idx, bd in enumerate(phone_book.data['Birthday']):
                bd = Birthday(bd)
                if bd.age < age:
                    idx_list.append(idx)
            print(phone_book.data.loc[idx_list, :])

        elif user_input == 'fo':  # find people who are older
            age = int(input('Input age to comparison (e.g. 27) \n'))

            idx_list = []
            for idx, bd in enumerate(phone_book.data['Birthday']):
                bd = Birthday(bd)
                if bd.age > age:
                    idx_list.append(idx)
            print(phone_book.data.loc[idx_list, :])

        elif user_input == 'fa':  # find people with the age
            age = int(input('Input age to comparison (e.g. 27) \n'))

            idx_list = []
            for idx, bd in enumerate(phone_book.data['Birthday']):
                bd = Birthday(bd)
                if bd.age == age:
                    idx_list.append(idx)
            print(phone_book.data.loc[idx_list, :])

        elif user_input == 'dns':  # delete record by name and surname
            name = validation.input_name()
            surname = validation.input_surname()

            phone_book.delete_record(name=name,
                                     surname=surname)

        elif user_input == 'dn':  # delete record by number
            number = validation.input_number()
            phone_book.delete_record(number=number)

        elif user_input == 'c':  # clear screen
            _ = os.system('cls')

        elif user_input == 'e':  # exit the programm
            is_continue = False

        else:
            print('You have entered not a number of possible operations. Please do it next time.')

    path = r'..\data\phone_book.csv'
    phone_book.data.to_csv(path, encoding='utf-8', index=False)
