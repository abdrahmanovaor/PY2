class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super(Book, self).__init__(name, author)
        self._name = name
        self._author = author
        self.pages = pages

    def __str__(self):
        super(Book, self).__str__()
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super(Book,self).__init__(name, author)
        self._name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        super(Book,self).__str__()
        return f"Книга {self.name}. Автор {self.author}"

