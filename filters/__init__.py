from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .user_chat import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
