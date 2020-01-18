def bracket_check(test_string):
    start = 0
    end = 0
    if test_string.count('(') == test_string.count(')'):
        for i in test_string:
            if i == '(':
                start += 1
            if i == '(' and end != 0:
                break
            if i == ')':
                if start > 0:
                    start -= 1
                else:
                    end += 1
        if end == 0 and start == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
