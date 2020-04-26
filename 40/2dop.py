class Server:
    def __init__(self, name, usernames):
        self.usernames = usernames
        self.name = name


class User:
    def __init__(self, username):
        self.name = username
        self.inbox = []
        self.sent = []


SERVERS = {'server1': Server('server1', {'qwerty': User('qwerty'),
                                         'user': User('user'),
                                         'Vasya': User('Vasya')}),
           'server2': Server('server2', {'abc': User('abc'),
                                         'frejkh': User('frejkh')}),
           'server3': Server('server3', {'U.N. Known': User('U.N. Known'),
                                         'Mister X': User('Mister X')}),
           'server4': Server('server4', {'asd': User('asd'),
                                         'karkarych': User('karkarych'),
                                         'ghost': User('ghost')})}


class MailClient:

    inbox = []
    sent = []

    def __init__(self, server, user):
        if server not in SERVERS.keys():
            print('Такого сервера не существует')
        self.server = SERVERS[server]
        if user not in self.server.usernames.keys:
            print('Такого пользователя не существует')
        self.user = server.usernames[user]
        if len(self.inbox) > 0:
            print(f'Здравствуйте {user}, у вас в ящике {len(self.inbox)} сообщений')
        else:
            print(f'Здравствуйте {user}')

    def get_mail_from_server(self):
        self.inbox = self.user.inbox

    def cleaner(self):
        self.user.inbox = []

    def receive_mail(self):
        self.get_mail_from_server()
        print('Список пользователей, написавших вам:')
        for idx, val in enumerate(self.inbox):
            print(f'{idx}. {val["from"]} написал вам:')
            print(val['message'])
        print('Хотите ли кому-то из них ответить?')
        a = input()
        while 1:
            if a == 'Да':
                while 1:
                    a = int(input('Введите номер письма для ответа'))
                    while a >= len(self.inbox):
                        a = int(input('Введите номер письма для ответа'))
                    b = input('Введите сервер')
                    while b not in SERVERS:
                        b = input('Введите сервер ещё раз')
                    self.send_mail(b, self.inbox[a]['from'], input('Введите сообщение'))
                    a = input('Вы хотите закончить?')
                    if a == 'Да':
                        break
            elif a == 'Нет':
                break
            else:
                a = input('Вводите только Да или Нет')
            self.cleaner()

    def send_mail(self, server1, user1, message):
        if server1 in SERVERS:
            if user1 in SERVERS[server1].usernames:
                self.user.sent.append({'server': server1,
                                       'from': self.user,
                                       'to': user1,
                                       'message': message})
                SERVERS[server1].usernames[user1].inbox.append({'server': self.server,
                                                                'from': self.user,
                                                                'message': message})
