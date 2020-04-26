def plans_for_tomorrow(text, divisor, *args, **kwargs):
    text = text.split(divisor)
    for i in args:
        if i[1] in kwargs:
            text[i[0]] = kwargs[i[1]](text[i[0]])
    return text


message = 'the jacket is entirely made of gold and silver and with buttons made of semi precious stones'
print(plans_for_tomorrow(
    message,
    ' ',
    (1, 'title'),
    (2, 'dic'),
    (1, 'abracodabra'),
    (10, 'title'),
    (1, 'dic'),
    set=lambda x: set(x),
    spliting=lambda x: x.split(),
    title=lambda x: x.title(),
    dic=lambda x: {len(x): x}
))