def who_are_you_and_hello():
    x = input()
    while not(x.isalpha() and x.capitalize() == x):
        x = input()
    print(f'Привет, {x}!')
