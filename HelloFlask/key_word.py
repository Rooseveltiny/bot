from commands import Parse, ListSites, ChooseWebSite, ShowCurrentWebSite
from custom_exceptions import UnknownCommand
import re

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

        key_word = self.message.text.split(" ")[0].lower()
        if key_word in COMMANDS.keys():
            command = COMMANDS[key_word]
            return str(command(self.message))
        else:
            raise UnknownCommand('Непонятная команда, давай ещё разок)')

