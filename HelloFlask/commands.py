
import re
import request

NUMS = {
    'одну': 1,
    'две': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
}

class Parse(object):

    def __init__(self, message):

        self.message = message

        try:
            self._pick_up_information()
        except Exception as err:
            print('не удалось получить данные из сообщения для парсинга!')

    def _get_q_pages(self):

        for num_word in NUMS:
            if re.search(num_word, self.message):
                return NUMS[num_word]
        return int(re.search(r'(\d+)', self.message).group(1))

    def _pick_up_information(self):

        self.category = re.search(r'категории (.+) с сайта', self.message).group(1)
        self.q_pages = self._get_q_pages()
        self.from_web_site = re.search(r'с сайта (.+)', self.message).group(1)
        print(self.category, self.q_pages, self.from_web_site)  
        
    def go_api(self):

        pass
        