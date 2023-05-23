# Define the 2-gram frequency.
bigram_frequency = {
    'AP': 500, 'PP': 400, 'PL': 300, 'LE': 200,
    'BR': 600, 'RA': 700, 'AI': 800, 'IN': 900,
    'SI': 550, 'IR': 450, 'RE': 350, 'EN': 250,
    'GL': 650, 'LO': 750, 'OB': 850, 'BE': 950,
    'SP': 520, 'PE': 420, 'EA': 320, 'AK': 220,
    'CH': 620, 'HA': 720, 'RS': 820, 'ME': 210,
    'FL': 510, 'LA': 410, 'AM': 310, 'MB': 230,
    'ST': 610, 'TU': 710, 'UD': 810, 'DY': 910,
    'TR': 560, 'RO': 460, 'IT': 360, 'VE': 260,
    'WA': 630, 'AT': 730, 'TE': 830, 'ER': 930,
}


# Set of possible words
possible_words = ['apple', 'brain', 'siren', 'globe', 'speak', 'chair', 'flame', 'study', 'train', 'water']

def calculate_word_score(word, bigram_frequency):
    score = 0
    # Create 2-grams from the word
    bigrams = [word[i:i+2] for i in range(len(word)-1)]
    for bigram in bigrams:
        score += bigram_frequency.get(bigram.upper(), 0)  # Use get to avoid KeyError for unseen bigrams
    return score

def guess_word(possible_words, bigram_frequency):
    max_score = 0
    best_guess = None

    for word in possible_words:
        score = calculate_word_score(word, bigram_frequency)
        if score > max_score:
            max_score = score
            best_guess = word

    return best_guess, max_score

# Example usage
guessed_word, score = guess_word(possible_words, bigram_frequency)
print(f"Best Word: {guessed_word.upper()} with a score of: {score}")
