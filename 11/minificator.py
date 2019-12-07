a = int(input())
booltf = False
s1 = ''
for i in range(a):
    c = input()
    c_without_begin_spaces = c.lstrip()
    number_of_spaces = len(c) - len(c_without_begin_spaces)
    curr_str = c_without_begin_spaces
    q_list = [c_without_begin_spaces[i] for i in range(len(c_without_begin_spaces))]


    while '  ' in c_without_begin_spaces:
        c_without_begin_spaces = c_without_begin_spaces.replace('  ', ' ')
    quote = c_without_begin_spaces.find("'")
    print(' ' * number_of_spaces + c_without_begin_spaces)
