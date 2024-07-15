def hide_card(card_number):
    n = card_number.replace(' ', '')
    return f'************{n[-4:]}'
