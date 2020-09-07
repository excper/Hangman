from random_words import RandomWords

class Hangman():
	def __init__(self):
		self.hidden_word = []
		self.word = RandomWords().random_word()
		self.hidden_word = ["_ "] * len(self.word)
#

	def showHiddenWord(self):
		print(f"Current word: " + "".join(self.hidden_word))

	def checkGuess(self, letter):
		if letter not in self.word:
			return False
		else:
			for i in range(len(self.word)):
				if self.word[i] == letter:
					self.hidden_word[i] = letter + " "
			return True

	def getResult(self):
		if not "_ " in self.hidden_word:
			return True
		else:
			return False
	def showWord(self):
		print(f"The word is: {self.word}.")
	def clear():

		print("\n")
		

class Player():
	def __init__(self):
		self.guessed_letter = []
		try:
			value = int(input("Input difficulty(1 for simplest, 3 for most difficult): "))
			if value == 1:
				self.lives = 14
			elif value == 2:
				self.lives = 10
			elif value == 3:
				self.lives = 7
			else:
				print("Your input is invalid, you get the most difficult difficulty!")
				self.lives = 7
		except:
			print("Your input is invalid, so you get the most difficult difficulty!")
			self.lives = 7

	#isAlive = lambda x: True if lives > 0 else False
	def isAlive(self):
		if self.lives > 0:
			return True
		else:
			return False

	def guessLetter(self):
		if len(self.guessed_letter) > 0:
			print(f"Your guessed letter(s): " + "".join(self.guessed_letter))
		value = input("Please input a letter to guess: ")
		while value in self.guessed_letter:
			value = input("Your guessed letter has been guessed, please re-enter another letter: ")
		self.guessed_letter.append(value)
		return value
	
	def loseLife(self):
		self.lives -= 1

	def showLives(self):
		print(f"Your lives: {self.lives}")



game_continue = True
while game_continue:

	hangman = Hangman()
	player = Player()

	while player.isAlive():
		Hangman.clear()
		hangman.showHiddenWord()
		player.showLives()
		if not hangman.checkGuess(player.guessLetter()):
			print("Your guess is wrong, you lose a life.")
			player.loseLife()
		else:
			print("Your guess is right.")
			if  hangman.getResult(): #Game not over
				print("You win!")
				break
	if not player.isAlive():
		print("You lose.")
	hangman.showWord()
	if input("Input q for quit: ") == "q":
		game_continue = False
print("Goodbye, thanks for your playing.")







