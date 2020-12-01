from datetime import date
import os

from phone_book import BirthDate, PhoneBook, Person
import input_handling


def get_user_input() -> str:
    user_input = input(
        '\nPlease, input the command relevant desired operations: \n'
        'p - print phone book \n'
        'pa - print age of the person \n'
        'a - add new record \n'
        'u - update record \n'
        'f - find person \n'
        'fb - find person by birth date \n'
        'fm - find people with birthdays in next month \n'
        'fy - find people who are younger \n'
        'fo - find people who are older \n'
        'fa - find people with the age \n'
        'dn - delete record by name \n'
        'dp - delete record by phone number \n'
        'c - clear screen \n'
        'e - exit the programm \n'
        '>> '
        )
    return user_input


def print_age() -> bool:
    firstname = input_handling.input_firstname()
    lastname = input_handling.input_lastname()

    actual = {
        'Firstname': firstname,
        'Lastname': lastname,
        }

    idx = phone_book.find_record(actual).index[0]
    birth_date = BirthDate(
        phone_book.data.loc[idx, 'Birth date']
        )

    print(f'{firstname} {lastname} is {birth_date.age} years old.')

    return True


def get_additional_user_input() -> str:
    user_input = input(
        'The person already has been in the phone book. '
        'Please, choose what you want to do with it: \n'
        'u - update current record \n'
        'c - change name of current record \n'
        'r - return to main menu \n'
        '>> '
        )
    return user_input


def update_current_record(actual: dict) -> bool:
    idx = phone_book.find_record(actual).index[0]

    birth_date = input_handling.input_birth_date()
    number = input_handling.input_number()

    phone_book.update_record(
        {
            'Birth date': birth_date,
            'Phone number': number,
            },
        idx=idx,
        )
    return True


def change_name_of_current_record(actual: dict) -> bool:
    new_firstname = input_handling.input_firstname()
    new_lastname = input_handling.input_lastname()

    idx = phone_book.find_record(actual).index[0]

    phone_book.update_record(
        {
            'Firstname': new_firstname,
            'Lastname': new_lastname,
            },
        idx=idx,
        )
    return True


def add_record() -> bool:
    firstname = input_handling.input_firstname()
    lastname = input_handling.input_lastname()

    actual = {
        'Firstname': firstname,
        'Lastname': lastname,
        }

    try:
        record = phone_book.find_record(actual).index[0]

    except IndexError:
        birth_date = input_handling.input_birth_date()
        number = input_handling.input_number()

        person = Person(firstname, lastname, birth_date, number)
        phone_book.add_record(person)

        return True
    
    else:
        user_input = get_additional_user_input()
        
        if user_input == 'u':  # update current record
            res = update_current_record(actual)
            return res

        elif user_input == 'c':  # change name of current record
            res = change_name_of_current_record(actual)
            return res

        elif user_input == 'r':  # return to main menu
            return True


def update_record() -> bool:
    print('Which person do you want to update?')
    actual = input_handling.input_to_find()

    data = phone_book.find_record(actual)
    
    if data.shape[0] > 1:
        print(data)
        idx = int(input('Input the index of the record to update (e.g. 1) \n'))
    else:
        idx = data.index[0]

    print('What attribute do you want to update?')
    actual = input_handling.input_to_find()

    phone_book.update_record(
        actual=actual,
        idx=idx,
        )
    return True


def find_person() -> bool:
    print('Search it by which column(s)?')
    actual = input_handling.input_to_find()

    res = phone_book.find_record(actual)
    print(res)

    return True


def find_birth_date_by_condition(function: 'function') -> bool:
    idx_list = []
    for idx, bd in enumerate(phone_book.data['Birth date']):
        bd = BirthDate(bd)
        if function(bd):
            idx_list.append(idx)

    print(phone_book.data.loc[idx_list, :])

    return True


def find_person_by_birthday() -> bool:
    birthday = input_handling.input_birthday()

    res = find_birth_date_by_condition(
        (lambda x: x.month == birthday.month 
            and x.day == birthday.day
            )
        )

    return res


def find_people_with_birthdays_in_next_month() -> bool:
    res = find_birth_date_by_condition(
        (lambda x: 0 <= (
            date(x.today.year, x.month, x.day) - 
            x.today
            ).days < 31)
        )

    return res


def find_people_who_are_younger()-> bool:
    age = int(input('Input age (e.g. 27) \n>> '))

    return find_birth_date_by_condition((lambda x: x.age < age))


def find_people_who_are_older() -> bool:
    age = int(input('Input age to comparison (e.g. 27) \n>> '))

    return find_birth_date_by_condition((lambda x: x.age > age))


def find_people_with_the_age() -> bool:
    age = int(input('Input age to comparison (e.g. 27) \n>> '))

    return find_birth_date_by_condition((lambda x: x.age == age))


def delete_record_by_name() -> bool:
    firstname = input_handling.input_firstname()
    lastname = input_handling.input_lastname()

    phone_book.delete_record(
        {
            'Firstname': firstname,
            'Lastname': lastname,
            }
        )
    return True


def delete_record_by_number() -> bool:
    number = input_handling.input_number()
    phone_book.delete_record({'Phone number': number})
    return True


def handle_user_input(user_input: str) -> bool:
    if user_input == 'p':  # print phone book
        return phone_book.print_book()

    if user_input == 'pa':  # print age
        return print_age() 

    if user_input == 'a':  # add new record
        return add_record()

    if user_input == 'u':  # update record
        return update_record()

    if user_input == 'f':  # find person
        return find_person()

    if user_input == 'fb':  # find person by birthday
        return find_person_by_birthday()

    if user_input == 'fm':  # find people with birthdays in next month
        return find_people_with_birthdays_in_next_month()

    if user_input == 'fy':  # find people who are younger
        return find_people_who_are_younger()

    if user_input == 'fo':  # find people who are older
        return find_people_who_are_older()

    if user_input == 'fa':  # find people with the age
        return find_people_with_the_age()

    if user_input == 'dn':  # delete record by name
        return delete_record_by_name()

    if user_input == 'dp':  # delete record by phone number
        return delete_record_by_number()

    if user_input == 'c':  # clear screen
        _ = os.system('cls')
        return True

    if user_input == 'e':  # exit the programm
        return False

    print('You have entered not a code of possible operations. Please do it next time.')
    return True


def main() -> bool:
    print("Hello, dear User! I'm your pleasant programm to work with phone books.")

    global phone_book
    phone_book = PhoneBook()

    while True:
        user_input = get_user_input()

        if handle_user_input(user_input):
            continue
        else:
            break

    return phone_book.save_phone_book()


if __name__ == '__main__':
    if main():
        print('Succesfully done!')
    else:
        print('Something went wrong.')
