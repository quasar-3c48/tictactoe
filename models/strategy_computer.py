from ramdom import choice

def pick_random_move(free_cells):
    return choice(free_cells) if free_cells else None