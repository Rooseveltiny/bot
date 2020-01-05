
'''
this module is for describing possible commands of bot for controling web-sites!
'''

import re
import request
from models import CurrentWebSite

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

LIST_OF_SITES = [
    'xvideos.com',
    'pretty_cool.com',
    'cool_pussy.com',
    'homepornweb.com',
    'chertik.tv',
    'megapo.com',
    'keklol.kek',
    'maamacri.ru',
    'yoyoyoyoyo.net',
    ]

class ListSites(object):

    def __init__(self, parameters):

        self.list_of_sites = LIST_OF_SITES 

    def __str__(self):

        list_of_sites = ''
        for index, value in enumerate(self.list_of_sites):
            list_of_sites += str(index+1)+ ')  '+value+ '\n'
        return list_of_sites

class ChooseWebSite(object):

    def __init__(self, message):

        self.message = message
        site_number = int(re.search(r'\d+', message.text).group(0))

        try:
            self.web_site = LIST_OF_SITES[site_number - 1]
        except:
            self.web_site = LIST_OF_SITES[len(LIST_OF_SITES) - 1]
        
        self._choose_web_site()

    def _choose_web_site(self):

        current_web_site = CurrentWebSite(user = self.message.chat.id, current_web_site = self.web_site)
        current_web_site.save()

    def __str__(self):

        return 'Выбран ' +self.web_site+'!'

class ShowCurrentWebSite(CurrentWebSite):

    def __init__(self, message):

        self.user = message.chat.id

    def __str__(self):

        current_web_site = self.users_web_site().first()
        if current_web_site:
            return 'В данный момент выбран '+ current_web_site.current_web_site
        else:
            return 'В данный момент ничего не выбрано!'

class Parse(object):

    def __init__(self, parameters):

        self.message = parameters.text
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
        self.from_web_site = re.search(r'сайта (.+)', self.message).group(1)
        print(self.category, self.q_pages, self.from_web_site)  
        
    def go_api(self):

        pass

    def __str__(self):

        return "всё ок!"
        

if __name__ == "__main__":
    
    list_of_sites = str(ListSites('some message!'))
    print(list_of_sites)
    finish = 1