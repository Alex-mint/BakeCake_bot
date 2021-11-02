import logging
import time
import telegram
import re

from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from BakeCake.models import Message
from BakeCake.models import Profile
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

MENU, LEVELS, FORM, TOPPING, BERRIES, DECOR, INSCRIPTION, COMMENT, ADDRESS, DELIVERY_DATE, DELIVERY_TIME, ORDER, PERSONAL_DATA, PHONE = range(14)


TG_TOKEN = 'token'

bot = telegram.Bot(token=TG_TOKEN)

menu_keyboard = [['Собрать торт'],
                 ['Параметры заказа'],
                 ['Статус заказа']
                 ]

menu_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True, one_time_keyboard=True)


def chunks_generators(buttons, chunks_number):
    for i in range(0, len(buttons), chunks_number):
        yield buttons[i: i + chunks_number]


def keyboard_maker(buttons, number):
    keyboard = list(chunks_generators(buttons, number))
    markup = ReplyKeyboardMarkup(keyboard,
                                 resize_keyboard=True,
                                 one_time_keyboard=True)
    return markup


def bottons_parser(botton):
    return re.findall(r'\d+', botton)



def start(update, context):
    time.sleep(1)
    user = update.message.from_user
    text = f'Привет {user.first_name}, \nИзготовление тортов на заказ.\nВыберите ингредиенты, форму, основу, надпись, а мы привезем готовый торт к вашему празднику.'

    update.message.reply_text(text, reply_markup=menu_markup)
    context.user_data['user_id'] = update.message.chat_id
    context.user_data['first_name'] = update.message.from_user.first_name
    context.user_data['last_name'] = update.message.from_user.last_name   #null=True
    context.user_data['username'] = update.message.from_user.username
    #if db.get_one_thing(user_id) == None:
    if True:
        buttons = ['Согласен', 'Не согласен']
        personal_data_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        # send PDF
        update.message.reply_text('Ваше согласие на обработку персональных данных',
                                  reply_markup=personal_data_markup)
        return PERSONAL_DATA
    else:
        return MENU


def personal_data(update, context):
    user_message = update.message.text
    if user_message == 'Согласен':
        update.message.reply_text('Введите ваш контактный телефон')
        return PHONE
    elif user_message == 'Не согласен':
        update.message.reply_text('Мое дело предложить - Ваше отказаться')
    else:
        pass


def phone(update, context):
    user_message = update.message.text
    context.user_data['phone'] = user_message
    buttons = ['Собрать торт']
    input_markup = keyboard_maker(buttons, 2)
    time.sleep(0.5)
    update.message.reply_text('Собери свой первый торт',
                              reply_markup=input_markup)
    return MENU



def menu(update, context):
    user_message = update.message.text
    if user_message == 'Собрать торт':
        buttons = ['1 уровень (+400р)', '2 уровня (+750р)', '3 уровня (+1100р)', 'Вернулся в меню']
        context.user_data['level_buttons'] = buttons[:-1]
        levels_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Количество уровней (обязательное поле)', reply_markup=levels_markup)
        return LEVELS
    if user_message == 'Параметры заказа':
        update.message.reply_text('Пока в разработке',
                                  reply_markup=menu_markup)
        return MENU
    elif user_message == 'Статус заказа':
        update.message.reply_text('Пока в разработке', reply_markup=menu_markup)
        return MENU
    else:
        update.message.reply_text('Пока в разработке',
                                  reply_markup=menu_markup)
        return MENU


def levels(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    if user_message in context.user_data.get('level_buttons'):
        total_levels, price = bottons_parser(user_message)
        context.user_data['total_levels'] = int(total_levels)
        context.user_data['price'] = int(price)
        print(int(total_levels) + int(price))
        buttons = ['Квадрат (+600)', 'Круг (+400)',
                   'Прямоугольник (+1000)', 'Вернулся в меню']
        context.user_data['form_buttons'] = buttons[:-1]
        levels_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Форма (обязательное поле)',
                                  reply_markup=levels_markup)
        return FORM
    else:
        pass

def form(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    if user_message in context.user_data.get('form_buttons'):
        price = bottons_parser(user_message)
        context.user_data['bc_form'] = user_message.split('(')[0].strip()
        context.user_data['price'] = int(price[0])
        print(user_message.split()[0], price[0])
        buttons = ['Без топпинга (+0)', 'Белый соус (+200)',
                   'Карамельный сироп (+180)', 'Кленовый сироп (+200)',
                   'Клубничный сироп (+300)', 'Черничный сироп (+350)',
                   'Молочный шоколад (+200)', 'Вернулся в меню']
        context.user_data['topping_buttons'] = buttons[:-1]
        topping_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Топпинг (Обязательное поле)',
                                  reply_markup=topping_markup)
        return TOPPING
    else:
        pass


def topping(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    if user_message in context.user_data.get('topping_buttons'):
        price = bottons_parser(user_message)
        context.user_data['bc_topping'] = user_message.split('(')[0].strip()
        context.user_data['price'] = int(price[0])
        print(user_message.split('(')[0].strip(), price[0])
        buttons = ['Ежевика (+400)', 'Клубника (+500)',
                   'Малина (+300)', 'Голубика (+450)',
                   'Пропустить', 'Вернулся в меню']
        context.user_data['berries_buttons'] = buttons[:-2]
        berries_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Ягоды (Не обязательное для заполнения поле)',
                                  reply_markup=berries_markup)
        return BERRIES
    else:
        pass


def berries(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    if user_message in context.user_data.get('berries_buttons'):
        price = bottons_parser(user_message)
        context.user_data['bc_berries'] = user_message.split('(')[0].strip()
        context.user_data['price'] = int(price[0])
        print(user_message.split('(')[0].strip(), price[0])
        buttons = ['Маршмеллоу (+200)', 'Фисташки (+300)',
                   'Безе (+400)', 'Фундук (+350)',
                   'Пекан (+300)', 'Пропустить',
                   'Вернулся в меню']
        context.user_data['decor_buttons'] = buttons[:-2]
        berrie_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Декор (Не обязательное поле)',
                                  reply_markup=berrie_markup)
        return DECOR
    else:
        pass


def decor(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    if user_message in context.user_data.get('decor_buttons'):
        price = bottons_parser(user_message)
        context.user_data['bc_decor'] = user_message.split('(')[0].strip()
        context.user_data['price'] = int(price[0])
        print(user_message.split('(')[0].strip(), price[0])
        buttons = ['Пропустить', 'Назад',
                   'Вернулся в меню']
        decor_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Надпись (Не обязательное поле)')
        time.sleep(0.5)
        update.message.reply_text('Мы можем разместить на торте любую надпись, например: «С днем рождения!»',
                                  reply_markup=decor_markup)
        return INSCRIPTION
    else:
        pass


def inscription(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    else:
        context.user_data['bc_inscription'] = user_message
        context.user_data['price'] = 500
        print(user_message)
        buttons = ['Пропустить', 'Назад',
                   'Вернулся в меню']
        comment_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Комментарий к заказу', reply_markup=comment_markup)
        return COMMENT


def comment(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    else:
        context.user_data['bc_comment'] = user_message
        print(user_message)
        buttons = ['Назад', 'Вернулся в меню']
        delivery_date_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Адрес доставки',
                                  reply_markup=delivery_date_markup)
        return ADDRESS


def address(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    else:
        context.user_data['bc_address'] = user_message
        print(user_message)
        buttons = ['Назад', 'Вернулся в меню']
        address_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Дата доставки',
                                  reply_markup=address_markup)
        return DELIVERY_DATE


def delivery_date(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    else:
        context.user_data['bc_delivery_date'] = user_message
        print(user_message)
        buttons = ['Назад', 'Вернулся в меню']
        delivery_date_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Время доставки',
                                  reply_markup=delivery_date_markup)
        return DELIVERY_TIME


def delivery_time(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    else:
        context.user_data['bc_delivery_time'] = user_message
        print(user_message)
        buttons = ['Заказать торт', 'Назад', 'Вернулся в меню']
        delivery_time_markup = keyboard_maker(buttons, 2)
        time.sleep(0.5)
        update.message.reply_text('Здесь выводится весь заказ',
                                  reply_markup=delivery_time_markup)
        return ORDER


def order(update, context):
    user_message = update.message.text
    if user_message == 'Вернулся в меню':
        update.message.reply_text('Меню', reply_markup=menu_markup)
        return MENU
    elif user_message == 'Заказать торт':
        time.sleep(0.5)
        update.message.reply_text('Ваш заказ успешно принят', reply_markup=menu_markup)
        user_id = context.user_data.get('user_id')
        first_name = context.user_data.get('first_name')
        last_name = context.user_data.get('last_name')
        username = context.user_data.get('username')
        phone = context.user_data.get('phone')

        total_levels = context.user_data.get('total_levels')
        bc_form = context.user_data.get('bc_form')
        bc_topping = context.user_data.get('bc_topping')
        bc_berries = context.user_data.get('bc_berries')
        bc_decor = context.user_data.get('bc_decor')
        bc_inscription = context.user_data.get('bc_inscription')
        bc_comment = context.user_data.get('bc_comment')
        bc_address = context.user_data.get('bc_address')
        bc_delivery_date = context.user_data.get('bc_delivery_date')
        bc_delivery_time = context.user_data.get('bc_delivery_time')
        return MENU


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
    )
    return ConversationHandler.END


class Command(BaseCommand):
    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.BOT_TOKEN,

        )
        updater = Updater(TG_TOKEN, use_context=True)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],

            states={

                MENU: [CommandHandler('start', start),
                       MessageHandler(Filters.text, menu)],

                LEVELS: [CommandHandler('start', start),
                         MessageHandler(Filters.text, levels)],

                FORM: [CommandHandler('start', start),
                       MessageHandler(Filters.text, form)],

                TOPPING: [CommandHandler('start', start),
                          MessageHandler(Filters.text, topping)],

                BERRIES: [CommandHandler('start', start),
                          MessageHandler(Filters.text, berries)],

                DECOR: [CommandHandler('start', start),
                        MessageHandler(Filters.text, decor)],

                COMMENT: [CommandHandler('start', start),
                          MessageHandler(Filters.text, comment)],

                ADDRESS: [CommandHandler('start', start),
                          MessageHandler(Filters.text, address)],

                INSCRIPTION: [CommandHandler('start', start),
                              MessageHandler(Filters.text, inscription)],

                DELIVERY_DATE: [CommandHandler('start', start),
                                MessageHandler(Filters.text, delivery_date)],

                DELIVERY_TIME: [CommandHandler('start', start),
                                MessageHandler(Filters.text, delivery_time)],

                ORDER: [CommandHandler('start', start),
                        MessageHandler(Filters.text, order)],

                PERSONAL_DATA: [CommandHandler('start', start),
                                MessageHandler(Filters.text, personal_data)],

                PHONE: [CommandHandler('start', start),
                                MessageHandler(Filters.text, phone)],

            },

            fallbacks=[CommandHandler('cancel', cancel)]
        )

        dp.add_handler(conv_handler)

        updater.start_polling()
        updater.idle()


