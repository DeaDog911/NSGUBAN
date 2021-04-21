from datetime import timedelta, datetime
from loader import bot
from data.config import NSGUBAN_CHAT_ID


def how_long_until_exams():
    today = datetime.now()
    rus_day = datetime.strptime('03.06.2021', '%d.%m.%Y')
    math_day = datetime.strptime('07.06.2021', '%d.%m.%Y')
    inf_day = datetime.strptime('24.06.2021', '%d.%m.%Y')
    bio_day = datetime.strptime('18.06.2021', '%d.%m.%Y')
    chem_day = datetime.strptime('31.05.2021', '%d.%m.%Y')
    rus_days_count = int(divmod((rus_day - today).total_seconds(), 86400)[0])
    math_days_count = int(divmod((math_day - today).total_seconds(), 86400)[0])
    inf_days_count = int(divmod((inf_day - today).total_seconds(), 86400)[0])
    bio_days_count = int(divmod((bio_day - today).total_seconds(), 86400)[0])
    chem_days_count = int(divmod((chem_day - today).total_seconds(), 86400)[0])
    text = f"""
До экзаменов осталось

Русский: {rus_days_count}
        
Математика: {math_days_count}
Информатика: {inf_days_count}
        
Биология: {bio_days_count}
Химия: {chem_days_count}
        """
    return text


async def send_exams_info():
    today = datetime.now()
    if today.weekday() == 0 and today.hour == 21:
        text = how_long_until_exams()
        await bot.send_message(chat_id=NSGUBAN_CHAT_ID, text=text, disable_notification=True)