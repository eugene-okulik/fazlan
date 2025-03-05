class Book:
    page_material = 'бумага'
    is_text = True

    def __init__(self, book_name, author, page_number, isbn, is_reserved=None):
        self.book_name = book_name
        self.author = author
        self.page_number = page_number
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_book_details(self):
        if self.is_reserved:
            print(f'Название: {self.book_name}, Автор: {self.author},'
                  f' cтраниц: {self.page_number}, материал: {self.page_material},'
                  f' зарезервирована')
        else:
            print(f'Название: {self.book_name}, Автор: {self.author},'
                  f' cтраниц: {self.page_number}, материал: {self.page_material}')


book_1 = Book('Идиот', 'Достоевский', 500, '978-5-699-12014-7')
book_2 = Book('Проект феникс', 'Ким', 384, '996-114-7')
book_3 = Book('Алхимик', 'Коэльо', 221, '5-532-1201', True)
book_4 = Book('Последняя лекция', 'Пауш', 288, '978-5-04-110903-5')
book_5 = Book('Девушка с татуировкой дракона', 'Ларссон', 576, '978-5-699-83619-2')

book_1.print_book_details()
book_2.print_book_details()
book_3.print_book_details()
book_4.print_book_details()
book_5.print_book_details()
print()


class SchoolBook(Book):
    def __init__(self, book_name, author, page_number, isbn, subject, school_class, is_exercise, is_reserved=None):
        super().__init__(book_name, author, page_number, isbn)
        self.subject = subject
        self.school_class = school_class
        self.is_exercise = is_exercise
        self.is_reserved = is_reserved  # как по-другому можно было реализовать?

    def print_schoolbook_details(self):
        if self.is_reserved:
            print(f'Название: {self.book_name}, Автор: {self.author},'
                  f' cтраниц: {self.page_number}, предмет: {self.subject},'
                  f' класс: {self.school_class}, зарезервирована')
        else:
            print(f'Название: {self.book_name}, Автор: {self.author},'
                  f' cтраниц: {self.page_number}, предмет: {self.subject},'
                  f' класс: {self.school_class}')


schoolbook_1 = SchoolBook('Алгебра', 'Аристотель', 200, '35-35322-11201', 'Математика', 9, True, True)
schoolbook_2 = SchoolBook('Геометрия', 'Петров', 777, '992-111-24', 'Математика', 8, True)
schoolbook_3 = SchoolBook('Художественная литература', 'Пушкин', 200, '821-3522', 'Литература', 10, False)
schoolbook_4 = SchoolBook('Законы инерции', 'Ньютон', 666, '123-70978-99', 'Физика', 11, False)
schoolbook_5 = SchoolBook('Занимательные реакции', 'Менделеев', 69, '53-124-642', 'Химия', 7, True)

schoolbook_1.print_schoolbook_details()
schoolbook_2.print_schoolbook_details()
schoolbook_3.print_schoolbook_details()
schoolbook_4.print_schoolbook_details()
schoolbook_5.print_schoolbook_details()
