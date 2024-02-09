class SmartPhone:
    def __init__(self, model, sim_cards, battery):
        self.model = model # Публичный атрибут
        self._battery = battery
        self.__sim_cards = sim_cards

    @property
    def sim_cards(self):
        return self.__sim_cards

    def info(self): # Публичный метод
        print(f"Бренд-{self.model}, сим карты-{self.__sim_cards}, батарейка-{self._battery}")
        self._gallery()
        # self.__password()

    def _gallery(self):
        print("Фотографии или галлерея")

    def __password(self):
        print("12345678")

    @property
    def password(self):
        return self.__password
    
mi = SmartPhone("note 10", ["MegaCom", "O!"], "500 Mach")
# mi.info()
# mi._gallery()
mi.password()
print(mi.model)
print(mi._battery)
print(mi.sim_cards)


# def private(value):
#     def test():

#         print("Hello world!")
#         value()
#         print("Bye!")

#     return test



# @private
# def hello():
#     print("WTF!!!")

# hello()