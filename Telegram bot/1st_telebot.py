import telebot
import json
import requests

bot = telebot.TeleBot('7052279821:AAGCo403edWmgsreodEWP1UAtH2mZgf1C-8')

searching = False  
ru_pressed = False
en_pressed = False

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)  
    button_en = telebot.types.KeyboardButton("/English")
    button_ru = telebot.types.KeyboardButton("/Русский")
    markup.add(button_en, button_ru)
    bot.send_message(message.chat.id, "Choose language \nВыберите язык", reply_markup=markup)

@bot.message_handler(commands=['English'])
def start_english(message):
    global searching
    searching = False 
    global en_pressed
    en_pressed = True
    global ru_pressed 
    ru_pressed = False
    if message.from_user.last_name != None:
         sms = f"Hello <b>{message.from_user.first_name}  <u>{message.from_user.last_name}</u></b>!, this bot can help you to find any music in iTunes site. Firstly, press a button 'search_music', and then just type a name of a song and i send you a link."   
    else:
        sms = f"Hello <b>{message.from_user.first_name} </b>!, this bot can help you to find any music in iTunes site. Firstly, press a button 'search_music', and then just type a name of a song and i send you a link."
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    search_music = telebot.types.KeyboardButton("/search_music")
    markup.add(search_music)
    bot.send_message(message.chat.id, sms, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['Русский'])
def start_russian(message):
    global searching
    searching = False  
    global ru_pressed
    ru_pressed = True
    global en_pressed
    en_pressed = False
    if message.from_user.last_name != None:
        sms = f"Здравствуйте <b>{message.from_user.first_name}  <u>{message.from_user.last_name}</u></b>!, этот бот поможет вам найти любую музыку на сайте iTunes. Сначала нажмите кнопку 'Искать музыку', а затем просто введите название песни, и я пришлю вам ссылку."   
    else:
        sms = f"Здравствуйте <b>{message.from_user.first_name} </b>!, этот бот поможет вам найти любую музыку на сайте iTunes. Сначала нажмите кнопку 'Искать музыку', а затем просто введите название песни, и я пришлю вам ссылку."
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    search_music = telebot.types.KeyboardButton("/Искать_музыку")
    markup.add(search_music)
    bot.send_message(message.chat.id, sms, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['search_music', 'Искать_музыку'])
def start_searching(message):
    global searching
    searching = True  
    if en_pressed:
        text = "And now type any song to search, I strictly recommend also type a name of artist: "
    elif ru_pressed:
        text = "А теперь введите в поиск любую песню, настоятельно рекомендую также ввести имя исполнителя:"
    bot.send_message(message.chat.id, text, parse_mode='html')


    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global searching
    if searching:  
        song_name = message.text
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + song_name)
        data = response.json()
        first_result = data['results'][0]
        track_view_url = first_result['trackViewUrl']
        bot.send_message(message.chat.id, track_view_url, parse_mode='html')

bot.polling(none_stop = True)
