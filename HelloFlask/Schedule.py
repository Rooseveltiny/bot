
from datetime import datetime, timedelta
import request
import re

DATE_WORDS = {
    "Понедельник": 1,
    "Вторник": 2,
    "Среду": 3,
    "Четверг": 4,
    "Пятницу": 5,
    "Субботу": 6,
    "Воскресение": 7,
}

KEY_WORDS = {
    'сегодня': 0,
    'на следующей': 7,
    'на прошлой': -7,
    'завтра': 1,
    'вчера': -1,
    'послезавтра': 2,
    'позавчера': -2
}

class Schedule(object):

    answer = 'Не удалось получить расписание!'

    def __init__(self, message):

        self.message = message
        self._set_date()

    def _set_date(self):

        today = datetime.now().date()

        found_word = None
        for word in DATE_WORDS.keys():
            if re.search(r'\S+'+word, self.message, re.IGNORECASE):
                found_word = word.lower()
                break

        found_keyword = "cегодня"
        for word in KEY_WORDS.keys():
            if re.search(r'\S+'+word, self.message, re.IGNORECASE):
                found_keyword = word.lower()
                break

        if not found_word:

            date = today - timedelta(days = today.weekday())
            date = today + timedelta(days = KEY_WORDS[found_keyword])
            print(date)

        
        
        

schedule = Schedule("Что у нас на следующей неделе во вторник?")
schedule = Schedule("Что у нас завтра?")
schedule = Schedule("Что у нас послезавтра?")
schedule = Schedule("Что у нас в среду?")
schedule = Schedule("Что у нас было на прошлой неделе в понедельник?")


