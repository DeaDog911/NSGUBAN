from datetime import timedelta, datetime
from loader import bot
from data.config import NSGUBAN_CHAT_ID


async def how_long_until_exams(now=False):
    today = datetime.now()
    if today.hour == 21 or now:
        rus_day = datetime.strptime('03.06.2021', '%d.%m.%Y')
        math_day = datetime.strptime('07.06.2021', '%d.%m.%Y')
        inf_day = datetime.strptime('24.06.2021', '%d.%m.%Y')
        bio_day = datetime.strptime('18.06.2021', '%d.%m.%Y')
        chem_day = datetime.strptime('31.05.2021', '%d.%m.%Y')
        rus_days_count = int(divmod((today - rus_day).total_seconds(), 86400)[0])
        math_days_count = int(divmod((today - math_day).total_seconds(), 86400)[0])
        inf_days_count = int(divmod((today - inf_day).total_seconds(), 86400)[0])
        bio_days_count = int(divmod((today - bio_day).total_seconds(), 86400)[0])
        chem_days_count = int(divmod((today - chem_day).total_seconds(), 86400)[0])
        text = f"""
До экзаменов осталось

Русский: {rus_days_count}
        
Математика: {math_days_count}
Информатика: {inf_days_count}
        
Биология: {bio_days_count}
Химия: {chem_days_count}
        """
        await bot.send_message(chat_id=-1001471031306, text=text)
