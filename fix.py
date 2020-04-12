from collections import defaultdict


def return_user_mail(user):
    if user in users_emails:
        return users_emails[user]
    return []


def append_to_dict1(user, user1, message):
    users_emails[user].append({user1: message})


def append_to_dict2(user, user1, message):
    users_sent[user1].append({user: message})


def cleaner(user):
    users_emails[user] = []


users_emails = defaultdict(list)
users_sent = defaultdict(list)
SERVERS = ['server1', 'server2', 'server3', 'server4']


class MailClient:

    def __init__(self, server, user):
        if server not in SERVERS:
            print('Такого сервера не существует')
        self.user = user
        self.server = server
        self.user_emails = return_user_mail(user)
        if len(self.user_emails) > 0:
            print(f'Здравствуйте {user}, у вас есть непрочитанные письма')
        else:
            print(f'Здравствуйте {user}')

    def receive_mail(self):
        print('Список пользователей, написавших вам:')
        for i in self.user_emails:
            print(f'{i} написал вам:')
            for j in self.user_emails[i]:
                print(j)
        print('Хотите ли кому-то из них ответить?')
        a = input()
        while 1:
            if a == 'Да':
                while 1:
                    a = input('Введите имя написавшего вам пользователя')
                    while a not in self.user_emails:
                        a = input('Введите имя написавшего вам пользователя')
                    b = input('Введите сервер')
                    while b not in SERVERS:
                        b = input('Введите сервер ещё раз')
                    self.send_mail(b, a, input('Введите сообщение'))
                    a = input('Вы хотите закончить?')
                    if a == 'Да':
                        break
            elif a == 'Нет':
                break
            else:
                a = input('Вводите только Да или Нет')
            cleaner(self.user)

    def send_mail(self, server1, user1, message):
        if server1 in SERVERS:
            append_to_dict1(user1, self.user, message)
            append_to_dict2(user1, self.user, message)
