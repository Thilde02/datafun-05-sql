import sqlite3

# Connect to the database (make sure your database file path is correct)
conn = sqlite3.connect('project.sqlite3')
cursor = conn.cursor()

# 1. Aggregation Query Example: Count the number of books
cursor.execute("SELECT COUNT(*) FROM books")
count_books = cursor.fetchone()
print("Total number of books:", count_books[0])

# 2. Filter Query Example: Find books published after 1950
cursor.execute("SELECT title, publication_year FROM books WHERE publication_year > 1950")
books_after_1950 = cursor.fetchall()
print("Books published after 1950:")
for book in books_after_1950:
    print(book)

# 3. Sorting Query Example: Sort books by publication year
cursor.execute("SELECT title, publication_year FROM books ORDER BY publication_year ASC")
sorted_books = cursor.fetchall()
print("Books sorted by publication year:")
for book in sorted_books:
    print(book)

# 4. Grouping Query Example: Count the number of books per author
cursor.execute("SELECT author_id, COUNT(*) FROM books GROUP BY author_id")
books_per_author = cursor.fetchall()
print("Books per author:")
for record in books_per_author:
    print(record)

# 5. Join Query Example: Get books with their author's name
cursor.execute("""
    SELECT books.title, authors.name FROM books
    INNER JOIN authors ON books.author_id = authors.author_id
""")
books_with_authors = cursor.fetchall()
print("Books with their authors:")
for record in books_with_authors:
    print(record)

# Close the connection
conn.close()
