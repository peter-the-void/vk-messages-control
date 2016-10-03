import vk
#import config


def safe_request(method):
    def wrapper(*args, **kwargs):
        try:
            res = method(*args, **kwargs)
        except:
            res = None
        return res
    return wrapper

class Message:
    def __init__(self,fname,lname,text):
        self.first_name = fname
        self.last_name = lname
        self.massage_text = text

    def get_text(self):
        string = 'От: ' + self.first_name + ' '
        string += self.last_name + '\n'
        string += self.massage_text
        return string


class User:
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.api = None

    def auth(self):
        session = vk.AuthSession(
            app_id='5610770', 
            user_login=self.login, 
            user_password=self.password, 
            scope='messages',
        )
        self.api = vk.API(session)

    @safe_request
    def get_messages(self):
        unread_msgs = []
        print('1')
        messages = self.api.messages.get(out=0, count=5)
        for message in messages:
            print(message)
            if message['read_state'] == 0:
                user_info = self.api.users.gets(user_ids=message['user_id'])
                unread_msgs.append(Message(user_info['first_name'],user_info['last_name'],message['body']).get_text())
            print('2')       
        return unread_msgs
        
u = User('harovod@mail.ru', 'kinoprom12')
u.auth()
u.get_messages()
