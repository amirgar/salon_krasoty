import telebot
from telebot import types
from string import Template
import logging

token = "7116388354:AAGUoOwFEDfYJCxF2UUgxcd1S5KtidEq_y0"
link = 't.me/saloon_krasoty2_bot'
password = '12345678'
chat_idd = -1002202544493

bot = telebot.TeleBot(token)


user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'month', 'date', 'type', 'time']

        for key in keys:
            self.key = None


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    bot.send_message(message.chat.id, 'Здравствуйте! Мы салон красоты "Салон красоты". '
                                      'Здесь вы можете быстро в несколько кликов записаться на прием. Если вы готовы зарегистрироваться нажмите /reg🌹🌹🌹', reply_markup=markup)

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(message.chat.id, 'Этот бот поможет вам записаться на прием к врачу.')


@bot.message_handler(commands=['reg'])
def process_reg(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User("Набережные Челны")
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Введите ваше имя и фамилию:', reply_markup=markup)
        bot.register_next_step_handler(msg, process_reg_step2)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')

def process_reg_step2(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg  = bot.send_message(chat_id, 'Введите номер телефона: ')
        bot.register_next_step_handler(msg, process_reg_step3)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')

def process_reg_step3(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Январь')
        itembtn2 = types.KeyboardButton('Февраль')
        itembtn3 = types.KeyboardButton('Март')
        itembtn4 = types.KeyboardButton('Апрель')
        itembtn5 = types.KeyboardButton('Май')
        itembtn6 = types.KeyboardButton('Июнь')
        itembtn7 = types.KeyboardButton('Июль')
        itembtn8 = types.KeyboardButton('Август')
        itembtn9 = types.KeyboardButton('Сентябрь')
        itembtn10 = types.KeyboardButton('Октябрь')
        itembtn11 = types.KeyboardButton('Ноябрь')
        itembtn12 = types.KeyboardButton('Декабрь')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9,
                   itembtn10, itembtn11, itembtn12)
        msg = bot.send_message(chat_id, 'Выберите месяц приема: ', reply_markup=markup)
        bot.register_next_step_handler(msg, process_reg_step4)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')


def process_reg_step4(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.month = message.text
        markup = types.ReplyKeyboardRemove()
        msg = bot.send_message(chat_id, 'Выберите день приема: ', reply_markup=markup   )
        bot.register_next_step_handler(msg, process_reg_step5)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')

def process_reg_step5(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.date = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Маникюр')
        itembtn2 = types.KeyboardButton('Педикюр')
        itembtn3 = types.KeyboardButton('Стрижка')
        markup.add(itembtn1, itembtn2, itembtn3)

        msg = bot.send_message(chat_id, 'Выберите тип приема: ', reply_markup=markup)
        bot.register_next_step_handler(msg, process_reg_step6)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')

def process_reg_step6(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.type = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('9:00')
        itembtn2 = types.KeyboardButton('10:00')
        itembtn3 = types.KeyboardButton('11:00')
        itembtn4 = types.KeyboardButton('12:00')
        itembtn5 = types.KeyboardButton('13:00')
        itembtn6 = types.KeyboardButton('14:00')
        itembtn7 = types.KeyboardButton('15:00')
        itembtn8 = types.KeyboardButton('16:00')
        itembtn9 = types.KeyboardButton('17:00')
        itembtn10 = types.KeyboardButton('18:00')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)

        msg = bot.send_message(chat_id, 'Выберите время приема: ', reply_markup=markup)
        bot.register_next_step_handler(msg, process_reg_step7)
    except Exception as e:
        bot.reply_to(message, 'Упс, что-то пошло не так...')


def process_reg_step7(message):
    global chat_idd
    chat_id = message.chat.id
    userr = message.from_user.username
    user = user_dict[chat_id]
    user.time = message.text

    bot.send_message(chat_id, getRegData(user, 'Ваша заявка'), parse_mode="markdown")
    bot.send_message(chat_idd, sendRegData(user, 'Заявка от бота', userr), parse_mode="markdown")


def sendRegData(user, title, name=''):
    t = Template(
        '$title \n Имя и фамилия: *$fullname* \n Номер телефона: *$phone* \n Месяц приема: *$month* \n '
        'День приема: *$date* \n Тип приема: *$type* \n Время приема: *$time* \n Телеграм пользователя: @$address')

    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'phone': user.phone,
        'month': user.month,
        'date': user.date,
        'type': user.type,
        'time': user.time,
        'address': name
    })

def getRegData(user, title, name=''):
    t = Template('$title *$name* \n Имя и фамилия: *$fullname* \n Номер телефона: *$phone* \n Месяц приема: *$month* \n '
                 'День приема: *$date* \n Тип приема: *$type* \n Время приема: *$time* \n Если будет необходимо, '
                 'мы с вами свяжемся. Чтобы пройти регистрацию снова, нажмите /reg🌹🌹🌹   ')

    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'phone': user.phone,
        'month': user.month,
        'date': user.date,
        'type': user.type,
        'time': user.time
    })

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()


if __name__ == '__main__':
        bot.polling(none_stop=True)