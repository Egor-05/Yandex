dict_of_friends = {}


def add_friends(name_of_person, list_of_friends):
    global dict_of_friends
    if name_of_person not in dict_of_friends:
        dict_of_friends[name_of_person] = list_of_friends
    else:
        dict_of_friends[name_of_person] += list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global dict_of_friends
    return name_of_person2 in dict_of_friends[name_of_person1]


def print_friends(name_of_person):
    dict_of_friends[name_of_person].sort()
    print(' '.join(dict_of_friends[name_of_person]))
