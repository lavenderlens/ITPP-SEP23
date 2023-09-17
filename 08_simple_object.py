class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# runtime code
book1 = Book("On Liberty", "Mill")
print(book1.title)
print(book1.author)
book1.author = "John Stuart Mill"
print(book1.author)

book2 = Book("The last Casualty", "Ben Elton")
book2.title = "The First Casualty"
print(book2.title)
print(book1)  # <__main__.Book object at 0x10461e250>
print(book2)  # <__main__.Book object at 0x10449c390>
