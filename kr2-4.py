class Actor:
    def __init__(self, name, role, height):
        self.name = name
        self.role = role
        self.height = int(height)
        self.j = True

    def __str__(self):
        return f'Actor {self.name} {self.role}'

    def joke(self):
        self.j = not self.j
        return self.j

    def buffoonery(self, size):
        return size >= self.height

    def change_amplua(self, value, register):
        if register == 'up':
            value = value.upper()
        else:
            value = value.lower()
        self.role = value

    def __lt__(self, other):
        if len(self.role) == len(other.role):
            if self.height == other.height:
                return self.name < other.name
            return self.height < other.height
        return len(self.role) < len(other.role)

    def __gt__(self, other):
        if len(self.role) == len(other.role):
            if self.height == other.height:
                return self.name > other.name
            return self.height > other.height
        return len(self.role) > len(other.role)

    def __le__(self, other):
        return len(self.role) <= len(other.role)

    def __ge__(self, other):
        return len(self.role) >= len(other.role)

    def __eq__(self, other):
        return (len(self.role) == len(other.role) and
                self.height == other.height and
                self.name == other.name)

    def __ne__(self, other):
        return (len(self.role) != len(other.role) or
                self.height != other.height or
                self.name != other.name)


a = Actor('Pulcinella', 'stupid servant', 160)
print(a)
print(a.joke())
print(a.joke())
print(a.joke())
print(a.buffoonery(161))
a = Actor('Pulcinella', 'stupid servant', 160)
b = Actor('Coviello', 'smart servant', 160)
print(b)
print(a > b)
b.change_amplua('stupid servant', 'up')
print(b)
print(a > b)
print(b.buffoonery(150))