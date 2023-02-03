from aiogram import executor
from aiogram import Dispatcher, Bot

from time import sleep
from datetime import datetime

from core.config import TOKEN
from core.config import PERM_USERS, PERM_IDS

from core.tracker import Scraper


def __isvaliduser__(
    username, userid):
    if (username in PERM_USERS and
    userid in PERM_IDS):
        return True

    else: 
        return False


bot = Bot(TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands="start")
async def start(
    message):
    while True:
        if (is_valid):
            is_valid = __isvaliduser__(
            message.from_user['username'], message.from_user['id'])

            try:
                scrape = Scraper('bitcoin')
                scrape.scraper()

                data = scrape.return_data(scrape.tag, scrape.price)
                print(data)
                
                my_course = round(float(data[1]) * 0.00183794, 2)
                print((my_course))

                await message.answer(f"Avarage {data[0]} Course: {data[1]}.\nMy {data[0]} Course: {my_course}")
                del scrape, data, my_course
                
                sleep(3600)

            except:
                pass


if __name__ == "__main__":
    while True:
        executor.start_polling(dispatcher)