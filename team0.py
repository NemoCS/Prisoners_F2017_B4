####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#Reid, Eric L, Mike

team_name = 'Team0: REM' # Only 10 chars displayed.
strategy_name = 'TOP SECRET'
strategy_description = 'WATCH AND SEE'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    if len(my_history)==1:
        return 'c'
    if len(my_history)==2:
        return 'b'
    if len(my_history)==3:
        return 'c'
    if len(my_history)==4:
        return 'b'
    if their_history[0:5]=='cccbc':
        return 'c'
    else:
        return 'b'

            
            

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

