-- Create authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    birth_year INTEGER,
    nationality TEXT
);

-- Create books table with a foreign key reference to authors
CREATE TABLE IF NOT EXISTS books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    publication_year INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
);

