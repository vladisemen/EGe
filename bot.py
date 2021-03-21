from pprint import pprint

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

import bot_config

def start(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text="Я бот, напиши что-нибудь")

def echo(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
   text_caps = ' '.join(context.args).upper()
   context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def inline_caps(update, context):
   query = update.inline_query.query
   if not query:
      return
   results = list()
   results.append(
      InlineQueryResultArticle(
         id=query.upper(),
         title='Caps',
         input_message_content=InputTextMessageContent(query.upper())
      )
   )
   context.bot.answer_inline_query(update.inline_query.id, results)

def main():
   my_bot = Updater(bot_config.TOKEN)

   dispatcher = my_bot.dispatcher

   start_handler = CommandHandler('start', start)
   dispatcher.add_handler(start_handler)

   caps_handler = CommandHandler('caps', caps)
   dispatcher.add_handler(caps_handler)

   inline_caps_handler = InlineQueryHandler(inline_caps)
   dispatcher.add_handler(inline_caps_handler)

   echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
   dispatcher.add_handler(echo_handler)

   my_bot.start_polling()
   my_bot.idle()


if __name__ == '__main__':
   main()
