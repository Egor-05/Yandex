class Report:
    def __init__(self, name, s_e_time, topic, report):
        """Формирует доклад"""
        self.name = name
        a, b = s_e_time
        a = [int(i) for i in a.split(':')]
        b = [int(i) for i in b.split(':')]
        a = a[0] * 3600 + a[1] * 60
        b = b[0] * 3600 + b[1] * 60
        self.s_e_time = (a, b)
        self.topic = topic
        self.report = report

    def __str__(self):
        """Вывод расписания докладов"""
        a = f'{self.s_e_time[0] // 3600:02d}:{self.s_e_time[0] % 3600 // 60:02d} - ' \
            f'{self.s_e_time[1] // 3600:02d}:{self.s_e_time[1] % 3600 // 60:02d} ' \
            f'{self.topic} ({self.name}), длина доклада: {self.len_of_report()}\n'
        return a

    def len_of_report(self):
        """Выводит длительность доклада"""
        a = self.s_e_time[1] - self.s_e_time[0]
        return f'{a // 3600} часов, {a % 3600 // 60} минут'


class Conference:
    def __init__(self):
        self.timetable = []

    def add_report(self, report):
        """добавляет доклад в расписание докладов"""
        if self.check_report_time(report):
            self.timetable.append(report)
            self.timetable = sorted(self.timetable, key=lambda x: x.s_e_time[0])
            return True
        return False

    def __str__(self):
        """Вывод расписания докладов"""
        return ''.join([str(i) for i in self.timetable])

    def max_break(self):
        """Выводит максимальный перерыв между докладами"""
        a = 0
        b = [(24, 0)] + [i.s_e_time for i in self.timetable] + [(24 * 3600, 0)]
        c = ''
        for i in range(len(b) - 1):
            if b[i + 1][0] - b[i][1] > a:
                a, c = b[i + 1][0] - b[i][1], f'{b[i][1] // 3600:02d}:{b[i][1] % 3600 // 60:02d} - ' \
                                              f'{b[i + 1][0] // 3600:02d}:{b[i + 1][0] % 3600 // 60:02d}'
        return f'{a // 3600:02d} часов, {a % 3600 // 60:02d} минут\nПерерыв: {c}'

    def check_report_time(self, report):
        """Проверяет правильно ли указанно время доклада"""
        for i in self.timetable:
            if i.s_e_time[0] <= report.s_e_time[0] <= i.s_e_time[1] or\
               i.s_e_time[0] <= report.s_e_time[1] <= i.s_e_time[1] or\
               report.s_e_time[0] <= i.s_e_time[0] <= report.s_e_time[1]:
                return False
        return True


c = Conference()
p = 1
while p:
    p = int(input('Введите:\n'
                  '1 - если вы хотите добавить доклад,\n'
                  '2 - если вы хотите увидеть расписание докладов и продолжить,\n'
                  '3 - для вывода максимального перерыва,\n'
                  '0 - выход: '))
    if p == 2:
        print(c)
    elif p == 1:
        a = input('Введите имя: ')
        b = input('Введите время начала доклада HH:MM: ')
        d = input('Введите время окончания доклада HH:MM: ')
        e = input('Введите тему доклада: ')
        f = input('Введите текст доклад: ')
        if c.add_report(Report(a, (b, d), e, f)):
            print('Доклад принят.')
        else:
            print('Указанное время для доклада уже занято!')
    elif p == 3:
        print(c.max_break())
