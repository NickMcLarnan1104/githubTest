# Quiz game by myself!

from functions import *
song = ''
correct = 0
wrong = 0

def main():

    print('Hello, welcome to the quiz game! There will be ten questions about eminem lyrics!')
    play_game = input('Are you ready to play the game? [y for yes and n for no]\n')
    play_game = play_game.lower()

    while play_game == 'y' and play_game != 'n':

        question = random_generator()
        song_chosen = random_question_generator(question)
        help_button()
        response_func(song_chosen)

        print()
        play_game = input('Would you like to keep going? ["y" for yes and "n" for no]\n')

        if play_game == 'n':
            results()

        
    input('Press ENTER to end program.')

main()
