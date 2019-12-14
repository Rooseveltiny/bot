import sys, os
sys.path.append('/home/r/roosevelt/bot/Bot/') # указываем директорию с проектом
sys.path.append('./env/lib/python3.6/site-packages') # указываем директорию с библиотеками, куда поставили Flask
from Bot import app as application # когда Flask стартует, он ищет application. Если не указать 'as application', сайт не заработает
from werkzeug.debug import DebuggedApplication # Опционально: подключение модуля отладки
application.wsgi_app = DebuggedApplication(application.wsgi_app, True) # Опционально: включение модуля отадки
application.debug = False  # Опционально: True/False устанавливается по необходимости в отладке