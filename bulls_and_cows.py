import random
'''
Generates a 4 digit number with no repeat digits It converts the number to a 
string and returns it
'''
def generate_secret():
    secret = random.randint(1000, 9999)
    secret_str = str(secret)
    secret_set = {secret_str[0], secret_str[1], secret_str[2], secret_str[3]}
    '''
    Using a set allows for the code to check for unique values. 
    A length of 4 means there are 4 unique values   
    '''
    while len(secret_set) != 4:
        secret = random.randint(1000, 10000)
        secret_str = str(secret)
        secret_set =  {secret_str[0], secret_str[1], secret_str[2], 
                       secret_str[3]}
    if len(secret_set) == 4:
        secret = secret_str
        return secret


def how_many_bulls(answer, guess):  
    bulls = 0
    for i in range(len(guess)):
        if answer[i] == guess[i]:
            bulls += 1 
    print("Bulls:", bulls)
    return bulls 
    '''
    This loop checks and compares digit in answer to digit in guess within
    the range of len of guess 
    '''

def how_many_cows(answer, guess):
    cows = 0
    for i in range(len(guess)):
        if answer[i] in guess:
            cows += 1
        '''Checks if the guess is in the answer'''
        if answer[i] == guess[i]:
            cows = cows -1
        '''This removes any instances of a digit being a bull and cow, 
        and also accounts for repeat digits'''
    print("Cows:", cows)
    return cows

