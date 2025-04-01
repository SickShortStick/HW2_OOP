
class Food:
    food_id = 0
    name: str
    food_price = 0

    def __init__(self):
        self.food_id = Food.food_id
        Food.food_id += 1

    def calculate_price(self):
        pass

    def __add__(self, other_food):
        return self.food_price + other_food.food_price

    def __mul__(self, number: int):
        return self.food_price * number
        

class Pizza(Food):
    
    sizes = {
        'Small' : 8,
        'Medium': 12,
        'Large' : 16
    }
    current_size: str


    variation = {'Margherita', 'Pepperoni'}
    current_variation: str

    toppings = {
        'Olives' : 1,
        'Sauce' : 1.5,
        'Cheese' : 2
    }
    extras: list

    def __init__(self, size, variation, extras: list):
        super().__init__()
        self.name = 'Pizza'
        self.current_size = size
        self.current_variation = variation
        self.extras = extras
        self.calculate_price()

    def calculate_price(self):
        toppings_price = 0
        for extra in self.extras:
            extra = extra.split()[-1]
            toppings_price += Pizza.toppings[extra]
        self.food_price = Pizza.sizes[self.current_size] + toppings_price
        return self.food_price
    
class Burger(Food):

    meat_layers = {
            'Single' : 6,
            'Double' : 9,
            'Triple' : 12
    }

    current_meat_layer: str

    buns = {
        'Reqular' : 1,
        'Seasame' : 2,
        'Brioche' : 3
    }
    
    current_bun: str

    extras = {
        'Cheese' : 1,
        'Egg' : 1.5,
        'Bacon' : 2
    }

    current_extras: list

    def __init__(self, meat_layers: str, bun: str, extras: list):
        super().__init__()
        self.name = 'Burger'
        self.current_meat_layer = meat_layers
        self.current_bun = bun
        self.current_extras = extras
        self.calculate_price()

    def calculate_price(self):
        extras_price = 0
        for extra in self.extras:
            extras_price += Burger.extras[extra]
        self.food_price = Burger.buns[self.current_bun] + Burger.meat_layers[self.current_meat_layer] + extras_price
        return self.food_price
    
class Drink(Food):
    
    volumes = {
        '300ml' : 2,
        '500ml' : 3,
        '1L' : 5
    }

    current_volume: str

    variation = {
        'Soda',
        'Juice',
        'Water'
    }

    current_variation: str

    def __init__(self, volume, variation):
        super().__init__()
        self.name = 'Drink'
        self.current_volume = volume
        self.current_variation = variation
        self.calculate_price()

    def calculate_price(self):
        self.food_price = Drink.volumes[self.current_volume]
        return self.food_price

class Order:

    items = {}

    discounts = {
        'DISCOUNT10' : 0.9,
        'DISCOUNT20' : 0.8
    }

    total_price = 0
    discounted_total_price = 0

    def __init__(self):
        pass

    def add_item(self, food: Food, quantity: int):
        self.items[food] = quantity

    def remove_item(self, food_id: int):
        for food in self.items.keys():
            if food.food_id == food_id:
                self.items.pop(food)
                return 0

    def calculate_total(self):
        for food in self.items.items():
            self.total_price += food[0] * food[1]
        return self.total_price

    def apply_discount(self, code: str):
        if code in self.discounts:
            self.discounted_total_price = self.total_price * self.discounts[code]
        return self.discounted_total_price

    def display_order(self):
        print('Order Summary:')
        for food, quantity in self.items.items():
            match food.name:
                case 'Burger':
                    print(f'{quantity}x {food.current_meat_layer} Burger with {food.current_bun} (ID: {food.food_id}) - ${food.food_price} each')
                case 'Pizza':
                    print(f'{quantity}x {food.current_size} {food.current_variation} (ID: {food.food_id}) - ${food.food_price} each')
                case 'Drink':
                    print(f'{quantity}x {food.current_volume} {food.current_variation} (ID: {food.food_id}) - ${food.food_price} each')
        print(f'Total Price: ${self.calculate_total()}')
            
# Creating different food items
pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")
# Creating an order and adding items
order = Order()
order.add_item(pizza, 2) # 2 Large Pepperoni Pizzas with extras
order.add_item(burger, 1) # 1 Double Burger with Brioche bun
order.add_item(drink, 3) # 3 Drinks (500ml each)

order.display_order()
print(f'Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10'): 0.2f}')