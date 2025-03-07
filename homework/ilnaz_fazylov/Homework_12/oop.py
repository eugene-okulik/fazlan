class Flowers:
    def __init__(self, name, fresh, color, stem_length, price, life_time):
        self.name = name
        self.fresh = fresh
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Rose(Flowers):
    def __init__(self, name, fresh, color, stem_length, price, life_time, is_torny):
        super().__init__(name, fresh, color, stem_length, price, life_time)
        self.is_torny = is_torny


flower_1 = Rose('Цветок_1', 4, 'синий', 87, 250, 2, True)
flower_2 = Rose('Цветок_2', 3, 'фиолетовый', 73, 240, 4, False)


class Chrysanthemum(Flowers):
    def __init__(self, name, fresh, color, stem_length, price, life_time, is_lush):
        super().__init__(name, fresh, color, stem_length, price, life_time)
        self.is_lush = is_lush


flower_3 = Chrysanthemum('Цветок_3', 2, 'красный', 100, 260, 1, True)
flower_4 = Chrysanthemum('Цветок_4', 1, 'желтый', 85, 200, 3, True)


class Tulips(Flowers):
    def __init__(self, name, fresh, color, stem_length, price, life_time, ):
        super().__init__(name, fresh, color, stem_length, price, life_time)


flower_5 = Tulips('Цветок_5', 1, 'зеленый', 50, 180, 3)
flower_6 = Tulips('Цветок_6', 5, 'белый', 60, 195, 4.5)


class Bouquet:
    bouquet = [flower_1, flower_2, flower_3, flower_4, flower_5, flower_6]

    def __init__(self):
        self.price = self.calculate_bouquet_price()

    def calculate_bouquet_price(self, price=0):
        for flower in self.bouquet:
            price += flower.price
        return price

    def calculate_avg_fading_time(self, fading_time=0):
        for flower in self.bouquet:
            fading_time += flower.life_time
        return round((fading_time / len(self.bouquet)), 2)

    def sort_flowers_by_fresh(self):
        for i in range(len(self.bouquet) - 1):
            for j in range(len(self.bouquet) - 1 - i):
                if self.bouquet[j].fresh > self.bouquet[j + 1].fresh:
                    self.bouquet[j], self.bouquet[j + 1] = self.bouquet[j + 1], self.bouquet[j]
        return self.bouquet

    def sort_flowers_by_color(self):
        new_bouquet = []  # есть еще варианты без доп списка отсортировать?
        for i in range(len(self.bouquet)):
            if self.bouquet[i].color == 'фиолетовый':
                new_bouquet.insert(0, self.bouquet[i])
            elif self.bouquet[i] == 'желтый':
                new_bouquet.insert(1, self.bouquet[i])
            elif self.bouquet[i].color == 'красный':
                new_bouquet.insert(2, self.bouquet[i])
            else:
                new_bouquet.append(self.bouquet[i])
        return new_bouquet

    def sort_flowers_by_stem_length(self):
        for i in range(len(self.bouquet) - 1):
            for j in range(len(self.bouquet) - 1 - i):
                if self.bouquet[j].stem_length < self.bouquet[j + 1].stem_length:
                    self.bouquet[j], self.bouquet[j + 1] = self.bouquet[j + 1], self.bouquet[j]
        return self.bouquet

    def sort_flowers_by_price(self):
        for i in range(len(self.bouquet) - 1):
            for j in range(len(self.bouquet) - 1 - i):
                if self.bouquet[j].price > self.bouquet[j + 1].price:
                    self.bouquet[j], self.bouquet[j + 1] = self.bouquet[j + 1], self.bouquet[j]
        return self.bouquet

    def search_flowers_by_life_time(self):
        avg_life_time = self.calculate_avg_fading_time()
        fresh_flowers = []
        for flower in self.bouquet:
            if flower.life_time <= avg_life_time:
                fresh_flowers.append(flower)
        return fresh_flowers


c = Bouquet()
print(c.price)
print(c.calculate_avg_fading_time())
print(c.sort_flowers_by_fresh())
print(c.sort_flowers_by_color())
print(c.sort_flowers_by_stem_length())
print(c.sort_flowers_by_price())
print(c.search_flowers_by_life_time())
