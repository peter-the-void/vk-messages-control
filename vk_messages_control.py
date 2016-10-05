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
        unread_msgs = list()
        messages = self.api.messages.get(out=0, count=500)
        for i in range(1, len(messages)):
            if messages[i]['read_state'] == 0:
                user_info = self.api.users.get(user_id = messages[i]['uid'])
                print(user_info)
                msg = Message(user_info[0]['first_name'],user_info[0]['last_name'], messages[i]['body'])
                unread_msgs.append(msg)                
        return unread_msgs


u = User(input(),input())
u.auth()
u.get_messages()
