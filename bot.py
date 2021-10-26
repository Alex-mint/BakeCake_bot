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

def log_errors(f):
    def inner(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка:{e}'
            print(error_message)
            raise e
    return inner()

@log_errors
def do_echo(update:Update, context:CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    profile,_=Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username
        }
    )
    reply_text = "Ваш id={}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        text=reply_text
    )

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
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True,
        )
        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()