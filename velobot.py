import telebot
from telebot import types
import json


def read_token(filename="config.json"):
    try:
        with open(filename, "r") as file:
            config = json.load(file)
            return config.get("telegram_token")
    except Exception as e:
        print("Ошибка при чтении конфигурации:", e)
        return None

token = read_token()
if token:
    bot = telebot.TeleBot(token)
else:
    print("Ошибка: Токен не найден!")
    

def inpudol():
    with open("") as ins:
        d = []
        for line in ins:
            d.append(float(line.strip()))
    dol = d
    return dol


def inpushir():
    with open("", 'r', encoding='utf-8') as ins:
        c = []
        for line in ins:
            c.append(float(line.strip()))
    shir = c
    return shir


def inpunaim():
    with open("", 'r', encoding='utf-8') as ins:
        c = []
        for line in ins:
            c.append(str(line.strip()))
    naim = c
    return naim


def inpuokrug():
    with open("", 'r', encoding='utf-8') as ins:
        c = []
        for line in ins:
            c.append(str(line.strip()))
    okrug = c
    return okrug


def inpuraion():
    with open("", 'r', encoding='utf-8') as ins:
        c = []
        for line in ins:
            c.append(str(line.strip()))
    raion = c
    return raion


def inpuadres():
    with open("", 'r', encoding='utf-8') as ins:
        c = []
        for line in ins:
            c.append(str(line.strip()))
    adres = c

    return adres


def find_near(d, s):
    minras = 1000000000000000000000000000000000000
    num = 0
    for i in range(971):
        ras = ((shir[i] - s) ** 2 + (dol[i] - d) ** 2) ** 0.5

        if ras < minras:
            minras = ras
            num = i
    print(naim[num], okrug[num], raion[num], adres[num], sep='\n')
    return [naim[num], okrug[num], raion[num], adres[num]]


dol = inpudol()
shir = inpushir()
naim = inpunaim()
okrug = inpuokrug()
raion = inpuraion()
adres = inpuadres()


@bot.message_handler(commands=['start'])
def start(message):
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    loc_btn = types.KeyboardButton(text="Отправить геопозицию", request_location=True)
    btn.add(loc_btn)
    bot.send_message(message.chat.id, "Привет, я бот, который поможет найти тебе ближайшую праковку для твоего"
                                      " велосипеда! Отправь мне свою геопозицию и я поищу, что есть поблизости "
                                      "\n\nИнформация о боте: /help", reply_markup=btn)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Этот бот создан командой студентов Высшей Инженерной Школы РУТ (МИИТ) для'
                                      ' упрощения поиска велосипедных парковок. В будущем планируется множество'
                                      ' обновлений, которые сделают поиск парковки ещё проще и быстрее! Оставайтесь с'
                                      ' нами и слдеите за обновлениями!')


@bot.message_handler(content_types=['location'])
def check_loc(message):
    d = message.location.longitude
    s = message.location.latitude
    bot.send_message(message.chat.id, str('\n'.join(find_near(d, s))))


bot.polling(none_stop=True, interval=0)
