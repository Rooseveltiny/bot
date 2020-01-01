import re
from commands import Parse

COMMANDS = {
    'запарси': Parse,
}

class KeyWord(object):

    def __init__(self, message):

        self.message = message.lower()
        self._perform_command()

    def _perform_command(self):

        COMMANDS[self.message.split(" ")[0].lower()](self.message)



message = "Запарси три страницы категории строительные технологии с сайта порно онлайн"        
command = KeyWord(message)



