"""
Docstring
"""

import pandas as pd


class Birthday:
    """
    .birth_date DD/MM/YYYY
    .birthday DD/MM
    .datetime
    __gt__ (greater than) ~ >
    __lt__ (lower than) ~ <
    __eq__
    """

    def __init__(self, date):
        self.birth_date = date
        self.birthday = date.rsplit('/', maxsplit=1)[0]
        self.datetime = date(self.year, self.month, self.day)

        self.day = int(date.split('/')[0])
        self.month = int(date.split('/')[1])
        self.year = int(date.split('/')[2])

        self.today = date.today()
        was_bd = (self.today.month, self.today.day) < (self.month, self.day)
        self.age = self.today.year - self.year - was_bd

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return self.birth_date


class Person:
    """
    .name
    .surname
    .birthday
    .number
    """

    def __init__(self, name, surname, birthday, number):
        self.name = name
        self.surname = surname
        self.birthday = Birthday(birthday)
        self.number = number


class PhoneBook:

    def __init__(self):
        try:
            path = r'..\data\phone_book.csv'
            self.data = pd.read_csv(path, encoding='utf-8')
        except pd.errors.EmptyDataError:
            self.data = pd.DataFrame(columns=['Name',
                                              'Surname',
                                              'Birthday',
                                              'Number'])

    def print_book(self):
        """
        Print all items to the screen
        """
        print(self.data)

    def add_record(self,
                   person):
        """
        Add a record to the phone book
        :param person: ...
        """
        idx = self.data.shape[0]
        self.data.loc[idx] = (person.name,
                              person.surname,
                              person.birthday,
                              person.number)

    def find_record(self,
                    name=None,
                    surname=None,
                    birthday=None,
                    number=None,
                    ):
        """
        Find record by values in columns
        :param name: name of person e.g. Lena
        :param surname: surname of person e.g. Osipova
        :param birthday: birthday of person e.g. 31/01/1999
        :param number: mobile number of person e.g. 89245548798
        """
        if number:
            number = int(number)

        actual = {col: value for col, value
                  in zip(self.data.columns,
                         (name, surname, birthday, number)
                         ) if value
                  }
        mask = self.data[actual.keys()] == actual.values()
        row_mask = [any(row) for i, row in mask.iterrows()]

        result = self.data[row_mask]

        if result.shape[0] == 0:
            print('There is no this record')

        return result

    def update_record(self,
                      name=None,
                      surname=None,
                      birthday=None,
                      number=None,
                      idx=None):
        """
        """
        actual = {col: value for col, value
                  in zip(self.data.columns,
                         (name, surname, birthday, number)
                         ) if value
                  }
        self.data.loc[idx, actual.keys()] = [*actual.values()]

    def delete_record(self,
                      name=None,
                      surname=None,
                      birthday=None,
                      number=None,
                      ):
        """
        """

        data = self.find_record(name=name,
                                surname=surname,
                                birthday=birthday,
                                number=number)
        if data.shape[0] > 1:
            print(data)
            idx = int(input('Input the index of the record to delete (e.g. 1) \n'))
        else:
            idx = data.index[0]
        self.data.drop([idx], axis=0, inplace=True)
