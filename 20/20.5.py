l1 = ['one',
      'two',
      'three',
      'four',
      'five',
      'six',
      'seven',
      'eight',
      'nine',
      'ten',
      'eleven',
      'twelve',
      'thirteen',
      'fourteen',
      'fifteen',
      'sixteen',
      'seventeen',
      'eighteen',
      'nineteen',
      'zero']

l2 = ['ten',
      'twenty',
      'thirty',
      'forty',
      'fifty',
      'sixty',
      'seventy',
      'eighty',
      'ninety']

l3 = ['one hundred',
      'two hundred',
      'three hundred',
      'four hundred',
      'five hundred',
      'six hundred',
      'seven hundred',
      'eight hundred',
      'nine hundred']


def number_in_english(number):
    if number < 20:
        return l1[number - 1]
    elif 19 < number < 100:
        number = str(number)
        if number[-1] != '0':
            return f'{l2[int(number[0]) - 1]} {l1[int(number[-1]) - 1]}'
        else:
            return l2[int(number[0]) - 1]
    else:
        number = str(number)
        if int(number[1] + number[-1]) <= 19:
            if number[1] != '0' and number[-1] != '0':
                return f'{l3[int(number[0]) - 1]} and {l1[int(number[1] + number[-1]) - 1]}'
            elif number[1] == '0' and number[-1] != '0':
                return f'{l3[int(number[0]) - 1]} and {l1[int(number[-1]) - 1]}'
            else:
                return l3[int(number[0]) - 1]
        else:
            if number[1] != '0' and number[-1] != '0':
                return f'{l3[int(number[0]) - 1]} and {l2[int(number[1]) - 1]} {l1[int(number[-1]) - 1]}'
            elif number[1] == '0' and number[-1] != '0':
                return f'{l3[int(number[0]) - 1]} and {l1[int(number[-1]) - 1]}'
            elif number[1] != '0' and number[-1] == '0':
                return f'{l3[int(number[0]) - 1]} and {l2[int(number[1]) - 1]}'
            else:
                return l3[int(number[0]) - 1]
