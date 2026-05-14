ALLOWED_SYMBOLS = ("X", "O")

def is_allowed(symbol):
    return symbol in ALLOWED_SYMBOLS
def opposite(symbol):
    return ALLOWED_SYMBOLS[1] if symbol == ALLOWED_SYMBOLS[0] else ALLOWED_SYMBOLS[0]