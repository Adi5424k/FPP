class menu:
    def __init__(self):
        self.dishes = {}
    def add(self, dish, price):
        self.dishes[dish] = price
    def __add__(self, item):
        self.dishes[item[0]] = item[1]
        return self
    def __setitem__(self, dish, price):
        self.dishes[dish] = price
    def __getitem__(self, item):
        return self.dishes[item]
    def show(self):
        for k,v  in self.dishes.items():
            print(f'{k} {v}')