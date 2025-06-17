import random
# fumction to simulate the dice game
def play_dice_game():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_of_die = dice_1 + dice_2
    if sum_of_die == 6 or sum_of_die == 7 or sum_of_die == 8:
        return "Win!"
    else:
        return "Lose!"

print(play_dice_game())