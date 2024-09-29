import random

START_RANGE = 1
END_RANGE = 10

def get_random_number():
  return random.randint(START_RANGE, END_RANGE)

def get_guess():
  while True:
    try:
      guess = int(input(f"Pick a number between {START_RANGE} and {END_RANGE}:  "))

      if guess < START_RANGE or guess > END_RANGE:
        raise ValueError(f"You entered a number outside of the guessing range: {START_RANGE} and {END_RANGE}")
    except ValueError as err:
      show_error(err)
      continue
    else:
      return guess

def start_game():
  guesses = 0
  scores = []
  random_number = get_random_number()
  numbers_used = [random_number]
  print("Welcome to the Number Guessing Game!")

  while True:
    guess = get_guess()
    guesses += 1
    if guess != random_number:
      print(f"Oops! It's {'higher' if random_number > guess else 'lower'} than {guess}...")
    else:
      print("Congratulations, you got it!")
      print(f"It took you {guesses} {'guess' if guesses == 1 else 'guesses'}.")

      if not replay():
        print("Thanks for playing!")
        break

      scores.append(guesses)
      random_number = get_random_number()

      while random_number == numbers_used[-1]:
        random_number = get_random_number()

      if len(numbers_used) > 1:
        print(f"Previous random numbers: {', '.join(map(str,numbers_used))}")


      print(f"Highest score: {min(scores) if len(scores) > 1 else guesses}")

      if len(scores) > 1:
        print(f"All scores: {', '.join(map(str,scores))}")

      numbers_used.insert(len(numbers_used), random_number)
      guesses = 0

      continue

def replay():
  is_playing = input("Would you like to continue playing? (Yes/No):  ")

  while is_playing != "yes".lower() and is_playing != "no".lower():
    is_playing = input("Please enter either 'Yes' or 'No':  ")

  return is_playing == "yes".lower()

def show_error(err):
  msg = str(err).lower()

  if "invalid" in msg:
    print("Uh oh! Looks like you didn't enter an integer, e.g. 5 or 05.")
    print(f"For you tech wizards out there: {err}")
  else:
    print(err)

start_game()