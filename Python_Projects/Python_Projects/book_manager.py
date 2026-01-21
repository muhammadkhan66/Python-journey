# Define a class called Book
class Book:
    # The constructor method to initialize a book object
    def __init__(self, title, author, pages):
        self.title = title      # Store the book's title
        self.author = author    # Store the book's author
        self.pages = pages      # Store the number of pages in the book

# Create an empty list to store multiple book objects
book = []

# Ask the user how many books they want to enter
num_of_book = input("Enter the number of books you want to enter: ")

# Loop for the number of books specified by the user
for i in range(int(num_of_book)):
    print(f"Entering book: {i+1}\n")  # Show which book is being entered
    
    # Ask the user to enter details of the book
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    pages = input("Enter the no. of pages of the book: ")
    
    # Create a new Book object with the entered details
    books = Book(title, author, pages)
    
    # Add the created Book object to the list
    book.append(books)

# Print all the books entered
print("Books\n")
for b in book:
    print(f"Title: {b.title} | Author: {b.author} | pages: {b.pages}\n")
