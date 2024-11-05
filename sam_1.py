class Pomodoro:
    states = ["absent", "bloom", "green", "ripe"]
    def __init__(self, index): # Создаем сам помидор
        self._index = index # динамическое св/во
        self._state = Pomodoro.states[0] # динамическое св/во

    def grow (self): # растут помидорки
        ind_state = Pomodoro.states.index(self._state)
        if ind_state < 3:
            self._state = Pomodoro.states[ind_state + 1]

    def is_ripe (self):
        match self._state:
            case "ripe":
                return True
            case "green":
                print("The tomatoes are still green")
                return False
            case "bloom":
                print("The tomatoes bloom")
                return False
            case "absent":
                print("The tomato has not started to grow yet")
                return False

class TomatoBush: # Создаем куст с помидорами
    def __init__(self, amount):
        self._tomatoes = [] # Массив с помидорами
        for i in range (amount):
            self._tomatoes.append(Pomodoro(i)) # Заполняем массив помидорками

    def grow_all(self): # Все помидорки на кустике растут
        for i in self._tomatoes:
            i.grow() # Вызываем ф/ю роста для каждой помидорки куста из класса Pomodoro

    def all_are_ripe(self): # Проверяем, все ли помидорки на кустике выросли
        for tomato in self._tomatoes:
            if not tomato.is_ripe():  # Если хотя бы один не созрел, возвращаем False
                return False
                break
        return True  # Если все созрели, возвращаем True

    def give_away_all(self): # Собираем все помидорки с куста, если они созрели
        self._tomatoes = [] # Очистили кустик


class Gardener: # Создаем Садовника для нашего сада
    def __init__ (self, name, plant):
        self.name = name # У садовника должно быть имя (динамическое св/во)
        self._plant = plant # объект класса  TomatoBush (динамическое св/во)

    def work(self): # Задаем главную задачу садовника - растить помидорки
        self._plant.grow_all()

    def harvest(self):  # Проверка на зрелость, сбор созревшего урожая
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Помидорки в корзинке.")
        else:
            print("Ждем дозревания.")

    @staticmethod
    def knowledge_base(): # Справочка по садоводству - всем нужна (статический м/д)
        print("...Справка...")

#Тесты:
# 1) Вызовите справку по садоводству
# 2) Создайте объекты классов ТomatoBush Gardener
# 3) Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4) Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними
# 5) Соберите урожай

Gardener.knowledge_base() # 1)
bush = TomatoBush(3) # 2)
gardener = Gardener("Сергей Павлович", bush) # 3)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

