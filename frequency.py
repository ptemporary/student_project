"""
    Calculate the letter frequency of a given letter across all letters of all valid words.
    Since: May 22 2023
"""

TOTAL_CHARS = 64860

def main():
    """
        Main function.
        Calculate the frequency of each letter in alphabet from a list of valid words (# of occurences in word list / total # of chars in list).
    """
    alphabet = alphabet_freq()

    """
        Tests of functions.
    """
    print(alphabet)

    # beef_weight = get_weight("beefs", alphabet)
    # print(f"Weight of the word \"beefs\" is {beef_weight}")

    best_word, best_weight = top_word(alphabet)
    print(f"Best word is {best_word} --> {best_weight}%")

    # print(top_ten(alphabet))

def alphabet_freq(list_name):
    """
        Returns a dictionary of the alphabet with a frequency for every letter.
    """
    alphabet              = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    letter_frequency_dict = {} # letter:frequency

    # Get count of each letter in all valid words.
    for letter in alphabet:
        count                         = get_letter_frequency(letter, list_name)
        letter_frequency_dict[letter] = round(count / TOTAL_CHARS, 4)

    return letter_frequency_dict

def get_letter_frequency (letter, list_name):
    """
        Get the frequency of a given letter across all words in a list.
    """
    long_str = ""
    
    for word in list_name:
        long_str = long_str + word

    total = long_str.count(letter)

    return total


def get_weight (word, letter_frequency_dict):
    """
        Gets the weight of a Wordle word; expressed as a percentage.
    """
    weight = 0

    for letter in word:
        weight += letter_frequency_dict[letter]

    return weight


def top_ten (letter_frequency_dict):
    """
        Gets the top 10 most likely words to be correct.
        Starts w/ a list of 10 0.0 weighted values (all spaces).
        If the weight of list[0] (smallest value) is less than the contending word in the data file, the contending word is plugged into list[0].
        The list is then sorted; lowest value at list[0].

        TODO delete??
    """
    top_list = ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "] # 0.0 weight.

    # First data file.
    with open("student_project_resources/wordle_valid_words.txt", 'r') as file:

            for word in file:
                word             = word.strip()
                word             = word.lower()
                contender        = get_weight(word, letter_frequency_dict)
                smallest_in_list = get_weight(top_list[-1], letter_frequency_dict)

                if smallest_in_list < contender:
                    top_list[-1] = word
                    top_list.sort()

    # Second data file.
    with open("student_project_resources/wordle_common_words.txt", 'r') as file:

            for word in file:
                word             = word.strip()
                word             = word.lower()
                contender        = get_weight(word, letter_frequency_dict)
                smallest_in_list = get_weight(top_list[-1], letter_frequency_dict)

                if smallest_in_list < contender:
                    top_list[-1] = word
                    top_list.sort()

    return top_list


def top_word (letter_frequency_dict):
    """
        Finds the most likely word to be correct in Wordle from the given word lists.
    """
    best_word   = ""
    best_weight = 0.0

    with open("student_project_resources/wordle_valid_words.txt", 'r') as file:

        for word in file:
            word   = word.strip()
            word   = word.lower()
            weight = get_weight(word, letter_frequency_dict)

            if (best_weight < weight) and (True != find_dup(word)):
                best_word   = word
                best_weight = weight

    with open("student_project_resources/wordle_common_words.txt", 'r') as file:

        for word in file:
            word   = word.strip()
            word   = word.lower()
            weight = get_weight(word, letter_frequency_dict)

            if (best_weight < weight) and (True != find_dup(word)):
                best_word   = word
                best_weight = weight
                
    return best_word, best_weight


def find_dup(word):
    """ Returns True if there's duplicate letters in a word. """
    prev_letters = []

    for letter in word:
        if letter in prev_letters:
            return True
        
        prev_letters.append(letter)

    return False
        

if __name__ == "__main__":
    main()
