'''
An object oriented libary model, done in response to a CodeFellows
'code challenge'. Three main classes modeled:
    1. books
    2. shelves - a containing class for books
    3. libraries - a containing class for shelves
    
This particular file is meant to be run with doctest from the command line using:
>>> python -m doctest doctest_from_command_line.py

Two tests will fail (i.e. I've used a nested representation for library, which 
doctest doesn't expect). All other tests will pass.
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
        message = "Shelf-container named '%s' containing the following shelves: \
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
        message = "Book-container named '%s' containing the following books:\
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


def tests():
    """
    Example output
    ==============
    
    # Let's instantiate some books
    >>> book1 = Book("The tides of darkness")
    >>> book2 = Book("The near side of the moon")
    >>> book3 = Book("The last book you'd ever read")
    
    # Checking the representation of one of these books
    >>> print book1
    Book(The tides of darkness)
    
    # Bundle our books together
    >>> books = [book1, book2, book3]
    
    # And shove our bundled books into a new shelf instance
    >>> my_shelf = Shelf(books, "My first shelf")
    
    # Check the representation of the shelf
    >>> print my_shelf
    Book-container named 'My first shelf' containing the following books:                  
    -----
    Book(The tides of darkness)
    Book(The near side of the moon)
    Book(The last book you'd ever read)
    
    # And shove my_shelf into a new library instance
    >>> my_library = Library([my_shelf], "T-town Library", "1234 E. Miles St.")
    
    # Check the representation of my_library
    >>> print my_library
    Shelf-container named 'T-town Library' containing the following shelves:                   
    -----
    
    Book-container named 'My first shelf' containing the following books:                  
    -----
    Book(The tides of darkness)
    Book(The near side of the moon)
    Book(The last book you'd ever read)
    '''
    
    # expanding the library by calling its create_shelf method
    >>> another_shelf = my_library.create_shelf([Book("A book for a new shelf")], "brand new expansion shelf")
    
    # printing the library again
    >>> print my_library
    Shelf-container named 'T-town Library' containing the following shelves:                   
    -----
    
    Book-container named 'My first shelf' containing the following books:                  
    -----
    Book(The tides of darkness)
    Book(The near side of the moon)
    Book(The last book you'd ever read)
    
    Book-container named 'Expansion shelf' containing the following books:                  
    -----
    Book(A book for a new shelf)
    '''
    
    # using counting methods for library, shelf
    >>> my_library.get_number_books()
    4
    >>> my_library.get_number_shelves()
    2
    >>> my_shelf.get_number_books()
    3
    >>> another_shelf.get_number_books()
    1
    
    # pass a book from my_shelf to another_shelf
    >>> my_shelf.move_book(book3, another_shelf)
    
    # check books list for both my_shelf and another_shelf
    >>> my_shelf.books
    [Book(The tides of darkness), Book(The near side of the moon)]
    >>> another_shelf.books
    [Book(A book for a new shelf), Book(The last book you'd ever read)]
    
    # instantiate a new library
    >>> another_library = Library(name="L-town Library", address="9876 W. Highland Blvd.")
    
    # pass another_library another_shelf
    >>> my_library.move_shelf(another_shelf, another_library)
    
    # check number of books in each library
    >>> my_library.get_number_books()
    2
    >>> another_library.get_number_books()
    2
    """

