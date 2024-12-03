import random

def get_word():
  """Choose a random word from a list."""
  words = ["python", "programming", "computer", "science", "skibidi", "sigma", "robot", "robotics", "crash", "fathom", "purple", "fathom" "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom" "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "fathom", "robot", "robotics", "crash", "fathom", "purple", "fathom"]
  return random.choice(words)

def play_hangman():
  """Runs the hangman game."""
  word = get_word()
  word_letters = set(word)  # Letters in the word
  alphabet = set(chr(x) for x in range(ord('a'), ord('z') + 1))  # All letters
  used_letters = set()  # What the user has guessed

  lives = 7

  # Getting user input
  while len(word_letters) > 0 and lives > 0:
    # Letters used
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    # Current word (e.g. 'p - t - o n')
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').lower()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print('')

      else:
        lives -= 1  # Takes away a life if wrong
        print('Letter is not in word.')

    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')

    else:
      print('Invalid character. Please try again.')

  # Gets here when len(word_letters) == 0 OR lives == 0
  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
    print('You guessed the word', word, '!!')

play_hangman()