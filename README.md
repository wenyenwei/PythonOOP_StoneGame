## Introduction
Stone Game - Python Object Oriented Programming Project
### Features
* #### Inheritance
Classes inheritance
* #### Exceptions
Input verification
* #### File I/O 
Read/write data from file
* #### AI player
Winning guaranteed algorithm
* #### Unittest
Python unit testing

## Installation
Please have python3 installed first.

Then cd to the directory and run:
* `python3 stone.py`

## Classes
There are four classes used in this program, including:
#### Player
username, records
```python
class Player:
	playersCollection = {'aaa': {'total games': 0, 'wins': 0, 'rate': 0}}
				
	def setPlayerForThisGame(self, index):
		# ask for username
		print("+ Press 0 to go back to menu +")
		usernameInput = input("Please enter player{} username: ".format(index))
		# if name not in collection, try again
		if Player.goBackToMenu(self, usernameInput):
			StoneGame._menu(self)
		while not Player.authentication(self, usernameInput) and not Player.goBackToMenu(self, usernameInput):
			print("!!! ERROR: username not found, please try again or press 0 to go back to menu. !!!")
			usernameInput = input("Please enter player{} username: ".format(index))
		# if name in collection, define username
		self.username = usernameInput
		print("*** Player verified! ***")
		return self.username		
    
    ...
```
#### Game 
game functions
```python
class Game:
	_currentIsPlayer1 = True


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
    ...
```
#### GameWithAI
inheritance from Game
```python
class GameWithAI(Game):
	def __init__(self):
		self.gameSettings = {}
		GameWithAI.initSettings(self)

	def initSettings(self):
		self.gameSettings["player1"] = Player().setPlayerForThisGame(1)
		self.gameSettings["player2"] = "Computer AI"
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
		GameWithAI.gameStart(self)
    ...
```
#### StoneGame 
main menu
```python
class StoneGame:
	def __init__(self):
		try:
			Player.playersCollection = json.load(open("records.txt", "r"))
		except:
			print("!!! ERROR: failed to open records file or file doesn't exist. !!!")
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
    ...
```

## Interface
#### Game Menu
```ruby
+ Welcome to Stone Game! +
-----------------------------------
|             GAME MENU            |
-----------------------------------
|  Press 1 to Start A New Game     |
|  Press 2 to Display Records      |
|  Press 3 to Add A New Player     |
|  Press 4 to Battle With Computer |
|  Press 5 to Exit                 |
-----------------------------------
```
## Unit Testing
Unit testing with Unittest.

A few simple unit test of Player class.

```python
from stone import *
import unittest

class TestPlayer(unittest.TestCase):
	""" Test Player Class Methods """

	def test_authentication(self):
		self.assertTrue(Player.authentication(self, 'aaa'))

	def test_goBackToMenu(self):
		self.assertTrue(Player.goBackToMenu(self, '0'))

	def test_calculateWinsRate(self):
		self.assertEqual(Player.calculateWinsRate(self, 'aaa'), 0)


if __name__ == '__main__':
	unittest.main()

```

Run:
* `python3 test.py`

Results: 
```ruby
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```
