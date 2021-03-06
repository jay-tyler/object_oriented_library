'''
An object oriented libary model, done in response to a CodeFellows
'code challenge'. Three main classes modeled:
    1. books
    2. shelves - a containing class for books
    3. libraries - a containing class for shelves
'''
'''
if __name__ == "__main__":
    # this is to import and execute doctest on output at bottom
    import doctest
    doctest.testmod()
'''
class ShelfContainingMethod(object):
    '''
    This is being defined for extensibility and code-DRY-ness.
    Should another object be defined that needs to contain shelves,
    e.g. a BookMobile or Warehouse,
    then it will need to inherit this class

    Any ShelfContainingMethod should be defined with a self.shelves
    Shelf containing list in __init__.
    '''

    def create_shelf(self, books=[], name=None):
        '''
        a create shelf method. Books can be placed on the shelf when
        it's created and the new shelf is returned for assignment
        '''
        new_shelf = Shelf(books, name)
        self.shelves.append(new_shelf)
        return new_shelf

    def move_shelf(self, shelf_name, new_shelf_container):
        self.shelves.remove(shelf_name)
        new_shelf_container.shelves.append(shelf_name)      

    def __str__(self):
        message = "\nShelf-container named '%s' containing the following shelves: \
                  \n-----\n" % self.name
        books = "\n".join([str(shelf) for shelf in self.shelves])
        return message + books

    def get_number_shelves(self):
        return len(self.shelves)

    def get_number_books(self):
        n = 0
        for shelf in self.shelves:
            n += len(shelf.books)
        return n


class BookContainingMethod(object):
    '''
    This is being defined for extensibility and code-DRY-ness.
    Should another object be defined that needs to contain books,
    e.g. a BookCart or maybe a Patron,
    then it will need to inherit this class

    Any BookContainingMethod should be defined with a self.books
    Book containing list in __init__.
    '''
    def __init__(self, books=[], name=None):
        self.books = books
        self.name = name

    def create_book(self):
        '''
        aka an "enshelf" method. This one with has
        built-in book instantiation and returns the
        new book for assignment
        '''
        new_book = Book(name)
        self.books.append(new_book)
        return new_book

    def move_book(self, book_name, new_book_container):
        '''
        aka a "deshelf" method. Passes to another
        book containing object.
        '''
        self.books.remove(book_name)
        new_book_container.books.append(book_name)      

    def __str__(self):
        message = "\nBook-container named '%s' containing the following books:\
                  \n-----\n" % self.name
        books = "\n".join([str(book) for book in self.books])
        return message + books

    def get_number_books(self):
        return len(self.books)


class Library(ShelfContainingMethod):
    def __init__(self, shelves=[], name=None, address=None):
        '''For instantiation, Library optionally takes name, an address
        and a list of Shelf objects.'''
        self.shelves = shelves
        self.name = name
        self.address = address


class Shelf(BookContainingMethod):
    def __init__(self, books=[], name=None):
        '''For instantiation, Shelf optionally takes a name and a list
        of Book objects.'''
        self.books = books
        self.name = name


class Book(object):
    def __init__(self, name):
        '''In real life, an ISBN would probably be used instead of a
        name, as it can be used to look up all other attributes
        (authors, edition, etc).'''
        self.name = name

    def __repr__(self):
        return "Book({})".format(self.name)
