import re
from commands import Parse, ListSites, ChooseWebSite

COMMANDS = {
    'сохрани': Parse,
    'список': ListSites,
    'выбери': ChooseWebSite,
}

class KeyWord(object):

    def __init__(self, parameter_of_message):

        self.parameters = parameter_of_message
        self.result = self._perform_command()

    def _perform_command(self):

        return str(COMMANDS[self.parameters.text.split(" ")[0].lower()](self.parameters))



