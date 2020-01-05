import re
from commands import Parse, ListSites, ChooseWebSite, ShowCurrentWebSite

COMMANDS = {
    'сохрани': Parse,
    'список': ListSites,
    'выбери': ChooseWebSite,
    'текущий': ShowCurrentWebSite
}

class KeyWord(object):

    def __init__(self, message):

        self.message = message
        self.result = self._perform_command()

    def _perform_command(self):

        return str(COMMANDS[self.message.text.split(" ")[0].lower()](self.message))



