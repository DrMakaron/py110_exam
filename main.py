from itertools import count
import json
from os import path

from conf import Config
from book import Book

CFG_FILE = path.join('data', 'config.ini')


def main(model_name: str, book_: Book, iterations: int = 1) -> None:
    """
    Function generates dict and write it into JSON file
    :param model_name:
    :param book_:
    :param iterations:
    :return:
    """
    counter = count(1)

    result = [{"model": model_name, "pk": next(counter), "fields": book_.generate_book()} for _ in range(iterations)]

    with open('output.json', 'w') as json_output:
        json.dump(result, json_output, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    config = Config(CFG_FILE)
    book = Book()

    main(config.MODEL, book, 100)
