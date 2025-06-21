import requests

#Use an API
api_key = 'YOUR_API_KEY'

api_url = 'https://api.api-ninjas.com/v1/randomword'

#Make a request and get the response 
response = requests.get(api_url, headers={'X-Api-Key': api_key})

if response.status_code == requests.codes.ok:
    # get the word from the api
    word = response.json()['word'][0]
    print(word)
    
else:
    print("Error:", response.status_code, response.text)


# Initialize the display of the guessed word as underscores
guessedWord = ['_'] * len(word)

#elliminate the space to from guessedWord
if ' ' in word:
    for i in range(len(word)):
        if word[i] == ' ':
            guessedWord[i] = ' '

# Set the number of attempts (word length + 6 extra chances)
attempts = len(word) + 6

print("Attempts: " + str(attempts))

# Game loop - runs until attempts are finished
while attempts > 0: 
    # Display the current guessed word state
    print('\nCurrent Word = ' + ' '.join(guessedWord))
    
    # Take user input for a letter guess
    guess = input('Guess a letter: ').strip()

    # Check if guess is empty
    if not guess:
        print("Oops! You didn't type anything. Please enter a letter.")
        continue  # Skip the rest of the loop and prompt again

    # Check if the guessed letter is in the word (case-insensitive)
    if guess.upper() in word.upper(): 
        for i in range(len(word)): 
            if word[i].upper() == guess.upper():
                guessedWord[i] = word[i]  # Preserve original casing
        print('Great guess!')
    else: 
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    # Win condition: no more underscores left
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
    # Loss condition: no attempts left
    elif attempts == 0:
        print('\nYou\'ve run out of attempts! The word was: ' + word)


