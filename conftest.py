import pytest
from main import BooksCollector
@pytest.fixture
def book_1_name():
    return 'Гордость и предубеждение и зомби'
@pytest.fixture
def book_2_name():
    return 'Что делать, если ваш кот хочет вас убить'
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_1_book(collector, book_1_name):
    collector.add_new_book(book_1_name)
    return collector
@pytest.fixture
def books():
    books = {
        "Гордость и предубеждение и зомби": 10,
        "Что делать, если ваш кот хочет вас убить": 9,
        "Тёмные начала": 8,
        "Автостопом по галактике": 7,
        "Гарри Поттер и Кубок огня": 6,
        "Убить пересмешника": 5,
        "Винни Пух": 4,
        "1984": 3,
        "Лев, колдунья и платяной шкаф": 2,
        "Джейн Эйр": 1,
        "Уловка-22": 10,
        "Грозовой перевал": 9,
        "Пение птиц": 8,
        "Ребекка": 7,
        "Над пропастью во ржи": 6,
        "Ветер в ивах": 5,
        "Большие надежды": 4,
        "Маленькие женщины": 3,
        "Мандолина капитана Корелли": 2,
        "Война и мир": 1
    }
    return books
@pytest.fixture
def collector_with_books(collector, books):
    for key, value in books.items():
        collector.add_new_book(key)
        collector.set_book_rating(key,value)
    return collector
