def find_obj(path):
    path = path.split('/')
    last = root
    for i in path:
        check = False
        for j in last.content:
            if i == j.name:
                last = j
                check = True
                break
        if not check and i != path[-1]:
            print(f'Каталога {i} не существует в {"корневом" if last.name == "" else ""} '
                  f'каталоге {last.name}')
            return
    if last.name == path[-1]:
        return last
    else:
        return last.new_obj(path[-1], False)


class FileSystem:
    def __init__(self, file_name, parent=None):
        self.name = file_name
        self.parent = parent

    def pwd(self):
        history = []
        n = self
        while n.parent is not None:
            history.append(n.name)
            n = n.parent
        history.reverse()
        return '/'.join(history)

    def __str__(self):
        return self.name


class Directory(FileSystem):
    def __init__(self, file_name, parent=None):
        super().__init__(file_name, parent)
        self.content = []

    def get_file(self, file_name):
        for i in self.content:
            if i.name == file_name:
                return i
        print('Файла с таким именем не существует')

    def new_obj(self, file_name, is_dir=True, content=''):
        if is_dir:
            obj = Directory(file_name, self)
        else:
            obj = File(file_name, self, content)
        self.content.append(obj)
        return obj

    def ls(self):
        return self.content


class File(FileSystem):
    def __init__(self, file_name, parent=None, content=''):
        super().__init__(file_name, parent)
        self.content = content

    def add_content(self, content):
        self.content += ' ' + content


root = Directory('')
aaa = root.new_obj('aaa')
bbb = aaa.new_obj('bbb')
txt = bbb.new_obj('1.txt', False)
file = find_obj('aaa/bbb/234.txt')
if file is not None:
    file.add_content('Hello')
pass

