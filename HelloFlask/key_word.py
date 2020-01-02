import re
from commands import Parse, ListSites, ChooseWebSite

COMMANDS = {
    'сохрани': Parse,
    'список сайтов': ListSites,
    'выбери': ChooseWebSite,
}

class KeyWord(object):

    def __init__(self, message):

        self.message = message.lower()
        return self._perform_command()

    def _perform_command(self):

        return str(COMMANDS[self.message.split(" ")[0].lower()](self.message))



message = "Сохрани три страницы категории строительные технологии с сайта чёртик"        
command = KeyWord(message)



