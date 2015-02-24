import copy
from numnode import NumNode

"""
Board[col][row] gives all possible values still in the domain of entry at [col][row].
[0][0] is the bottom left of the board. hence the first component indicates how far left
from the origin the entry is and the second component is how far up the board we are from
the origin.

"""
testBoard1 = ["3 _ _ 9 _ 2 _ _ 5","_ _ 1 _ _ _ _ _ _","_ 5 2 _ _ _ _ 9 _","_ 4 8 _ 2 _ 1 _ 3","_ _ _ _ 7 _ _ _ _","5 _ 9 _ 3 _ 7 8 _","_ 1 _ _ _ _ 6 5 _","_ _ _ _ _ _ 4 _ _","8 _ _ 4 _ 6 _ _ 7"]
testBoard2 = ["_ 9 _ _ 7 _ _ 2 _","_ 4 6 _ 5 _ 1 8 _","_ _ 2 1 4 9 3 _ _","9 _ 8 _ _ _ 7 _ 5","_ _ 4 _ 3 _ 2 _ _","5 _ 7 _ _ _ 6 _ 1","_ _ 9 5 6 2 8 _ _","_ 6 5 _ 9 _ 4 7 _","_ 8 _ _ 1 _ _ 5 _"]
testBoard3 = ["3 7 4 1 6 8 9 5 2","8 2 6 _ _ _ 1 3 7","5 _ 1 _ 3 7 8 _ _","6 3 7 _ _ _ 2 8 5","_ 5 9 3 8 2 6 _ _","4 8 2 6 7 5 3 1 9","2 _ 8 5 _ 6 7 _ 3","7 6 3 _ 9 4 5 2 1","9 1 5 7 2 3 4 6 8"]
def run_sudoku():
	EntriesFinalised = 0
	Board = []
	for row in range(9):
		entire_row = []
		for col in range(9):
			entire_row.append(NumNode(col, row))
		Board.append(entire_row)
	print("Please enter your entries for the board starting from the bottom row moving left to right.")
	print("Numbers must be between 1 and 9 inclusive seperated by spaces. Blank values should be entered as an _ (underscore)")
	for row in range(9):
		print("Row " + str(row+1) + " entries?")
		#entries = testBoard[row]
		#entries = testBoard2[row]
		entries = testBoard3[row]
		#entries = raw_input()
		entries += " "
		for col in range(9):
			try:
				numValue = int(entries[0:entries.index(' ')])
				Board[col][row].set_Node_value(numValue)
				EntriesFinalised += 1
			except ValueError:
				pass
			entries = entries[entries.index(' ') + 1:]
	print_board(Board)
	solve_board(Board, EntriesFinalised)



def solve_board(board, entriesfinalised):
	def get_entry(colx, rowy):
		return board[colx][rowy]
	

	print(entriesfinalised)
	print(get_entry(3,1).domain)
	for row in range(9):
		for col in range(9):
			entry = board[col][row]
			if (entry.ValueSet):
				valueToPrune = entry.value
				for each_relative in entry.neighbours_coordinates_in_row():
					try:
						get_entry(*each_relative).remove_from_domain(valueToPrune)
						
					except ValueError:
						pass
				for each_relative in entry.neighbours_coordinates_in_col():
					try:
						get_entry(*each_relative).remove_from_domain(valueToPrune)
						
					except ValueError:
						pass
				for each_relative in entry.neighbours_coordinates_in_3by3():
					try:
						get_entry(*each_relative).remove_from_domain(valueToPrune)
						
					except ValueError:
						pass
			#print(entry.domain)
	print(entriesfinalised)
	print_board(board)
	print(get_entry(3,1).domain)
	print(get_entry(3,1).value)
	while entriesfinalised < 81:
		for col in range(9):
			for row in range(9):
				entry = board[col][row]
				if (entry.ValueSet):
					continue
				if (len(entry.domain) == 1):
					valueToSet = entry.domain[0]
					entry.set_Node_value(valueToSet)
					entriesfinalised += 1
					print(entriesfinalised)
					for each_relative in entry.neighbours_coordinates_in_row():
						try:
							get_entry(*each_relative).remove_from_domain(valueToPrune)
							
							
						except ValueError:
							pass	
					for each_relative in entry.neighbours_coordinates_in_col():
						try:
							get_entry(*each_relative).remove_from_domain(valueToPrune)
							
							
						except ValueError:
							pass
					for each_relative in entry.neighbours_coordinates_in_3by3():
						try:
							get_entry(*each_relative).remove_from_domain(valueToPrune)
							
							
						except ValueError:
							pass

	print_board(board)
	


def print_board(boardRep):
	print("----------------------------")
	for row in range(8,-1,-1):
		rowString = "| "
		for col in range(0,3,1):
			rowString += str(boardRep[col][row].value) + " "
		rowString += " | "
		for col in range(3,6,1):
			rowString += str(boardRep[col][row].value) + " "
		rowString += " | "
		for col in range(6,9,1):
			rowString += str(boardRep[col][row].value) + " "
		rowString += " |"
		print(rowString)
	print("____________________________")



run_sudoku()