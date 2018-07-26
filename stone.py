import collections
import json
class Player:
	'game players'
	playersCollection = {}
				
	def setPlayerForThisGame(self, index):
		# ask for username
		print("+ Press 0 to go back to menu +")
		usernameInput = input("Please enter player{} username: ".format(index))
		# if name not in collection, try again
		# logic problem here
		if Player.goBackToMenu(self, usernameInput):
			StoneGame._menu(self)
		while not Player.authentication(self, usernameInput) and not Player.goBackToMenu(self, usernameInput):
			print("!!! ERROR: username not found, please try again or press 0 to go back to menu. !!!")
			usernameInput = input("Please enter player{} username: ".format(index))
		# if name in collection, define username
		self.username = usernameInput
		print("*** Player verified! ***")
		return self.username		
	
	# player authentication
	def authentication(self, username):
		return username in Player.playersCollection

	def goBackToMenu(self, action):
		return True if action == '0' else False

	def addPlayer(self):
		userInput = input("Please enter new player username: ")
		# check username is not existed
		if Player.authentication(self, userInput):
			print("User exists, please try other username.")
			Player.addPlayer(self)
		# add to collection
		else: 
			print("*** New user added! Welcome {}! ***".format(userInput))
			Player.playersCollection[userInput] = { "wins": 0, "total games": 0, "rate": 0 }
			StoneGame._goBackToMenu(self)

	def displayPlayer(self):
		print("------------- Records ---------------")
		print("--- Player ------ Winning Rate ------")
		for player in Player.playersCollection:
			print("  {:<20}{}%".format(player, Player.playersCollection[player]["rate"]))
		print("-----------------------------------")
		StoneGame._goBackToMenu(self)

	def calculateWinsRate(self, player):
		return float(Player.playersCollection[player]["wins"]) / float(Player.playersCollection[player]["total games"]) * 100 if not Player.playersCollection[player]["total games"] == 0 else 0

	def sortByValue(self, dict):
		sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1][2], reverse=True)


class Game:
	__currentIsPlayer1 = True


	def __init__(self):
		self.gameSettings = {}
		Game.initSettings(self)


	# user input initial game settings
	def initSettings(self):
		self.gameSettings["player1"] = Player().setPlayerForThisGame(1)
		self.gameSettings["player2"] = Player().setPlayerForThisGame(2)
		try:
			self.gameSettings["total amount"] = input("Please enter total stone amount: ")
			self.gameSettings["upper bound"] = input("Please enter stone upper bound: ")
		except ValueError:
			print("!!! Invalid input. Please try again.")
			self.gameSettings["total amount"] = input("Please enter total stone amount: ")
			self.gameSettings["upper bound"] = input("Please enter stone upper bound: ")
		# sort dict after all inputs entered
		self.gameSettings = collections.OrderedDict(sorted(self.gameSettings.items()))
		# start game
		Game.gameStart(self)

	def gameStart(self):
		# set current stone amount to original amount
		self.gameSettings["current amount"] = self.gameSettings["total amount"]
		# display game info and then start game
		print("------------ GAME INFO ------------")
		for item in self.gameSettings:
			print("|  {}: {}".format(item, self.gameSettings[item])) 
		print("------------ GAME START -----------")
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
		Game.endGame(self, Game.returnCurrentPlayer(self))
		

	# display current stone
	def stoneController(self):
		print("Current stone amount: {}".format(self.gameSettings["current amount"]), end=" ")
		for i in range(int(self.gameSettings["current amount"])):
			print("*", end="")
		print()

	# return current player
	def returnCurrentPlayer(self):
		return "player1" if Game.__currentIsPlayer1 else "player2"

	# display and switch player
	def playerController(self):
		# display current player
		currentPlayer = Game.returnCurrentPlayer(self)
		print("{}'s turn!".format(self.gameSettings[currentPlayer]))
		# switch player
		Game.__currentIsPlayer1 = not Game.__currentIsPlayer1

	# calculate stone
	def stoneReducer(self):
		try:
			stoneToReduce = int(input("Please enter stone amount: "))
			self.gameSettings["current amount"] = int(self.gameSettings["current amount"]) - stoneToReduce
		except ValueError:
			print("!!! Invalid input. Please try again. !!!")
			Game.stoneReducer(self)

	# display winner
	def endGame(self, winner):
		# get loser
		Game.playerController(self)
		loser = Game.returnCurrentPlayer(self)
		# display winner
		print("*** {} wins! ***".format(self.gameSettings[winner]))
		# add to record
		Game.__processRecord(self, self.gameSettings[winner], True)
		Game.__processRecord(self, self.gameSettings[loser], False)

		# play again?
		Game.gameStart(self) if input("+ Play Again?(y/n) +") == "y" else StoneGame._menu(self)

	# update record after game
	def __processRecord(self, username, win):
		Player.playersCollection[username]["total games"] += 1
		if win:
			Player.playersCollection[username]["wins"] += 1
		Player.playersCollection[username]["rate"] = Player.calculateWinsRate(self, username)

class StoneGame:
	'main game system'
	def __init__(self):
		try:
			Player.playersCollection = json.load(open("records.txt", "r"))
		except:
			print("!!! ERROR: failed to open records file or file doesn't existreverse=True. !!!")
			pass

	def main(self):
		print("+ Welcome to Stone Game! +")
		# display menu
		StoneGame._menu(self)
		
	# enter 0 for game menu
	def _goBackToMenu(self):
		print("+ Press 0 to return to game menu. +")
		userInput = input()
		if userInput == '0':
			StoneGame._menu(self)
		else: 
			print("!!! Invalid input, please try again. !!!")
			StoneGame._goBackToMenu(self)

	# display game menu
	def _menu(self):
		# can re-write this part
		print("-----------------------------------")
		print("|             GAME MENU            |")
		print("-----------------------------------")
		print("|  Press 1 to Start A New Game     |")
		print("|  Press 2 to Display Records      |")
		print("|  Press 3 to Add A New Player     |")
		print("|  Press 4 to Battle With Computer |")
		print("|  Press 5 to Exit                 |")
		print("-----------------------------------")

		# process user action request
		StoneGame.processUserAction(self, input("> "))


	# process user action request
	def processUserAction(self, userActionInput):
		if userActionInput == '1':
			Game()
		elif userActionInput == '2':
			Player().displayPlayer()
		elif userActionInput == '3':
			Player().addPlayer()
		elif userActionInput == '4':
			pass
		elif userActionInput == '5':
			print("Bye!")
			StoneGame.__saveToFile(self)
			quit()
		else:
			print("!!! Input not found, please try again. !!!")
			StoneGame._menu(self)

	def __saveToFile(self):
		f = open("records.txt", "w")
		f.write(str(Player.playersCollection).replace("'", '"'))





newGame = StoneGame().main()

