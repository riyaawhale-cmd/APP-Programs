from book import Book
from user import User

# ===============================
# Transaction Class
# ===============================
class Transaction:

    def __init__(self):
        self.users = []
        self.books = []

    # --------------------------
    # Add User
    # --------------------------
    def add_user(self):

        user_id = input("Enter User ID : ")
        name = input("Enter Name : ")
        email = input("Enter Email : ")

        user = User(user_id, name, email)
        self.users.append(user)

        print("\nUser Added Successfully\n")

    # --------------------------
    # Add Book
    # --------------------------
    def add_book(self):

        book_id = input("Enter Book ID : ")
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")
        publisher = input("Enter Publisher : ")
        version = input("Enter Version : ")

        book = Book(book_id, title, author, publisher, version)
        self.books.append(book)

        print("\nBook Added Successfully\n")

    # --------------------------
    # Show Users
    # --------------------------
    def show_users(self):

        if len(self.users) == 0:
            print("No Users Found\n")
            return

        for user in self.users:
            user.display()

    # --------------------------
    # Show Books
    # --------------------------
    def show_books(self):

        if len(self.books) == 0:
            print("No Books Available\n")
            return

        for book in self.books:
            book.display()

    # --------------------------
    # Search Book
    # --------------------------
    def search_book(self):

        title = input("Enter Book Title : ")

        for book in self.books:
            if book.title.lower() == title.lower():
                book.display()
                return

        print("Book Not Found\n")

    # --------------------------
    # Issue Book
    # --------------------------
    def issue_book(self):

        user_id = input("Enter User ID : ")
        book_id = input("Enter Book ID : ")

        user_found = None
        book_found = None

        for user in self.users:
            if user.user_id == user_id:
                user_found = user
                break

        for book in self.books:
            if book.book_id == book_id:
                book_found = book
                break

        if user_found is None:
            print("User Not Found\n")
            return

        if book_found is None:
            print("Book Not Found\n")
            return

        if book_found.available:
            book_found.available = False
            book_found.issued_to = user_id
            print(f"\nBook Issued Successfully to {user_found.name}\n")
        else:
            print("Book Already Issued\n")

    # --------------------------
    # Return Book
    # --------------------------
    def return_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    print("Returned by User ID :", book.issued_to)
                    book.available = True
                    book.issued_to = None
                    print("Book Returned Successfully\n")
                else:
                    print("Book Already Available\n")

                return

        print("Book Not Found\n")

    # --------------------------
    # Update User
    # --------------------------
    def update_user(self):

        user_id = input("Enter User ID to Update : ")

        for user in self.users:

            if user.user_id == user_id:

                user.name = input("Enter New Name : ")
                user.email = input("Enter New Email : ")

                print("\nUser Updated Successfully\n")
                return

        print("User Not Found\n")

    # --------------------------
    # Update Book
    # --------------------------
    def update_book(self):

        book_id = input("Enter Book ID to Update : ")

        for book in self.books:

            if book.book_id == book_id:

                book.title = input("Enter New Title : ")
                book.author = input("Enter New Author : ")
                book.publisher = input("Enter New Publisher : ")
                book.version = input("Enter New Version : ")

                print("\nBook Updated Successfully\n")
                return

        print("Book Not Found\n")

    # --------------------------
    # Display Issued Books
    # --------------------------
    def display_issued_books(self):

        found = False

        for book in self.books:

            if not book.available:

                user_name = "Unknown"

                for user in self.users:
                    if user.user_id == book.issued_to:
                        user_name = user.name
                        break

                print("\n----------------------------")
                print("Book ID     :", book.book_id)
                print("Title       :", book.title)
                print("Author      :", book.author)
                print("Publisher   :", book.publisher)
                print("Version     :", book.version)
                print("Issued To   :", user_name)
                print("User ID     :", book.issued_to)
                print("----------------------------")

                found = True

        if not found:
            print("No Books Issued\n")


# ===============================
# Main Program
# ===============================

library = Transaction()

while True:

    print("\n========== Library Management ==========")
    print("1. Add User")
    print("2. Add Book")
    print("3. Show Users")
    print("4. Show Books")
    print("5. Search Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Update User")
    print("9. Update Book")
    print("10. Display Issued Books")
    print("11. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        library.add_user()

    elif choice == "2":
        library.add_book()

    elif choice == "3":
        library.show_users()

    elif choice == "4":
        library.show_books()

    elif choice == "5":
        library.search_book()

    elif choice == "6":
        library.issue_book()

    elif choice == "7":
        library.return_book()

    elif choice == "8":
        library.update_user()

    elif choice == "9":
        library.update_book()

    elif choice == "10":
        library.display_issued_books()

    elif choice == "11":
        print("Thank You...")
        break

    else:
        print("Invalid Choice")