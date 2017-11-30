import bulls_and_cows as bc

def main():
# Do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('Would you like to play again? (y/n)')
    print('So long sucker!')

'''Plays one interactive game of bulls and cows on the console'''
def play_game():
    answer = bc.generate_secret()
    '''print("answer is", answer) print answer for testing purposes'''
    guess = input("What is your guess?: ")
    
    attempts = 0
    while guess != answer:
        bc.how_many_bulls(answer, guess)
        bc.how_many_cows(answer, guess)
        print("Try again!")
        attempts += 1
        print("Attempts:", attempts)
        guess = input("What is your guess?: ")
        ''' This allows the user to guess again'''
       
        
    if guess == answer:
        print("Your answer", guess, "was correct!")
        print ("Attempts:", attempts+1)
main()
