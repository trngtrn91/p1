# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "P"
    if (len(opponent_history) >= 4 and len(opponent_history) < 1002) or (len(opponent_history) >= 7000 and len(opponent_history) <=8000):
        if opponent_history[-3] == 'R' and opponent_history[-2] == 'P' and opponent_history[-1] == 'P':
            #opponent = 'Quincy'
            choose = ["P", "P", "S", "S", "R"]
            guess = choose[len(opponent_history) % len(choose)]
    
    if (len(opponent_history) >= 1002 and len(opponent_history) <2002) or (len(opponent_history) >= 4000 and len(opponent_history) <5000):
        #opponent = 'abb'       

        pattern = [
        ['R', 'P', 'S', 'R', 'S', 'P', 'P', 'R', 'S', 'S'],
        ['P', 'S', 'S', 'R', 'R', 'P', 'S', 'R', 'P', 'R'],
        ['S', 'R', 'P', 'P', 'S', 'S', 'R', 'P', 'R', 'S'],
        ['R', 'R', 'S', 'P', 'R', 'S', 'P', 'S', 'R', 'P'],
        ['P', 'R', 'R', 'S', 'P', 'S', 'R', 'S', 'S', 'P'],
        ['S', 'P', 'R', 'R', 'P', 'R', 'S', 'S', 'P', 'R'],
        ['R', 'S', 'S', 'P', 'P', 'R', 'R', 'S', 'P', 'S'],
        ['P', 'P', 'R', 'S', 'R', 'P', 'S', 'P', 'R', 'S'],
        ['S', 'R', 'S', 'R', 'P', 'P', 'S', 'R', 'P', 'R'],
        ['R', 'P', 'P', 'S', 'S', 'R', 'P', 'R', 'S', 'P']]
        if len(opponent_history) % 10 == 0:
            guess = pattern[0][len(opponent_history) % 10]
        elif len(opponent_history) % 10 == 1:
            guess = pattern[1][len(opponent_history) % 2]
        elif len(opponent_history) % 10 == 2:
            guess = pattern[2][9]
        elif len(opponent_history) % 10 == 3:
            guess = pattern[3][3]
        elif len(opponent_history) % 10 == 4:
            guess = pattern[3][3]
        elif len(opponent_history) % 10 == 5:
            guess = pattern[3][3]
        elif len(opponent_history) % 10 == 6:
            guess = pattern[2][9]
        elif len(opponent_history) % 10 == 7:
            guess = pattern[8][9]
        elif len(opponent_history) % 10 == 8:
            guess = pattern[8][1]
        elif len(opponent_history) % 10 == 9:
            guess = pattern[9][2]
      
        
        

    if (len(opponent_history) >= 2002 and len(opponent_history) <4000) or (len(opponent_history) >= 5000 and len(opponent_history) <6000):
        #opponent = 'kris'
        choose1 = ['R', 'S', 'P']
        guess = choose1[len(opponent_history) % len(choose1)]
        

    if (len(opponent_history) >= 3002 and len(opponent_history) <4000) or (len(opponent_history) >= 6000 and len(opponent_history) <7000):
        # oppent = mr
        # last_ten = opponent_history[-10:]
        # most_frequent = min(set(last_ten), key=last_ten.count)
        # if most_frequent == '':
        #     most_frequent = "R"
        # above = prev_play
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        if prev_play:
            guess = ideal_response[prev_play]
        # prev play = max of my history 10 last move
        
    
    return guess
