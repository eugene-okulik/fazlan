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


class Chrysanthemum(Flowers):
    def __init__(self, name, fresh, color, stem_length, price, life_time, is_lush):
        super().__init__(name, fresh, color, stem_length, price, life_time)
        self.is_lush = is_lush


class Tulips(Flowers):
    def __init__(self, name, fresh, color, stem_length, price, life_time, ):
        super().__init__(name, fresh, color, stem_length, price, life_time)


class Bouquet:

    def __init__(self):
        self.flowers = []

    def append(self, flower):
        self.flowers.append(flower)

    def calculate_bouquet_price(self):
        prices = map(lambda flower: flower.price, self.flowers)
        return sum(prices)

    def calculate_avg_fading_time(self):
        life_times = map(lambda flower: flower.life_time, self.flowers)
        return round((sum(life_times) / len(self.flowers)), 2)

    def sort_flowers_by_fresh(self):
        return sorted(self.flowers, key=lambda fresh: fresh.fresh)

    def sort_flowers_by_color(self):
        return sorted(self.flowers, key=lambda color: color.color, reverse=True)

    def sort_flowers_by_stem_length(self):
        return sorted(self.flowers, key=lambda stem_length: stem_length.stem_length)

    def sort_flowers_by_price(self):
        return sorted(self.flowers, key=lambda price: price.price, reverse=True)

    def search_flowers_by_life_time(self):
        avg_life_time = self.calculate_avg_fading_time()
        fresh_flowers = []
        for flower in self.flowers:
            if flower.life_time <= avg_life_time:
                fresh_flowers.append(flower)
        return fresh_flowers


flower_1 = Rose('Цветок_1', 4, 'синий', 87, 170, 2, True)
flower_2 = Rose('Цветок_2', 3, 'фиолетовый', 73, 350, 4, False)
flower_3 = Chrysanthemum('Цветок_3', 2, 'красный', 100, 99, 1, True)
flower_4 = Chrysanthemum('Цветок_4', 1, 'желтый', 85, 150, 3, True)
flower_5 = Tulips('Цветок_5', 1, 'зеленый', 50, 180, 3)
flower_6 = Tulips('Цветок_6', 5, 'белый', 60, 100, 4.5)

bouquet = Bouquet()

bouquet.append(flower_1)
bouquet.append(flower_2)
bouquet.append(flower_3)
bouquet.append(flower_4)
bouquet.append(flower_5)
bouquet.append(flower_6)

print(bouquet.calculate_bouquet_price())
print(bouquet.calculate_avg_fading_time())
print(bouquet.sort_flowers_by_fresh())
print(bouquet.sort_flowers_by_color())
print(bouquet.sort_flowers_by_stem_length())
print(bouquet.sort_flowers_by_price())
print(bouquet.search_flowers_by_life_time())
