'''
An object oriented libary model, done in response to a CodeFellows
'code challenge'. Three main classes modeled:
    1. books
    2. shelves - a containing class for books
    3. libraries - a containing class for shelves
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

    def move_book(self):
        '''
        aka a "deshelf" method. Passes to another
        book containing object.
        '''
        pass

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

# separately instantiating books
book1 = Book("The tides of darkness")
book2 = Book("The near side of the moon")
book3 = Book("The last book you'd ever read")
books = [book1, book2, book3]

# shoving those books into a new shelf instance assigned to my_shelf
my_shelf = Shelf(books, "My shelf")

# shoving my_shelf into a new library instance
my_library = Library([my_shelf], "T-town Library", "1234 E. Miles St.")

# printing books, my_shelf using defined __repr__ and __str__
print books
print my_shelf
print my_library

# using book and shelf counting methods
print "*****number of shelves in new_library: ***** ", my_library.get_number_shelves()
print "*****number of books in new_library: ***** ", my_library.get_number_books()
print "*****number of books in my_shelf: ***** ", my_shelf.get_number_books()

# expanding the library by calling its create_shelf method
another_shelf = my_library.create_shelf([Book("A book for a new shelf")],
                                         "brand new expansion shelf")

# printing the library again using __str__
print my_library

# using the counting methods again
print "*****number of shelves in new_library: ***** ", my_library.get_number_shelves()
print "*****number of books in new_library: ***** ", my_library.get_number_books()
print "*****number of books in my_shelf: ***** ", my_shelf.get_number_books()
print "*****number of books in another_shelf: ***** ", another_shelf.get_number_books()

# creating a new library and then moving another_shelf to it
new_library = Library(name="L-town Library", address="9876 W. Highland Blvd.")
my_library.move_shelf(another_shelf, new_library)
print "*****my library, printed: ***** ", my_library
print "*****new library, printed: *****", new_library
