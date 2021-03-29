import asyncio

from aiogram import executor

from utils.notify_admins import on_startup_notify
from scripts.exams_counter import how_long_until_exams

NOTIFICATIONS_DELAY = 3600


async def on_startup(dispatcher):
    import filters
    import middlewares
    await on_startup_notify(dispatcher)


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(NOTIFICATIONS_DELAY, repeat, coro, loop)


if __name__ == '__main__':
    from handlers import dp
    loop = asyncio.get_event_loop()
    loop.call_later(NOTIFICATIONS_DELAY, repeat, how_long_until_exams, loop)
    executor.start_polling(dp, on_startup=on_startup)
