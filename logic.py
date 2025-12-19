from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer 
        self.pokemon_number = randint(1,1000)  
        self.weight = self.get_weight()
        self.name = self.get_name()
        self.img = self.get_img()
        self.name = self.get_name()
        self.hunger = randint(20, 70) 
        self.power = randint(30, 90)
        self.hp = randint(200, 400)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            image_url = data["sprites"]["front_default"]
            return image_url
        else:
            return "Pikachu"
        




        


    def feed(self, food_type="обычная"):
        if self.hunger <= 0:
            return f"{self.name} не голоден!"
        
        food_effects = {
            "обычная еда": {"hunger": -20},
            "ягода": {"hunger": -30},
            "эликсир": {"hunger": -50},
            "торт": {"hunger": -40}
        }

        
        
        effect = food_effects.get(food_type, food_effects["обычная еда"])
        self.hunger = max(0, self.hunger + effect["hunger"])
        response = f"{self.name} покормлен({food_type})! Сытость: {100 - self.hunger}%"

        return response
    
    
    def hunger_status(self):
        if self.hunger <= 10:
            return "сытый"
        elif self.hunger <= 30:
            return "немного голоден"
        elif self.hunger <= 50:
            return "голоден"
        elif self.hunger <= 70:
            return "очень голоден"
        else:
            return "умирает от голода!"
        







    def get_weight(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["weight"])
        else:
            return "60"
        

    # Метод класса для получения информации
    def info(self):
        return (f"Имя твоего покемона: {self.name}\n"
                f"Вес твоего покемона: {self.weight}\n"
                f"Сила твоего покемона: {self.power}\n"
                f"Здоровье твоего покемона: {self.hp}")
    
    # тут имя изменяется ⬇⬇⬇⬇

    def change_name(self, new_name):
        self.name = new_name
        return f"Имя покемона изменено на: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    





    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 2:
                return 'Покемон-волшебник применил щит в сражении'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


class Wizard(Pokemon):
    def info(self):
        return ' У тебя покемон-волшебник\n\n' + super().info()
    
class Fighter(Pokemon):
    def info(self):
        return ' У тебя покемон-боец\n\n' + super().info()
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'\nБоец примеил супер атаку силой {super_power}'
