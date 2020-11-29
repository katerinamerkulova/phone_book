"""
Docstring
"""

import datetime
import os

import pandas as pd


class BirthDate:

    """
    .birth_date DD/MM/YYYY
    .birthday DD/MM
    .datetime
    __gt__ (greater than) ~ >
    __lt__ (lower than) ~ <
    __eq__
    """

    def __init__(self, date: str):
        self.birth_date = date
        self.birthday = date.rsplit('/', maxsplit=1)[0]

        self.day, self.month, self.year = [int(x) for x in date.split('/')]
        self.date_obj = datetime.date(self.year, self.month, self.day)

        self.today = datetime.date.today()
        bd_not_yet = (self.today.month, self.today.day) < (self.month, self.day)
        self.age = self.today.year - self.year - bd_not_yet

    def __str__(self) -> str:
        return self.birth_date

    def __eq__(self, other: 'BirthDate') -> bool:
        if isinstance(other, str):
            return str(self) == other
        return self.age == other.age

    def __gt__(self, other: 'BirthDate') -> bool:
        return self.age > other.age

    def __lt__(self, other: 'BirthDate') -> bool:
        return self.age < other.age


class Person:

    """
    .firstname
    .surname
    .birth_date
    .number
    """

    def __init__(
            self,
            firstname: str,
            lastname: str,
            birth_date: BirthDate,
            number: str,
        ):
        self.firstname = firstname
        self.lastname = lastname
        self.birth_date = birth_date
        self.number = number


class PhoneBook:

    """
    Docstring
    """

    path = os.path.join('..', 'data', 'phone_book.csv')

    def __init__(self):
        try:
            self.data = pd.read_csv(self.path, encoding='utf-8', dtype=str)
        except pd.errors.EmptyDataError:
            self.data = pd.DataFrame(
                columns=[
                    'Firstname',
                    'Lastname',
                    'Birth date',
                    'Phone number',
                    ]
                )

    def print_book(self) -> bool:
        """
        Print all items to the screen
        """
        print(self.data)
        return True

    def add_record(self, person: Person) -> bool:
        """
        Add a record to the phone book
        :param person: ...
        """
        idx = self.data.shape[0]
        self.data.loc[idx] = (
            person.firstname,
            person.lastname,
            person.birth_date,
            person.number,
        )
        return True

    def find_record(self, actual: dict) -> pd.core.frame.DataFrame:
        """
        Find record by values in columns
        :param name: name of person e.g. Lena
        :param surname: surname of person e.g. Osipova
        :param birthday: birthday of person e.g. 31/01/1999
        :param number: mobile number of person e.g. 89245548798
        """

        mask = self.data[actual.keys()] == actual.values()
        row_mask = [any(row) for i, row in mask.iterrows()]

        result = self.data[row_mask]

        if result.shape[0] == 0:
            print('There is no such record')

        return result

    def update_record(self, actual: dict, idx: int)-> bool:
        """
        Docstring
        """
        self.data.loc[idx, actual.keys()] = [*actual.values()]
        return True

    def delete_record(self, actual: dict) -> bool:
        """
        Docstring
        """
        data = self.find_record(actual)

        if data.shape[0] > 1:
            print(data)
            idx = int(input('Input the index of the record to delete (e.g. 1) \n'))
        else:
            idx = data.index[0]

        self.data.drop([idx], axis=0, inplace=True)
        return True
    
    def save_phone_book(self) -> bool:
        save.data.to_csv(self.path, encoding='utf-8', index=False)
        return True
