import telebot
from random import randint
from config import token
from logic import Pokemon, Wizard, Fighter 
from datetime import datetime, timedelta

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1, 3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        
        bot.send_message(message.chat.id, f"Поздравляем! Ты создал покемона!\n\n{pokemon.info()}")
        bot.send_photo(message.chat.id, pokemon.show_img())
        
        # Проверка типа покемона
        if chance == 2:  # Wizard
            type_msg = "Твой покемон - Волшебник! Может использовать щит в бою."
        elif chance == 3:  # Fighter
            type_msg = "Твой покемон - Боец! Имеет шанс нанести критический удар."
        else:  # обычный
            type_msg = "Твой покемон - обычный тип."
            
        bot.send_message(message.chat.id, type_msg)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона! Используй /attack чтобы атаковать другого человека.")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        attacker_username = message.from_user.username
        defender_username = message.reply_to_message.from_user.username
        
        if (defender_username in Pokemon.pokemons.keys() and 
            attacker_username in Pokemon.pokemons.keys()):
            
            enemy = Pokemon.pokemons[defender_username]
            pok = Pokemon.pokemons[attacker_username]
            
            res = pok.attack(enemy)
            
            bot.send_message(message.chat.id, res)
            
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
            
    else:
        bot.send_message(message.chat.id, 
                         "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
        

        
@bot.message_handler(commands=['feed'])
def feed_pokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        result = pokemon.feed()
        bot.reply_to(message, result)
    else:
        bot.send_message(message.chat.id, "У тебя еще нет покемона! Используй /start чтобы создать своего покемона.")
    



@bot.message_handler(commands=['info'])
def show_info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        if isinstance(pok, Wizard):
            pokemon_type = "Волшебник"
            special_ability = "Имеет щит для защиты"
        elif isinstance(pok, Fighter):
            pokemon_type = "Боец"
            special_ability = "Имеет шанс нанести критический удар"
        else:
            pokemon_type = "Обычный"
            special_ability = "Нет особых способностей"
        info_text = f"Информация о покемоне:\n\n"
        info_text += f"Тренер: {pok.pokemon_trainer}\n"
        info_text += f"Номер: #{pok.pokemon_number}\n"
        info_text += f"Имя: {pok.name}\n"
        info_text += f"Вес: {pok.weight} кг\n"
        info_text += f"Здоровье: {pok.hp} HP\n"
        info_text += f"Сила: {pok.power}\n"
        info_text += f"Голод: {pok.hunger}%\n"
        
        
        bot.send_message(message.chat.id, info_text)
    else:
        bot.reply_to(message, "У тебя еще нет покемона! Используй /start чтобы создать своего покемона.")


bot.infinity_polling(none_stop=True)
