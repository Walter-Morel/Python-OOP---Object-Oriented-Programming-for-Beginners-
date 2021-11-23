class MyEditorialBook:
    
    has_cover = True
    editorial_code = 39012
    
    def __init__(self, title, num_pages, published):
        self.title = title
        self.num_pages = num_pages
        self.published = published


my_book = MyEditorialBook('The Metamorphosis', 100, 1915)
MyEditorialBook.has_cover = False
MyEditorialBook.editorial_code = 99865
print('Title: {} Num pages: {} Published: Cover: {} Editorial Code: {}'.format(my_book.title, my_book.num_pages, MyEditorialBook.has_cover, MyEditorialBook.editorial_code))