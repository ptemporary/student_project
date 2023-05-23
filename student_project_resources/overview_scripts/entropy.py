import math

# Set of possible words
possible_words = ['apple', 'brain', 'siren', 'globe', 'speak', 'chair', 'flame', 'study', 'train', 'water']

def process_guess(solution, guess):
    result = ""
    # Write this functin yourself ;p

    return result

# Function to calculate the score of a guess based on the entropy reduction
def calculate_guess_entropy(guess, possible_words):
    # Calculate the number of words that would be eliminated for each possible result
    result_counts = {}
    for word in possible_words:
        result = process_guess(word, guess)  # Use your existing function
        if result not in result_counts:
            result_counts[result] = 0
        result_counts[result] += 1
    
    # Calculate the entropy of this guess
    entropy = 0
    for count in result_counts.values():
        p = count / len(possible_words)
        entropy += -p * math.log2(p)
    
    return entropy

# Function to guess a word based on entropy reduction
def guess_word_entropy(possible_words):
    min_entropy = float('inf')
    best_guess = None

    for word in possible_words:
        entropy = calculate_guess_entropy(word, possible_words)
        if entropy < min_entropy:
            min_entropy = entropy
            best_guess = word

    return best_guess, min_entropy

# Example usage
guessed_word, entropy = guess_word_entropy(possible_words)
print(f"Best Word: {guessed_word.upper()} with an entropy of: {entropy}")
