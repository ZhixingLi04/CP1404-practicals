import csv

# Constants
UNREAD = 'u'
COMPLETED = 'c'
BOOKS_CSV_FILE = 'books.csv'


# Function to load books from CSV file
def load_books_from_csv():
    try:
        with open(BOOKS_CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []


# Function to save books to CSV file
def save_books_to_csv(books):
    with open(BOOKS_CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)


# Function to display list of books
def display_books(books):
    if not books:
        print("No books to display.")
        return

    max_title_len = max(len(book[0]) for book in books)
    max_author_len = max(len(book[1]) for book in books)

    print(f"{'Title':<{max_title_len}}  {'Author':<{max_author_len}}  Pages  Status")
    print("=" * (max_title_len + max_author_len + 14))

    unread_count = 0
    for index, book in enumerate(books):
        title, author, pages, status = book
        if status == UNREAD:
            unread_count += 1
            title = f"{title}*"
        print(f"{title:<{max_title_len}}  {author:<{max_author_len}}  {pages}  {status}")

    print(f"\nTotal books: {len(books)}, Unread books: {unread_count}")


# Function to add a new book
def add_book(books):
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    pages = input("Enter the number of pages: ")

    # Validate inputs
    if not title or not author or not pages.isdigit():
        print("Invalid input. Please enter valid details.")
        return

    new_book = [title, author, pages, UNREAD]
    books.append(new_book)
    print("Book added successfully.")


# Function to mark a book as completed
def mark_book_completed(books):
    if not any(book[3] == UNREAD for book in books):
        print("No unread books to mark as completed.")
        return

    display_books(books)  # Show current books with indices
    try:
        index = int(input("Enter the number of the book to mark as completed: ")) - 1
        if 0 <= index < len(books) and books[index][3] == UNREAD:
            books[index][3] = COMPLETED
            print(f"Marked '{books[index][0]}' by {books[index][1]} as completed.")
        else:
            print("Invalid book number or book is already completed.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Main function to control program flow
def main():
    print("Welcome to the Interactive Book List Program!")

    # Load books from CSV file
    books = load_books_from_csv()

    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Mark a book as completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            display_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            mark_book_completed(books)
        elif choice == '4':
            print("Saving your book list...")
            save_books_to_csv(books)
            print("Book list saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    main()
