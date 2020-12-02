import numpy as np


class Animal:

    def __init__(self, name, species, favorite_food, color, habitat):
        self.name = name
        self.species = species
        self.favorite_food = favorite_food
        self.color = color
        self.habitat = habitat

    def eat(self, food_to_eat):
        if food_to_eat == self.favorite_food:
            print(f'Yummy {food_to_eat} is my favorite food!')
        else:
            print(f"""I am upset! {food_to_eat.capitalize()} isn't my favorite
                food: {self.favorite_food}""")
