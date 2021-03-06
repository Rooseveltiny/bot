from key_word import KeyWord

TEST = [
    'Выбери сайт 1',
    'Текущий сайт?',
    'Список сайтов',
    'Сохрани 3 страницы из категории строительные технологии с сайта Фэйсбук',
] 

class Chat(object):

    id = 443028866

class MessageObject(object):

    chat = Chat
    
    def __init__(self, message):

        self.text = message

def perform_tests():

    tests_result = ''
    for message in TEST:    
        message = MessageObject(message)
        # command = KeyWord(message)
        tests_result += KeyWord(message).result+'\n'

    return tests_result

if __name__ == "__main__":

    perform_tests()



