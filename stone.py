import collections
class Player:
	'game players'
	playersCollection = {}

	def __init__(self, index):
		# ask for username
		usernameInput = input("Please enter player{} username: ".format(index))
		# if name not in collection, try again
		# logic problem here
		while not Player.authentication(self, usernameInput) and not Player.goBackToMenu(self, usernameInput):
			usernameInput = input("Please enter player{} username: ".format(index))
		# if name in collection, define username
		self.username = iusernameInput			

	# player authentication
	def authentication(self, username):
		if not username in Player.playersCollection:
			print("ERROR: username not found, please try again or press 0 to go back to menu.")
		return username in Player.playersCollection

	def goBackToMenu(self, action):
		if action == '0':
			StoneGame._menu(self)
		else:
			return False


class Game:
	__currentIsPlayer1 = True


	def __init__(self):
		self.gameSettings = {}
		Game.initSettings(self)


	# user input initial game settings
	def initSettings(self):
		self.gameSettings["player1"] = Player(1)
		self.gameSettings["player1"] = Player(2)
		self.gameSettings["total amount"] = input("Please enter total stone amount: ")
		self.gameSettings["upper bound"] = input("Please enter stone upper bound: ")
		# sort dict after all inputs entered
		self.gameSettings = collections.OrderedDict(sorted(self.gameSettings.items()))

	def gameStart(self):
		print("======= GAME INFO ========")
		# display game info and then start game
		for item in self.gameSettings:
			print("{}: {}".format(item, self.gameSettings[item])) 
		print("======= GAME START =======")
		# set current stone amount to original amount
		self.gameSettings["current amount"] = self.gameSettings["total amount"]
		# start game process
		Game.gameProcessor(self)

	def gameProcessor(self):
		while int(self.gameSettings["current amount"]) > 0:		
			# display current stone amount
			Game.stoneController(self)
			# display current player
			Game.playerController(self)
			# Call stone reducer to calculate stone amount
			Game.stoneReducer(self)
		# end game function
		

	# display current stone
	def stoneController(self):
		print("Current stone amount: {}".format(self.gameSettings["current amount"]), end="")
		for i in range(int(self.gameSettings["current amount"])):
			print("*", end="")
		print()

	# display and switch player
	def playerController(self):
		# display current player
		currentPlayer = "player1" if Game.__currentIsPlayer1 else "player2"
		print("{}'s turn!".format(self.gameSettings[currentPlayer]))
		# switch player
		Game.__currentIsPlayer1 = not Game.__currentIsPlayer1

	# calculate stone
	def stoneReducer(self):
		stoneToReduce = int(input("Please enter stone amount: "))
		self.gameSettings["current amount"] = int(self.gameSettings["current amount"]) - stoneToReduce

	# display winner
	def endGame(self, winner):
		# display winner
		print("{} wins!".format(winner))

	# display all records
	def displayRecord(self):
		pass



class StoneGame:
	'main game system'
	__menu = {
		"Press 1 to Start A New Game": 1,
		"Press 2 to Display Records": 2,
		"Press 3 to Add A New Player": 3,
		"Press 4 to Battle With Computer": 4,
		"Press 5 to Exit": 5
	}

	def main(self):
		print("Welcome to Stone Game!")
		# display menu
		StoneGame._menu(self)
		
	# display game menu
	def _menu(self):
		# can re-write this part
		print("Press 1 to Start A New Game")
		print("Press 2 to Display Records")
		print("Press 3 to Add A New Player")
		print("Press 4 to Battle With Computer")
		print("Press 5 to Exit")

		# process user action request
		StoneGame.processUserAction(input("> "))

	# process user action request
	def processUserAction(userActionInput):
		return {
			"Press 1 to Start A New Game": Game(),
			"Press 2 to Display Records": 2,
			"Press 3 to Add A New Player": 3,
			"Press 4 to Battle With Computer": 4,
			"Press 5 to Exit": quit()
		}[userActionInput]



newGame = StoneGame().main()

