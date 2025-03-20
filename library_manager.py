import json

class LibraryManager:
    def __init__(self):
        self.library = []  # Initialize an empty list to store books.
        self.load_library()  # Load the library data from a file if it exists.

    def add_book(self):
        """
        Method to add a new book to the library.
        Prompts user for book details and stores the book in the library list.
        """
        print("\nAdd a New Book")
        print("================")
        title = input("Harry Potter and the Sorcerer's Stone")
        author = input("J.K. Rowling")
        
        while True:
            try:
                year = int(input("1997"))
                break
            except ValueError:
                print("1997")
        
        genre = input("Fantasy")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
        
        # Create a dictionary representing the book
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }
        
        # Add the book to the library
        self.library.append(book)
        print("\nBook added successfully!")

    def remove_book(self):
        """
        Method to remove a book from the library by title.
        """
        print("\nRemove a Book")
        print("===============")
        title = input("Harry Potter and the Sorcerer's Stone")
        for book in self.library:
            if book['title'].lower() == title.lower():
                self.library.remove(book)  # Remove the book from the library
                print("Book removed successfully!")
                return
        print("Book not found.")

    def search_book(self):
        """
        Method to search for books by title or author.
        Displays all matching books.
        """
        print("\nSearch for a Book")
        print("====================")
        search_type = input("Search by:\n1. \Harry Potter and the Sorcerer's Stone\n2. J.K. Rowling\nHarry Potter and the Sorcerer's Stone")
        matches = []
        
        if search_type == '1':
            title = input("Harry Potter and the Sorcerer's Stone")
            matches = [book for book in self.library if book['title'].lower() == title.lower()]
        elif search_type == '2':
            author = input("J.K. Rowling")
            matches = [book for book in self.library if book['author'].lower() == author.lower()]
        else:
            print("Invalid choice.")
            return

        if matches:
            print("\nMatching Books:")
            print("================")
            for index, book in enumerate(matches, 1):
                status = "Read" if book['read'] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print("No matching books found.")

    def display_books(self):
        """
        Method to display all books in the library.
        """
        if self.library:
            print("\nYour Library:")
            print("==============")
            for index, book in enumerate(self.library, 1):
                status = "Read" if book['read'] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print("Your library is empty.")

    def display_statistics(self):
        """
        Method to display statistics about the library.
        Shows total number of books and the percentage of books that have been read.
        """
        total_books = len(self.library)
        if total_books == 0:
            print("No books in the library.")
            return
        
        read_books = sum(1 for book in self.library if book['read'])
        percentage_read = (read_books / total_books) * 100
        print("\nLibrary Statistics:")
        print("====================")
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.2f}%")

    def save_library(self):
        """
        Method to save the current library to a file.
        """
        with open('library.txt', 'w') as file:
            json.dump(self.library, file)  # Save library data in JSON format
        print("Library saved to file.")

    def load_library(self):
        """
        Method to load library data from a file.
        Initializes the library with existing data if available.
        """
        try:
            with open('library.txt', 'r') as file:
                self.library = json.load(file)  # Load library data from the file
            print("Library loaded from file.")
        except FileNotFoundError:
            print("No saved library found. Starting with an empty library.")

def main():
    # Create an instance of the LibraryManager class
    manager = LibraryManager()
    
    # Pre-add a sample book: Harry Potter and the Sorcerer's Stone
    sample_book = {
        'title': "Harry Potter and the Sorcerer's Stone",
        'author': "J.K. Rowling",
        'year': 1997,
        'genre': "Fantasy",
        'read': True  # Change to False if the book is unread
    }
    manager.library.append(sample_book)  # Pre-add the sample book to the library
    
    # Run a loop to display the menu to the user
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("========================================")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        # Handle user choices
        if choice == '1':
            manager.add_book()
        elif choice == '2':
            manager.remove_book()
        elif choice == '3':
            manager.search_book()
        elif choice == '4':
            manager.display_books()
        elif choice == '5':
            manager.display_statistics()
        elif choice == '6':
            manager.save_library()  # Save the library before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
