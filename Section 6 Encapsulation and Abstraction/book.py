class Book:
     
        def __init__(self, title, author, num_pages, ISBN, publisher):
    	    self.title = title
    	    self.author = author
    	    self._num_pages = num_pages
    	    self._ISBN = ISBN
    	    self._publisher = publisher


my_book = Book('metamorphosis', 'kafka', 100, 6677679919, True)
print(my_book._title)


