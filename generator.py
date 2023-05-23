
#! /usr/bin/env python3

"""
    Brief: Generates a guess for a Wordle word.  There are 2 classes, one to
    take CLI input as a guess if a human is playing.  The second class is for an 
    automated "Wordle cracker" computer program to generate a word guess.
    Since: 5/19/2023
    TODO make "Machine" class for automated Worlde solver.
"""

import frequency
# from random import choice

WORD_LEN = 5


class Machine_Guess:
    """
        A class specifically designed to handle automated input (word guesses) 
        from another program.from random import choice
    """
    guess_no = 0

    def valid_word(self, input):
        """
            Checks if inputted word is in the list of valid Wordle words.
            Checks 2 text files of un/common words.
        """
        is_valid = False

        # File 1
        with open("student_project_resources/wordle_common_words.txt", "r") as file:
            common_words = file.read()
            found = common_words.find(input)

            if -1 != found:
                is_valid = True

        # File 2
        with open("student_project_resources/wordle_valid_words.txt", "r") as file:
            valid_words = file.read()
            found = valid_words.find(input)

            if -1 != found:
                is_valid = True

        return is_valid

    def new_word(self, guess_no):
        """
            Gets user input.  Enforces input to be 5 letters long, composed of 
            only letters, and must be in either the common/valid words list.
        """
        alphabet = frequency.alphabet_freq()
        word     = frequency.top_word(alphabet) # Most likely correct guess.

        #while True:
        return word


class Human_Guess:
    """
        A class specifically designed to handle human user input (word guesses) 
        from the CLI.
    """

    def valid_word(self, input):
        """
            Checks if inputted word is in the list of valid Wordle words.
            Checks 2 text files of un/common words.
        """
        is_valid = False

        # File 1
        with open("student_project_resources/wordle_common_words.txt", "r") as file:
            common_words = file.read()
            found = common_words.find(input)

            if -1 != found:
                is_valid = True

        # File 2
        with open("student_project_resources/wordle_valid_words.txt", "r") as file:
            valid_words = file.read()
            found = valid_words.find(input)

            if -1 != found:
                is_valid = True

        return is_valid

    def new_word(self):
        """
            Gets user input.  Enforces input to be 5 letters long   """
        while True:
            word = input().upper().strip()

            if WORD_LEN != len(word):
                print("ERROR: word must be 5 letters, try again.\n")
            elif False == word.isalpha():
                print("ERROR: word must contain only letters, try again.\n")
            elif False == self.valid_word(word):
                print("ERROR: invalid word, try again.\n")
            else:
                pass

            break

        return word


# Test; delete for final product.
# if __name__ == "__main__":
#     human = Human_Guess()
#     print(human.new_word())
