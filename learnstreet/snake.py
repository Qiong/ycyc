#Snakes and Ladders Project
#The game consists of a 10x10 playing board of squares.
import random

def create_board_code():
    board=[]
    for i in range(0,100):
        obj = {}
        obj['end'] = i
        board.append(obj)
    # Set Snakes and Ladders, Offset is by 1
    # Ladders
    board[13]['end'] = 47
    board[18]['end'] = 59
    board[54]['end'] = 75
    board[68]['end'] = 89
    board[77]['end'] = 96
    # Snakes
    board[98]['end'] = 28
    board[46]['end'] = 17
    board[24]['end'] = 6
    return board
    
    #print board



def get_steps():
    #Select a random number from 1-6 and return that number.
    #This simulates the rolling of a single die.
	"REPLACE THIS CODE WITH YOUR METHOD"
	return random.randint(1,6)



def make_move(playerPos, steps1, steps2):
    #This method will move a player's piece across the board.
    #Imagine the player rolling two dice -- i.e., two calls to the get_steps()
    #method above. The values of those two rolls are "steps1" and "steps2".
    #The player's current board position is passed in as "playerPos".
    #This method adds steps1 and steps2 to playerPos. You will also need to
    #check the new player position against 99, which is as far as the board can go.
	"REPLACE THIS CODE WITH YOUR METHOD"

	steps1 = get_steps
	steps2 = get_steps
	if playerPos < 100:
		if playerPos == 99:
			playerPos = board[playerPos][end]
		elif playerPos == 47:
			playerPos = board[playerPos][end]
		elif playerPos ==24:
			playerPos = board[playerPos][end]
		else:
			playerPos = steps2 + steps1 + playerPos
	else:
		print 'you win'

def main():
	create_board_code()

if __name__ == '__main__':
	main()

