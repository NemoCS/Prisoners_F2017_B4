####
# Names: Cory Smith & Brian Sadowitz
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '08 Bagels' # Only 10 chars displayed.
strategy_name = 'No Forgiveness'
strategy_description = 'You will regret your betrayal. The guilty pay the price.'
    
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'