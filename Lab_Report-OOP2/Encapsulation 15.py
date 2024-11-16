class LibraryBook:
    def __init__(self, ISBN, title, author):
        
        self.ISBN = ISBN
        self._title = title
        self._author = author
        self._status = "available"


    def get_ISBN(self):
        return f"*******{self.ISBN[-4:]}"

    def borrow_book(self, borrower_name):
        if self._status == "available":
            self._status = "borrowed"
            print(f"'{self._title}' has been borrowed by {borrower_name}.")
        else:
            print(f"'{self._title}' is already borrowed.")


    def _display_basic_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class DigitalLibraryBook(LibraryBook):
    def __init__(self, isbn, title, author, file_format):
        super().__init__(isbn, title, author)
        self.file_format = file_format


    def display_digital_info(self):
        self._display_basic_info()
        print(f"File Format: {self.file_format}")


library_book = LibraryBook("01794632235", "Amar Shontan", "Ahsan Habib")


print("Masked ISBN:", library_book.get_ISBN())

library_book.borrow_book("Afjal")

library_book.borrow_book("Abdullah")

digital_book = DigitalLibraryBook("01634734834", "Amar Chelebela", "Abdullah", "PDF")

print("\nDigital Book Information:")
digital_book.display_digital_info()
