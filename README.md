<p align="center">
    <img src="https://cdn1.iconfinder.com/data/icons/cybercrime-internet-security/33/antivirus-06-1024.png" alt="qa_python" width="165" height="165">
</p>

<h3 align="center">Sprint 2</h3>

## qa_python

Pytest training. Writing unit tests.

## List of tests

[method add_new_book](#method_add_new_book)
- [test_add_new_book_add_two_books](#test_add_new_book_add_two_books) (default)
- [test_add_new_book_add_default_rating_equal_1](#test_add_new_book_add_default_rating_equal_1)
- [test_add_new_book_add_two_equal_books_added_one](#test_add_new_book_add_two_equal_books_added_one)

[method set_book_rating](#method_set_book_rating)
- [test_set_book_rating_to_not_existing_book_rating_none](#test_set_book_rating_to_not_existing_book_rating_none)
- [test_set_book_rating_negative_rating](#test_set_book_rating_negative_rating)
- [test_set_book_with_rating_1_get_rating_1](#test_set_book_rating_1_rating_1)
- [test_set_book_rating_positive_rating](#test_set_book_rating_positive_rating)

[method get_book_rating ](#method_get_book_rating)
- [test_get_book_rating_existing_book_rating_1](#test_get_book_rating_existing_book_rating_1)
- [test_get_book_rating_not_existing_book_rating_none](#test_get_book_rating_not_existing_book_rating_none)

[method get_books_with_specific_rating ](#method_get_books_with_specific_rating)
- [test_get_books_with_specific_rating_positive_rating](#test_get_books_with_specific_rating_positive_rating)
- [test_get_books_with_specific_rating_negative_rating](#test_get_books_with_specific_rating_negative_rating)

[method get_books_rating ](#method_get_books_rating)
- [test_get_books_rating_book_list_equal](#test_get_books_rating_book_list_equal)
 
[method add_book_in_favorites ](#method_add_book_in_favorites)
- [test_add_book_in_favorites_add_existing_book_added](#test_add_book_in_favorites_add_existing_book_added)
- [test_add_book_in_favorites_add_not_existing_book_not_added](#test_add_book_in_favorites_add_not_existing_book_not_added)
- [test_add_book_in_favorites_book_is_already_in_favorites_book_not_added](#test_add_book_in_favorites_book_is_already_in_favorites_book_not_added)

[method delete_book_from_favorites ](#method_delete_book_from_favorites)
- [test_delete_book_from_favorites_book_deleted](#test_delete_book_from_favorites_book_deleted)
- [test_delete_book_from_favorites_not_existing_book_not_in_list](#test_delete_book_from_favorites_not_existing_book_not_in_list)
 
[method get_list_of_favorites_books  ](#method_get_list_of_favorites_books )
- [test_get_list_of_favorites_books_lists_are_equal](#test_get_list_of_favorites_books_lists_are_equal)
 
## method_add_new_book

### test_add_new_book_add_two_books

Checks possibility to add two books to "books_rating" dictionary

### test_add_new_book_add_default_rating_equal_1

Checks that new book has default rating = 1

### test_add_new_book_add_two_equal_books_added_one

Checks impossibility to add two books to "books_rating" dictionary with the same name

## method_set_book_rating

### test_set_book_rating_to_not_existing_book_rating_none

Checks if an not existing book can't be rated

### test_set_book_rating_negative_rating

Checks if the new rating is in [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1] the rating won't be changed (default 1)

### test_set_book_with_rating_1_get_rating_1

Checks if the new rating 1, change rating to 5 than to 1. The rating will be changed to 1

### test_set_book_rating_positive_rating

Checks if the new rating is in [2, 5, 9, 10] the rating will be changed to [2, 5, 9, 10]

## method_get_book_rating

### test_get_book_rating_existing_book_rating_1

Checks possibility to get the rating of existing book

### test_get_book_rating_not_existing_book_rating_none

Checks impossibility to get the rating of not existing book

## method_get_books_with_specific_rating 

### test_get_books_with_specific_rating_positive_rating

Checks possibility to get the list with rating in range 1-10

### test_get_books_with_specific_rating_negative_rating

Checks that there are no books in the list with rating in [-100, -1, 0, 11, 12, 100, None, '"%^$#', 'undefined', '', 2.1]

## method_get_books_rating 

### test_get_books_rating_book_list_equal

Checks equality of list in books_rating and source list

## method_add_book_in_favorites

### test_add_book_in_favorites_add_existing_book_added

Checks possibility to add existing book to favorites

### test_add_book_in_favorites_add_not_existing_book_not_added

Checks impossibility to add not existing book to favorites

### test_add_book_in_favorites_book_is_already_in_favorites_book_not_added

Checks impossibility to add existing in favorites book to favorites again

## method_delete_book_from_favorites

### test_delete_book_from_favorites_book_deleted

Checks possibility to delete book from favorites

### test_delete_book_from_favorites_not_existing_book_not_in_list

Checks to delete not existing in favorites book from favorites, book is not in the favorites

## method_get_list_of_favorites_books 

### test_get_list_of_favorites_books_lists_are_equal

Checks equality of favorites list and list of added to favorites books


## Installation pytest

pip install pytest

## start tests

pytest -v tests.py 