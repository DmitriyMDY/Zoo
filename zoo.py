# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен подклассами")

    def eat(self):
        print(f"{self.name} ест.")

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} щебечет.")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} ревет.")

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

# Функция демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} был добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} был добавлен в штат зоопарка.")

# Создание объектов животных
parrot = Bird("Попугай", 2, 25)
lion = Mammal("Лев", 5, "Золотой")
snake = Reptile("Змея", 3, "Чешуйчатый")

# Создание объектов сотрудников
zookeeper = ZooKeeper("Иван")
vet = Veterinarian("Марина")

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_staff(zookeeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Взаимодействие сотрудников с животными
zookeeper.feed_animal(parrot)
vet.heal_animal(lion)
