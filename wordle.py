#!/usr/bin/env python3
"""
This class is an implentation of a Wordle game. 

"""
import pandas as pd
from random import choice
import helpers
import generator
import argparse
import frequency

MAX_GUESSES = 6
COMPUTER_FIRST_GUESS = "AEROS"

def main(is_automatic):
    """
        Main function.
    """
    
    master_list = get_master_list()
    target_word = choose_target_word(master_list)
    game        = Wordle(target_word, is_automatic)
    game.play_game(is_automatic)
    

def get_master_list():
    master_list = open('student_project_resources/wordle_valid_words.txt', 'r').read().upper().split('\n')
    master_list += open('student_project_resources/wordle_common_words.txt', 'r').read().split('\n') * 10
    return master_list

def get_beginning_filtered_list():
    filtered_list = open('student_project_resources/wordle_valid_words.txt', 'r').read().upper().split('\n')
    return filtered_list


def choose_target_word(master_list):
    return choice(master_list)


class Wordle:
    def __init__(self, solution, automated):
        self.solution  = solution
        self.automated = automated

    def play_game(self, automated):
        """
            Starts a Wordle game for the user.
        """
        guess_no = 1
        solved   = False

        print(f"Solution: {self.solution}")

        

        # Decides if a human player or an automated "worlde cracker" program is playing.
        
        if automated == False:
            player = generator.Human_Guess()

            while MAX_GUESSES > guess_no:
                print(f"Guess #{guess_no}/{MAX_GUESSES}:", end=" ")
                guess = player.new_word()

                if self.solution == guess:
                    solved = True
                    print("You found the solution!")
                    break
                elif False == player.valid_word(guess):
                    continue
                else:
                    feedback = helpers.process_guess(self.solution, guess)
                    print(feedback)
                    guess_no += 1

            if (not solved) and (MAX_GUESSES == guess_no):
                print(f'You failed to guess the word: #{self.solution} womp womp')






        #give first guess
        #if solution == first guess
        #done!
        #else enter loop
        #receive feedback
        #filter the filtered master list
        #generate next best word
        #use as next guess
        elif automated == True:

            player = generator.Machine_Guess()
            filtered_list = get_beginning_filtered_list()

            print(filtered_list)
            

            alphabet_weights = frequency.alphabet_freq()
            guess         = frequency.top_word(alphabet_weights)

            while MAX_GUESSES > player.guess_no:
                print(f"Guess #{guess_no}/{MAX_GUESSES}:", end=" ")
                guess = player.new_word()

                if self.solution == guess:
                    solved = True
                    print("You found the solution!")
                    break

                elif False == player.valid_word(guess):
                    continue
                else:
                    player.feedback = helpers.process_guess(self.solution, guess)
                    print(feedback)
                    player.guess_no += 1

            if (not solved) and (MAX_GUESSES == guess_no):
                print(f'You failed to guess the word: #{self.solution} womp womp')







        else:
            print('how did you get here ???')


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-a', '--automation', help='enables automatic playing vs human playing',default=False, required=False, type=bool)
    args = argparser.parse_args()
    automatic_game = args.automation
    main(automatic_game)
    
