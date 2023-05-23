# Define the letter frequency.
# Frequency data taken from Samuel Morse's frequency analysis of letters in typing samples
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html

letter_frequency = {
    'E': 12000, 'T': 9000, 'A': 8000, 'I': 8000, 'N': 8000, 'O': 8000, 'S': 8000,
    'H': 6400, 'R': 6200, 'D': 4400, 'L': 4000, 'U': 3400, 'C': 3000, 'M': 3000,
    'F': 2500, 'W': 2000, 'Y': 2000, 'G': 1700, 'P': 1700, 'B': 1600,
    'V': 1200, 'K': 800, 'Q': 500, 'J': 400, 'X': 400, 'Z': 200
}

# Set of possible words
possible_words = ['apple', 'brain', 'siren', 'globe', 'speak', 'chair', 'flame', 'study', 'train', 'water']

def calculate_word_score(word, letter_frequency):
    score = 0
    for letter in word:
        score += letter_frequency[letter.upper()]
    return score

def guess_word(possible_words, letter_frequency):
    max_score = 0
    best_guess = None

    for word in possible_words:
        score = calculate_word_score(word, letter_frequency)
        if score > max_score:
            max_score = score
            best_guess = word

    return best_guess, max_score

# Example usage
guessed_word, score = guess_word(possible_words, letter_frequency)
print(f"Best Word: {guessed_word.upper()} with a score of: {score}")