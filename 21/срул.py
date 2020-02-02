list_of_items = {}
counter = 0
cost = 0
count = 0


def add_item(itemName, itemCost):
    global count
    global cost
    global list_of_items
    cost += itemCost
    count += 1
    if itemName not in list_of_items:
        list_of_items[itemName] = [itemCost]
    else:
        list_of_items[itemName].append(itemCost)


def print_receipt():
    global count
    if count != 0:
        global cost
        global counter
        counter += 1
        global list_of_items
        print(f'Чек {counter}. Всего предметов: {count}')
        for i in list_of_items:
            for j in list_of_items[i]:
                print(i, '-', j)
        print('Итого:', cost)
        print('-----')
        cost = 0
        count = 0
        list_of_items = {}
