class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return list(set([c.book for c in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([c.royalties for c in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return list(set([c.author for c in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validation for instances and types
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]