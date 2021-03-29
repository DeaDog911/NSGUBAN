from random import randint
import re

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from scripts.exams_counter import how_long_until_exams
from utils.misc.throttling import rate_limit


# @rate_limit(120, "gay")
@dp.message_handler(Command("gay", prefixes="!/"))
async def gay(message: types.Message):
    """Хедлер, для обработки комманды /gay или !gay
    В ответ, бот отправляет то, на сколько пользователь является геем
    Примеры:
        /gay
        /gay Vasya
        !gay
        !gay Vasya
    """
    # разбиваем сообщение на комманду и аргументы через регулярное выражение
    command_parse = re.compile(r"(!gay|/gay) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    target = parsed.group(2)
    percentage = randint(0, 100)

    # если пользователь не ввёл цель, он сам становится ею
    if not target:
        target = message.from_user.get_mention()
    # отправляем результат
    await message.reply(f"🏳️‍🌈 Похоже, что {target} гей на {percentage}%")


@dp.message_handler(Command('commie', prefixes='!/'))
async def commie(message: types.Message):
    command_parse = re.compile(r"(!commie|/commie) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    target = parsed.group(2)
    percentage = randint(0, 100)
    print(message.chat.id)
    # если пользователь не ввёл цель, он сам становится ею
    if not target:
        target = message.from_user.get_mention()

    # отправляем результат
    await message.reply(f"🚩 Похоже, что {target} коммунист на {percentage}%")


@dp.message_handler(Command('exams', prefixes='!/'))
async def exams(message: types.Message):
    await how_long_until_exams(now=True)