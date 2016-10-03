def hello_msg(first_name, last_name):
    msg = 'Здравствуйте, ' + first_name + ' ' + last_name + '.\n'
    msg += 'Вас приветствует vk messages control - бот, который будет пересылать вам сообщения из vk.\n'
    msg += 'Для управления ботом доступны следующие команды:\n\n'
    msg += '/settings - настройка доступа к vk\n'
    msg += '/get - получение последних сообщений\n'
    msg += '/exit - выход и сброс всех данных\n\n'
    msg += 'Удачи!'
    return msg

def login_msg():
    return 'Введите логин в строке для сообщения'

def pass_msg():
	return 'Теперь пароль^^'

def auth_err_msg():
	return 'Что-то не так. Возможно неправильный логин или пароль'