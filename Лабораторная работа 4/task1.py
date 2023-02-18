if __name__ == "__main__":
    class Avto:
        """
        Базовый класс, представляющий автомобиль.
        Атрибуты:
        brand : str Марка автомобиля.
        model : str Модель автомобиля.
        year : int Год выпуска автомобиля.
        color : str Цвет автомобиля.
        mileage : float Пробег автомобиля.
        Методы:
        get_brand() -> str: Возвращает марку автомобиля.
        get_model() -> str: Возвращает модель автомобиля.
        get_year() -> int: Возвращает год выпуска автомобиля.
        get_mileage() -> float: Возвращает пробег автомобиля.
        set_mileage(mileage: float) -> None: Устанавливает пробег автомобиля.
        __str__() -> str: Возвращает строковое представление автомобиля.
        __repr__() -> str: Возвращает строку, представляющую объект класса Avto.
        """

        def __init__(self, brand: str, model: str, year: int, color: str, mileage: float) -> None:
            self.brand = brand
            self.model = model
            self.year = year
            self.color = color
            self.mileage = mileage

        def get_brand(self) -> str:
            """
            Возвращает марку автомобиля.
            Возвращает: str Марка автомобиля.
            """
            return self.brand

        def get_model(self) -> str:
            """
            Возвращает модель автомобиля.
            Возвращает: str Модель автомобиля.
            """
            return self.model

        def get_year(self) -> int:
            """
            Возвращает год выпуска автомобиля.
            Возвращает: int Год выпуска автомобиля.
            """
            return self.year

        def get_mileage(self) -> float:
            """
            Возвращает пробег автомобиля.
            Возвращает:float Пробег автомобиля.
            """
            return self.mileage

        def set_mileage(self, mileage: int) -> None:
            """
            Устанавливает пробег автомобиля.
            Аргументы: mileage : float Новый пробег автомобиля.
            """
            self.mileage = mileage

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля.
            """
            return f"{self.year} {self.brand} {self.model} ({self.color}) with {self.mileage} km"

        def __repr__(self) -> str:
            """
            Возвращает строку, представляющую объект класса Avto.
            """
            return f"Avto('{self.brand}', '{self.model}', {self.year}, '{self.color}', {self.mileage})"


    class Truck(Avto):
        """
        Класс, представляющий грузовик.
        Атрибуты:
        - brand: марка автомобиля
        - model: модель автомобиля
        - year: год выпуска автомобиля
        - carrying_capacity: грузоподъемность грузовика
        Методы:
        - load(weight: float): загрузить грузовик заданным весом
        - unload(): разгрузить грузовик
        - __str__(): возвращает строковое представление объекта
        - __repr__() возвращает строку, которая может быть использована для создания объекта
        """

        def __init__(self, brand: str, model: str, year: int, carrying_capacity: float, color: str, milage: int):
            """
            Конструктор класса.
            brand: марка автомобиля
            model: модель автомобиля
            year: год выпуска автомобиля
            carrying_capacity: грузоподъемность грузовика
            """
            super().__init__(brand, model, year, color, milage)
            self.carrying_capacity = carrying_capacity

        def load(self, weight: float) -> str:
            """
            Загрузить грузовик заданным весом.
            weight: вес груза
            """
            if weight <= self.carrying_capacity:
                return "Грузовик загружен."
            else:
                return "Грузовик не может быть загружен, вес груза превышает грузоподъёмность грузовика."

        def unload(self) -> str:
            """
            Разгрузить грузовик.
            :return: строку с результатом попытки разгрузки грузовика
            """
            return "Грузовик разгружен."

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.
            """
            return f"{self.brand} {self.model} ({self.year}), Грузоподъёмность: {self.carrying_capacity}т"

        def __repr__(self) -> str:
            """
            Возвращает строку, которая может быть использована для создания объекта.
            :return: строку, которая может быть использована для создания объекта
            """
            return f"Truck('{self.brand}', '{self.model}', {self.year}, {self.carrying_capacity})"


    class Minivan(Avto):
        """Класс, представляющий минивэн.
        Атрибуты:
            - passengers (int): количество пассажиров, которых может вместить мультивэн.
        Методы:
            - carry_passengers: Перевозит заданное количество пассажиров.
            - move: Перемещает мультивэн.
        """

        def __init__(self, brand: str, model: str, year: int, weight: str, passengers: int, milage: int):
            """Конструктор класса Minivan.
            Аргументы:
                - make: марка автомобиля.
                - model: модель автомобиля.
                - year: год выпуска автомобиля.
                - weight: вес автомобиля в тоннах.
                - passengers: количество пассажиров, которых может вместить мультивэн.

            """
            super().__init__(brand, model, year, weight, milage)
            self.passengers = passengers

        def carry_passengers(self, num_passengers: int) -> bool:
            """Перевозит заданное количество пассажиров.
            Аргументы: num_passengers (int): количество пассажиров, которых нужно перевезти.
            Возвращает: bool: True, если пассажиры были успешно перевезены, False в противном случае.
            """
            if num_passengers <= self.passengers:
                print(f"{num_passengers} пассажиров были успешно перевезены в минивэне.")
                return True
            else:
                print("Минивэн не может перевезти такое количество пассажиров.")
                return False

        def move(self) -> str:
            """Перемещает мультивэн.
            Возвращает:str: сообщение о перемещении мультивэна.
            """
            return f"Минивэн {self.brand} {self.model} перевозит {self.passengers} пассажиров и движется по дороге."


    # Создание объектов класса Avto
    avto1 = Avto('Nissan', 'GT-R', 2018, 'red', 2000)
    avto2 = Avto('Toyota', 'Camry', 2020, 'blue', 4000)

    # Тестирование методов класса Avto
    print(avto1)  # Nissan GT-R (2018)
    print(avto2)  # Toyota Camry (2020)

    # Создание объектов класса Truck
    truck1 = Truck('Scania', 'R520', 2019, 50.0, 'red', 250000)
    truck2 = Truck('MAN', 'TGX', 2020, 40.0, 'black', 600000)

    # Тестирование методов класса Truck
    print(truck1)  # Scania R520 (2019), Грузоподъёмность: 50.0т
    print(truck2)  # MAN TGX (2020), Грузоподъёмность: 40.0т
    print(truck1.load(45.0))  # Грузовик загружен.
    print(truck1.load(60.0))  # Грузовик не может быть загружен, вес груза превышает грузоподъёмность грузовика.
    print(truck1.unload())  # Грузовик разгружен.

    # Создание объектов класса Minivan
    minivan1 = Minivan('Honda', 'Odyssey', 2021, '3500', 8, 80000)
    minivan2 = Minivan('Kia', 'Sedona', 2020, '3500', 6, 60000)

    # Тестирование методов класса Minivan
    print(minivan1)  # Honda Odyssey (2021), Вместимость: 8 человек
    print(minivan2)  # Kia Sedona (2020), Вместимость: 7 человек
    print(minivan1.carry_passengers(10))  # Введено недопустимое количество пассажиров.
    print(minivan1.move())  # Движение по дороге с .
