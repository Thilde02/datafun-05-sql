SELECT books.title, authors.name 
FROM books
INNER JOIN authors 
ON books.author_id = authors.author_id