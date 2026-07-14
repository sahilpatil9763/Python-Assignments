"""
Write a Python program to implement a class named Bookstore with the following specifications:
• The class should contain two instance variables:
    • Name (Book Name)
    • Author (Book Author)
• The class should contain one class variable:
    • NoOfBooks (initialize it to 0)
• Define a constructor (_init_) that accepts Name and Author and initializes instance variables.
• Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
• Implement an instance method:
    • Display () - should display book details in the format:
      <BookName> by <Author>. No of books: <NoOfBooks>

      Example usage:

Obj1 = Bookstore("Linux System Programming","Robert Love")
Obj1.Display()  # Linux System Programming by Robert Love. No of books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # C Programming by Dennis Ritchie. No of books: 2
"""

class BookStore:
    
    # Class Variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1

    # Instance Method
    def Display(self):
        print(f"{self.Name} by {self.Author}, No of boooks : {BookStore.NoOfBooks}")

# Object Creation
Obj1 = BookStore("Linux System Programming","Robert Love")
Obj1.Display()  # Linux System Programming by Robert Love. No of books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # C Programming by Dennis Ritchie. No of books: 2