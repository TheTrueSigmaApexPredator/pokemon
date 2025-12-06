from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.weight = self.get_weight()
        self.name = self.get_name()
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

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
        return f"Имя твоего покемона: {self.name}"
    def show_weight(self):
        return f"Вес твоего покемона: {self.weight}"
    
    # тут имя изменяется ⬇⬇⬇⬇

    def change_name(self, new_name):
        self.name = new_name
        return f"Имя покемона изменено на: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



