import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    ### METHOD add_new_book
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_default_rating_equal_1(self, collector_with_1_book, book_1_name):
        # Checks that new book has default rating = 1
        assert collector_with_1_book.get_book_rating(book_1_name) == 1
    def test_add_new_book_add_two_equal_books_added_one(self, collector_with_1_book, book_1_name):
        # Checks impossibility to add two books to "books_rating" dictionary with the same name
        collector_with_1_book.add_new_book(book_1_name)  # add the second book with the same name
        assert len(collector_with_1_book.get_books_rating()) == 1

    ### METHOD set_book_rating
    def test_set_book_rating_to_not_existing_book_rating_none(self, collector, book_1_name):
        # Checks if an not existing book can't be rated
        collector.set_book_rating(book_1_name,7)
        assert collector.get_book_rating(book_1_name) == None
    negative_rating = [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1]
    @pytest.mark.parametrize('rating', negative_rating)
    def test_set_book_rating_negative_rating(self, collector_with_1_book, book_1_name, rating):
        # Checks if the new rating is in [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1] the rating won't be changed (default 1)
        collector_with_1_book.set_book_rating(book_1_name, rating)
        assert collector_with_1_book.get_book_rating(book_1_name) == 1
    def test_set_book_with_rating_1_get_rating_1(self, collector_with_1_book, book_1_name):
        # Checks if the new rating 1, change rating to 5 than to 1. The rating will be changed to 1
        collector_with_1_book.set_book_rating(book_1_name,5)  # set rating 5 to change it to 1
        collector_with_1_book.set_book_rating(book_1_name,1)
        assert collector_with_1_book.get_book_rating(book_1_name) == 1
    positive_rating = [2, 5, 9, 10]
    @pytest.mark.parametrize('rating', positive_rating)
    def test_set_book_rating_positive_rating(self, collector_with_1_book, book_1_name, rating):
        # Checks if the new rating is in [2, 5, 9, 10] the rating will be changed to [2, 5, 9, 10]
        collector_with_1_book.set_book_rating(book_1_name, rating)
        assert collector_with_1_book.get_book_rating(book_1_name) == rating

    ### METHOD get_book_rating
    def test_get_book_rating_existing_book_rating_1(self, collector_with_1_book, book_1_name):
        # Checks possibility to get the rating of existing book
        assert collector_with_1_book.get_book_rating(book_1_name) == 1
    def test_get_book_rating_not_existing_book_rating_none(self, collector_with_1_book, book_2_name):
        # Checks impossibility to get the rating of not existing book
        assert collector_with_1_book.get_book_rating(book_2_name) == None

    ### METHOD get_books_with_specific_rating
    get_positive_rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    @pytest.mark.parametrize('rating', get_positive_rating)
    def test_get_books_with_specific_rating_positive_rating(self, collector_with_books, rating):
        # Checks possibility to get the list with rating in range 1-10
        assert len(collector_with_books.get_books_with_specific_rating(rating)) == 2

    get_negative_rating = [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1]
    @pytest.mark.parametrize('rating', get_negative_rating)
    def test_get_books_with_specific_rating_negative_rating(self, collector_with_books, rating):
        # Checks that there are no books in the list with rating in [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1]
        assert len(collector_with_books.get_books_with_specific_rating(rating)) == 0

    ### METHOD get_books_rating
    def test_get_books_rating_book_list_equal(self, collector_with_books, books):
        # Checks equality of list in books_rating and source list
        assert collector_with_books.get_books_rating() == books

    ### METHOD add_book_in_favorites
    def test_add_book_in_favorites_add_existing_book_added(self, collector_with_1_book, book_1_name):
        # Checks possibility to add existing book to favorites
        collector_with_1_book.add_book_in_favorites(book_1_name)
        assert book_1_name in collector_with_1_book.get_list_of_favorites_books()
    def test_add_book_in_favorites_add_not_existing_book_not_added(self, collector_with_1_book, book_2_name):
        # Checks impossibility to add not existing book to favorites
        collector_with_1_book.add_book_in_favorites(book_2_name)
        assert book_2_name not in collector_with_1_book.get_list_of_favorites_books()
    def test_add_book_in_favorites_book_is_already_in_favorites_book_not_added(self, collector_with_1_book, book_1_name):
        # Checks impossibility to add existing in favorites book to favorites again
        collector_with_1_book.add_book_in_favorites(book_1_name)
        collector_with_1_book.add_book_in_favorites(book_1_name)
        collector_with_1_book.delete_book_from_favorites(book_1_name)
        assert book_1_name not in collector_with_1_book.get_list_of_favorites_books()

    ### METHOD delete_book_from_favorites
    def test_delete_book_from_favorites_book_deleted(self, collector_with_1_book, book_1_name):
        # Checks possibility to delete book from favorites
        collector_with_1_book.add_book_in_favorites(book_1_name)
        collector_with_1_book.delete_book_from_favorites(book_1_name)
        assert book_1_name not in collector_with_1_book.get_list_of_favorites_books()
    def test_delete_book_from_favorites_not_existing_book_not_in_list(self, collector_with_1_book, book_1_name):
        # Checks to delete not existing book from favorites, book is not in the favorites
        collector_with_1_book.delete_book_from_favorites(book_1_name)
        assert book_1_name not in collector_with_1_book.get_list_of_favorites_books()

    ### METHOD get_list_of_favorites_books
    def test_get_list_of_favorites_books_lists_are_equal(self, collector_with_books, book_1_name, book_2_name):
        # Checks equality of favorites list and list of added to favorites books
        collector_with_books.add_book_in_favorites(book_1_name)
        collector_with_books.add_book_in_favorites(book_2_name)
        list_of_favorites = [book_1_name, book_2_name]
        assert list_of_favorites == collector_with_books.get_list_of_favorites_books()