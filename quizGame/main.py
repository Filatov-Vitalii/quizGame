def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)

        chosen = input('\nEnter your answer: ')
        chosen = chosen.upper()

        if chosen == 'A' or chosen == 'B' or chosen == 'C' or chosen == 'D':
            print('')
        else:
            chosen = '-'

        guesses.append(chosen)

        correct_guesses += check_answer(questions.get(key), chosen)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT!')
        return 1
    else:
        print('WRONG!')
        return 0


def display_score(correct_guesses, guesses):
    print('-------------------------')
    print('RESULTS')
    print('-------------------------')

    print('Right answers: ', end = '')
    for i in questions:
        print(questions.get(i), end = ' ')
    print()

    print('Your answers: ', end='')
    for i in guesses:
        print(i, end=' ')
    print()

    if correct_guesses == 1:
        plural_or_singular = ''
    else:
        plural_or_singular = 's'

    print('You scored {} point{}'.format(correct_guesses, plural_or_singular))
    percent = int((correct_guesses/len(questions))*100)
    print('Correct answers rate: {}%'.format(percent))


def play_again():
    print()
    response = input('Do you want to play again? (Y/N) ')
    response = response.upper()

    if response == 'Y':
        return True
    else:
        return False

questions = {
    'Is the Earth round?' : 'B',
    'What famous US festival hosted over 350,000 fans in 1969?' : 'A',
    'What year was the very first model of the iPhone released?' : 'A',
    'Who was the first woman to win a Nobel Prize (in 1903)?' : 'D'
}

options = [['A. No', 'B. Yes', 'C. Sometimes', 'D. There is no Earth'],
           ['A. Woodstock', 'B. Stonestick', 'C. Tic-tac', 'D. Nashestvie'],
           ['A. 2007', 'B. 2005', 'C. 2000', 'D. 2010'],
           ['A. Rosalind Franklin', 'B. Kirstine Meyer', 'C. Margaretta Morris', 'D. Marie Curie']]

new_game()

while play_again():
    print()
    new_game()

print('\nThanks for playing! Goodbye')