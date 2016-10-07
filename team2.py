#Eric & Drake
team_name = 'haramBAEs' # Only 10 chars displayed.
strategy_name = 'build a wall'
strategy_description = 'idek'
    
def move(my_history, their_history, my_score, their_score):
    if their_history[-4:] == 'cbcb':
        return 'b'
    elif their_history[-4:] == 'bcbc':
        return 'b'
    elif their_history[-1:] == 'c':
        return 'c'
    elif their_history[-2:] == 'bb':
        return 'b'
    else:
        return'c'
