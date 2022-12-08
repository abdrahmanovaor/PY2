import doctest

class Book:
    def __init__(self, title:str, genre: str, pages: int):
        """

        :param genre:
        :param title:
        :param pages:

        Примеры:
        >>> book=Book("Капитанская дочка",'роман',pages=145)

        """

        if not isinstance(pages, int):
            raise TypeError (f"Не тот тип для количества страниц. Ожидается int")
        if not pages > 120:
            raise ValueError(f"Ожидается книга объемом больше 120 страниц")
        self.pages = pages

        if not isinstance(genre,str):
            raise TypeError (f"Не тот тип данных. Ожидается str")
        if genre != 'роман':
            raise ValueError(f"Ожидается роман")
        self.genre = genre
        if not isinstance(title, str)
            raise TypeError
        self.title = title

    def method_1(self) -> bool:
        """
        Функция которая проверяет является ли книга романом
        :return: Является ли книга романом
        Примеры:
        >>> book = Book("Капитанская дочка", 'повесть', 145 )
        >>> book.is_notnovel_()
        """
        ...
            if not isinstance(genre, str):
                raise TypeError
            if not genre == 'роман':
                raise ValueError (f"Ожидается роман")
            self.genre = genre
if __name__ == "__main__"
    book = Book("Капитанская дочка", genre='роман', pages=145)
    doctest.testmod()
class Building():
    """описание здания"""
    def __init__(self, street:str, number:int):
        if not isinstance(street, str):
            raise TypeError
        self.street = street
        if not isinstance(number, int)
            raise TypeError
        self.number = number
    def built(self):
        print("Здание на улице" + self.street + "№" + self.number + "построен")
    def notbuilt(self):
        if self.number > 50:
            print("Здание на улице" + self.street + "№" + self.number + "не построено")
building_ = Building("Ленина", 24)

class City():
    """описание города"""
    def __init__(self, name:str, population: int, year:int):
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(population, int)
            raise TypeError
        self.population = population
        if not isinstance(year, int)
            raise TypeError
        if year < 0
            raise ValueError
        self.year = year
    def million(self):
        if self.population >= 1000000:
            print ("город" + self.name + "миллионник")
    def age(self):
        if self.year > 2000:
            print("Город" + self.name "новый")
city1 = City("Moscow", 12600000, 1147)





