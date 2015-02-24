class NumNode(object):
	"""NumNode is a class as an entry in the Board"""
	def __init__(self, col, row, value = 0, domain = [1,2,3,4,5,6,7,8,9], setupAlready = False):
		self.col = col
		self.row = row
		self.value = value
		self.domain = domain
		self.ValueSet = setupAlready

	def set_Node_value(self, value):
		if(self.ValueSet):
			raise Exception("This entry cannot be changed.")
		self.ValueSet = True
		self.value = value

	def remove_from_domain(self, value):
		try:
			self.domain.remove(value)
		except ValueError:
			raise ValueError("value doesnt exist in the domain.")
	
	def neighbours_coordinates_in_row(self):
		neighbours = [(col, self.row) for col in range(9)]
		neighbours.remove((self.col, self.row))
		return neighbours

	def neighbours_coordinates_in_col(self):
		neighbours = [(self.col, row) for row in range(9)]
		neighbours.remove((self.col, self.row))
		return neighbours

	def neighbours_coordinates_in_3by3(self):
		if(self.col < 3):
			if (self.row < 3):
				neighbours = [(col,row) for col in range(3) for row in range(0,3)]	
			elif (self.row < 6):
				neighbours = [(col,row) for col in range(3) for row in range(3,6)]
			else:
				neighbours = [(col,row) for col in range(3) for row in range(6,9)]
			neighbours.remove((self.col, self.row))
			return neighbours
		if(self.col < 6):
			if (self.row < 3):
				neighbours = [(col,row) for col in range(3,6) for row in range(0,3)]	
			elif (self.row < 6):
				neighbours = [(col,row) for col in range(3,6) for row in range(3,6)]
			else:
				neighbours = [(col,row) for col in range(3,6) for row in range(6,9)]
			neighbours.remove((self.col, self.row))
			return neighbours
		if(self.col < 9):
			if (self.row < 3):
				neighbours = [(col,row) for col in range(6,9) for row in range(0,3)]	
			elif (self.row < 6):
				neighbours = [(col,row) for col in range(6,9) for row in range(3,6)]
			else:
				neighbours = [(col,row) for col in range(6,9) for row in range(6,9)]
			neighbours.remove((self.col, self.row))
			return neighbours


	def __str__(self):
		return "Domain = " + str(self.domain) + ", value = " + str(self.value)



		