import sqlite3

# Step 1: Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 2: Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        status TEXT DEFAULT 'Available'
    )
''')
conn.commit()

# Step 3: Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    print("✅ Book added successfully!\n")

# Step 4: Display all books
def display_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("\n📚 All Books:")
    print("-" * 40)
    for book in books:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {book[3]}")
    print("-" * 40 + "\n")

# Step 5: Issue a book
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row and row[0] == 'Available':
        cursor.execute("UPDATE books SET status = 'Issued' WHERE id = ?", (book_id,))
        conn.commit()
        print("✅ Book issued successfully!\n")
    else:
        print("❌ Book is either already issued or ID is invalid.\n")

# Step 6: Return a book
def return_book():
    book_id = input("Enter Book ID to return: ")
    cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row and row[0] == 'Issued':
        cursor.execute("UPDATE books SET status = 'Available' WHERE id = ?", (book_id,))
        conn.commit()
        print("✅ Book returned successfully!\n")
    else:
        print("❌ Book is not issued or ID is invalid.\n")

# Step 7: Delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    print("🗑 Book deleted successfully!\n")

# Step 8: Main menu
def main():
    while True:
        print("📚 Library Management Menu")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("👋 Exiting. Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Step 9: Entry point
if __name__ == "__main__":
    main()
    conn.close()