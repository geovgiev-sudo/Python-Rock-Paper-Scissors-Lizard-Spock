import random

BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
lizard = 'Lizard'
spock = 'Spock'
total_games_played = 0
win_counter = 0
draw_counter = 0
lose_counter = 0
troll_counter = 0

print(f'\n{BOLD}{BLUE}Hello and welcome to "Fun with ROCK, PAPER, SCISSORS, LIZARD or SPOCK!"\n')
input('Press ENTER to continue and have fun! ')
game_mode = input(f'\n{MAGENTA}Would you like to play against the computer or another human? Type "COMPUTER" or "HUMAN" ').lower()

if game_mode == 'human':
    print()
    print(f'{YELLOW}This feature is currently under development. Please stay tuned for further updates!' 
          f'\n\nIn this demo version, you can only play against the computer.')

while True:
    player_move = input(f'\n{BOLD}{MAGENTA}Please choose between ROCK, PAPER, SCISSORS, LIZARD or SPOCK: ').lower()

    if player_move == "rock":
        player_move = rock
    elif player_move == "paper":
        player_move = paper
    elif player_move == "scissors":
        player_move = scissors
    elif player_move == 'lizard':
        player_move = lizard
    elif player_move == 'spock':
        player_move = spock
    else:
        troll_counter += 1
        if troll_counter <= 3:
            print(f'\n{RED}Please be nice, follow the rules of the game. Try again...')
        elif 3 < troll_counter <= 5:
            print(f'\n{RED}Please stop! Be nice!')
        elif 5 < troll_counter <= 7:
            print(f'\n{RED}Stop that! You are making me sad!')
        elif 7 < troll_counter <= 9:
            print(f'\n{RED}I AM STARTING TO GET MAD! Play the game properly or else!')
        elif 9 < troll_counter:
            print(f'\n{RED}THAT\'S IT! I AM NOW SAD AND ANGRY! YOU DON\'T GET TO HAVE FUN! GOODBYE!')
            exit()
        continue
    print(f'\n{CYAN}You choose {player_move}!')
    input(f'\n{MAGENTA}What does the computer choose? ... Press ENTER to find out! ')

    computer_random_number = random.randint(1, 5)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    elif computer_random_number == 4:
        computer_move = lizard
    elif computer_random_number == 5:
        computer_move = spock

    print(f'\n{CYAN}The computer chooses {computer_move}.')

    if ((player_move == rock and (computer_move == scissors or computer_move == lizard)) or
        (player_move == paper and (computer_move == rock or computer_move == spock)) or
        (player_move == scissors and (computer_move == paper or computer_move == lizard)) or
        (player_move == lizard and (computer_move == paper or computer_move == spock)) or
        (player_move == spock and (computer_move == scissors or computer_move == rock))):
        print(f'\n{BOLD}{GREEN}You win this round!')
        win_counter +=1

    elif player_move == computer_move:
        print(f'\n{BOLD}{YELLOW}BAZINGA! Draw! ...')
        draw_counter += 1

    else:
        print(f'\n{BOLD}{RED}Loser!')
        lose_counter += 1

    total_games_played += 1

    answer = input(f'\n{MAGENTA}Would you like to play another game? Type "Yes" or "No"! ').lower()
    if answer == 'no':
        break
    elif answer == 'yes':
        continue

win_percentage = win_counter / total_games_played * 100
draw_percentage = draw_counter / total_games_played * 100
lose_percentage = lose_counter / total_games_played * 100

print(f'\n{CYAN}You have just had the most fun of your life! Here are your results:')
print(f'\nWins: {win_counter}. Win percentage: {win_percentage:.2f}%')
print(f'Draws: {draw_counter}. Draw percentage: {draw_percentage:.2f}%')
print(f'Losses: {lose_counter}. Lose percentage: {lose_percentage:.2f}%')
