jokes = []


def print_only_new(message):
    global jokes
    if message not in jokes:
        print(message)
        jokes.append(message)
