class Book:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print(f'"{book}" added successfully.')

    def show_book(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)

    def add_user(self):
        user = input("Enter user name: ")
        self.users.append(user)
        print(f"{user} added successfully.")

    def show_user(self):
        if len(self.users) == 0:
            print("No users found.")
        else:
            print("\nUsers:")
            for user in self.users:
                print("-", user)

    def remove_user(self):
        user = input("Enter user name to remove: ")
        if user in self.users:
            self.users.remove(user)
            print(f"{user} removed successfully.")
        else:
            print("User not found.")

    def exist_user(self):
        user = input("Enter user name: ")
        if user in self.users:
            print("User exists.")
        else:
            print("User does not exist.")

    def return_book(self):
        book = input("Enter book name to return: ")
        self.books.append(book)
        print(f'"{book}" returned successfully.')


class Main:
    def run(self):
        library = Book()

        while True:
            print("\n===== Library Menu =====")
            print("1. Add Book")
            print("2. Show Books")
            print("3. Add User")
            print("4. Show Users")
            print("5. Remove User")
            print("6. Check User Exists")
            print("7. Return Book")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.show_book()
            elif choice == "3":
                library.add_user()
            elif choice == "4":
                library.show_user()
            elif choice == "5":
                library.remove_user()
            elif choice == "6":
                library.exist_user()
            elif choice == "7":
                library.return_book()
            elif choice == "8":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = Main()
    app.run()