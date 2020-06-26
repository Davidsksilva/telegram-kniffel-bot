import telegram

from constants import TOKEN

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())
