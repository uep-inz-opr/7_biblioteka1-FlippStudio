class Book:

    def __init__(self, book_title, author, year):
        self.title = book_title
        self.author = author
        self.year = year
        self.quantity = 1

    def __repr__(self):
        return "'" + self.author + "', " + str(self.quantity)


books = {}
n = input()
for i in range(int(n)):
    temp = eval(input())
    title = temp[0].strip()
    author = temp[1].strip()
    year = temp[2]
    if title in books:
        books[title].quantity += 1
    else:
        books[title] = Book(title, author, year)

sorted_books = sorted(books.items())

for book in sorted_books:
    print(book)

