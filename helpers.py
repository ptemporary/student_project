def validate_guess(user_guess):
    if len(user_guess) != 5:
        print('Invalid guess length')
        return False
    
    common_file = open('student_project_resources/wordle_valid_words.txt', 'r')
    common_words = common_file.read().upper().split('\n')
    for word in common_words:
        if user_guess == word:
            return True
        else:
            print('Invalid word guess')
            return False
        

def process_guess(solution, guess):
    matching_letters = {}
    result = ''
    for i in range(len(solution)):
        if guess[i] in solution and guess[i] not in matching_letters.keys():
            matching_letters[guess[i]] = 0
        if guess[i] not in solution:
            result += '_'
        elif guess[i] == solution[i]:
            result += 'G'
            matching_letters[guess[i]] += 1
        else:
            result += 'X'
    if 'X' in result:
        for i in range(len(guess)):
            if result[i] == 'X':
                if matching_letters[guess[i]] < sum([1 for j in solution if j == guess[i]]):
                    result = result[:i] + 'Y' + result[i+1:]
                    matching_letters[guess[i]] += 1
                else:
                    result = result[:i] + '_' + result[i+1:]
            else:
                pass
    return result
    