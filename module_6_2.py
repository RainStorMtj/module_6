class Vehicle:
    __COLOR_VARIANTS = ['Чёрный', 'Белый', 'Красный', 'Розовый', 'Жёлтый']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.title() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Федя', 'Toyota Mark II', '500', 'Белый')
vehicle1.print_info()

vehicle1.set_color('Фиолетовый')
vehicle1.set_color('жёлтый')
vehicle1.owner = 'Вася'
vehicle1.print_info()