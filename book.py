from random import randint, uniform, choice
from os import path

from faker import Faker


class Book:

    def __init__(self):
        self.fake = Faker('ru-RU')
        self.books_file_path = path.join('data', 'books.txt')

    def __get_title(self) -> str:
        """
        Function returns random book title from the books.txt
        :return:
        """
        with open(self.books_file_path, 'r') as file:
            content = file.read().split('\n')
            return choice(content)

    @staticmethod
    def __get_random_int(start_position: int, end_position: int) -> int:
        """
        Function returns random int value (year, number of pages, etc.)
        :param start_position: start interval value
        :param end_position: end interval value
        :return: random int value from defined interval
        """
        return randint(start_position, end_position)

    @staticmethod
    def __get_random_float(start_position: int, end_position: int) -> float:
        """
        Function returns random float value (price, rating, etc.)
        :param start_position: start interval value
        :param end_position: end interval value
        :return: random float value from defined interval
        """
        return round(uniform(start_position, end_position), 1)

    @staticmethod
    def __get_authors(fake: Faker) -> list[str]:
        """
        Function returns list of fake writers
        :param fake: Faker class example
        :return: writers list
        """
        return [fake.name() for _ in range(randint(1, 3))]

    @staticmethod
    def __get_isbn(fake: Faker) -> str:
        """
        Function returns fake book number (isbn13)
        :param fake: Faker class example
        :return: fake isbn13
        """
        return fake.isbn13()

    def generate_book(self) -> dict:
        """
        Function returns book description in dict format
        :return: dict
        """
        output = {'fields': {
                                'title': self.__get_title(),
                                'year': self.__get_random_int(1900, 2022),
                                'pages': self.__get_random_int(1, 1000),
                                'isbn13': self.__get_isbn(self.fake),
                                'rating': self.__get_random_float(0, 5),
                                'price': self.__get_random_float(0, 1000000),
                                'author': self.__get_authors(self.fake)
                            }}

        return output


if __name__ == '__main__':
    book = Book()

    book.generate_book()
