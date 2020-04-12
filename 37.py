SERVERS = ['server1', 'server2', 'server3', 'server4']


class MailClient:

    inbox = []
    sent = []

    def __init__(self, server, user):
        if server not in SERVERS:
            print('Такого сервера не существует')
        self.user = user
        self.server = server
        self.load_folders()
        if len(self.inbox) > 0:
            print(f'Здравствуйте {user}, у вас в ящике {len(self.inbox)} сообщений')
        else:
            print(f'Здравствуйте {user}')

    def get_mail_from_server(self):
        # полуает почту с сервера и добавляет её в self.inbox
        pass

    def cleaner(self):
        # удаляет почту пользователя с сервера
        pass

    def load_folders(self):
        # загружет inbox и sent с диска для текущего пользователя
        pass

    def save_folders(self):
        # сохраняет inbox и sent на диск для текущего пользователя
        pass

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
            self.sent.append({'server': server1, 'from': self.user, 'to': user1, 'message': message})
