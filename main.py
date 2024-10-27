import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('')

@bot.message_handler(content_types = ['photo', 'audio'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a good photo', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id )


@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото' )
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Hello', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Open website')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Photo deleted')


@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, '<u>Help</u> <em>information</em>', parse_mode = 'html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}' )
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Your id {message.from_user.id}')

    
bot.polling(non_stop = True)
