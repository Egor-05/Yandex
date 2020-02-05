def lucky(ticket):
    global lastTicket
    lastTicket = str(lastTicket)
    ticket = str(ticket)
    if len(lastTicket) < 6:
        lastTicket = lastTicket.rjust(6, '0')
    if len(str(ticket)) < 6:
        ticket = ticket.rjust(6, '0')
    if (sum([int(i) for i in lastTicket[:3]]) == sum([int(i) for i in lastTicket[3:]]) and
       sum([int(i) for i in ticket[:3]]) == sum([int(i) for i in ticket[3:]])):
        return 'Счастливый'
    else:
        return 'Несчастливый'
