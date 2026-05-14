BOARD_SIZE = 6
WIN_LENGTH = 6

def validate_config():
    """I did that as a kind of error handling funtion. For example, if In the future, I add config parameters, I'll update the logic. But for now I just kept that simple by handling the current params """
    if BOARD_SIZE < 3:
        raise ValueError("BOARD_SIZE must be >= 3")
    if WIN_LENGTH < 3:
        raise ValueError("WIN_LENGTH must be >= 3")
    if WIN_LENGTH > BOARD_SIZE:
        raise ValueError("WIN_LENGTH cannot be greater than BOARD_SIZE")