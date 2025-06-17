# function to simulate card game
def card_game(top_faces, bottom_faces):
    d_cnt = 0
    a_cnt = 0

    for i in range(len(top_faces)):
        if top_faces[i] == 'd' or top_faces[i] == 'D':
            d_cnt += 1
        elif top_faces[i] == 'a' or top_faces[i] == 'A':
            a_cnt += 1

    for i in range(len(bottom_faces)):
        if bottom_faces[i] == 'd' or bottom_faces[i] == 'D':
            d_cnt += 1
        elif bottom_faces[i] == 'a' or bottom_faces[i] == 'A':
            a_cnt += 1

    
    return "yes" if d_cnt >= 2 and a_cnt >= 1 else "no"

# take in input for the deck of cards
cards_top = ""
i = 0
while i < 3:
    face = input(f"Enter the top face of card {i+1}: ")
    if (face >= 'a' and face <= 'z') or (face >= 'A' and face <= 'Z'):
        cards_top += face
        i += 1
    else:
        print("Invalid input. Please enter a letter (a-z or A-Z).")\

cards_bottom = ""
i = 0
while i < 3:
    face = input(f"Enter the bottom face of card {i+1}: ")
    if (face >= 'a' and face <= 'z') or (face >= 'A' and face <= 'Z'):
        cards_bottom += face
        i += 1
    else:
        print("Invalid input. Please enter a letter (a-z or A-Z).")

result = card_game(cards_top, cards_bottom)
print(result)