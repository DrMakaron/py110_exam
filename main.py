from random import randint, uniform, choice

from faker import Faker

from conf import Config


CFG_FILE = 'config.ini'


def get_title() -> str:
    """
    Function returns random book title from the books.txt
    :return:
    """
    with open('books.txt', 'r') as file:
        content = file.read().split('\n')
        return choice(content)


def get_random_int(start_position: int, end_position: int) -> int:
    """
    Function returns random int value (year, number of pages, etc.)
    :param start_position: start interval value
    :param end_position: end interval value
    :return: random int value from defined interval
    """
    return randint(start_position, end_position)


def get_random_float(start_position: int, end_position: int) -> float:
    """
    Function returns random float value (price, rating, etc.)
    :param start_position: start interval value
    :param end_position: end interval value
    :return: random float value from defined interval
    """
    return round(uniform(start_position, end_position), 1)


def get_authors(fake: Faker) -> list[str]:
    """
    Function returns list of fake writers
    :param fake: Faker class example
    :return: writers list
    """
    return [fake.name() for _ in range(randint(1, 3))]


def get_isbn(fake: Faker) -> str:
    """
    Function returns fake book number (isbn13)
    :param fake: Faker class example
    :return: fake isbn
    """
    return fake.isbn13()


if __name__ == '__main__':
    config = Config(CFG_FILE)
    faker = Faker('ru-RU')

    print(get_random_int(1900, 2022), get_title(), get_random_float(0, 5), get_authors(faker), get_isbn(faker))
