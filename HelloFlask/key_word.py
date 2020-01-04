import re
from commands import Parse, ListSites, ChooseWebSite

COMMANDS = {
    'сохрани': Parse,
    'список': ListSites,
    'выбери': ChooseWebSite,
}

class KeyWord(object):

    def __init__(self, **kwargs):

        #### here we should change on kwargs!!!!
        self.parameters = kwargs
        self.result = self._perform_command()

    def _perform_command(self):

        return str(COMMANDS[self.parameters['message'].split(" ")[0].lower()](self.parameters))


if __name__ == "__main__":
    
    data = {
        'message': 'список сайтов',
        'user_id': 1234321
    }

    command = KeyWord(data)
    



