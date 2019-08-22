from Node import Node
from OutOfRange import OutOfRange
class Trie:
	def __init__(self):
		self.node = Node()
	def getIndex(self, ch):
		if ord('a') <= ord(ch) <= ord('z'):
			return ord(ch) - ord('a')
		elif ord('A') <= ord(ch) <= ord('Z'):
			return ord(ch) - ord('A')
		return -1
	def insert(self, value):
		curr = self.node
		length = len(value)
		for i in range(length):
			index = self.getIndex(value[i])
			if index < 0 or index > 25: raise OutOfRange(value)
			if not curr.children[index]: curr.children[index] = Node()
			curr = curr.children[index]
		curr.end = True
	def search(self, value): 
		curr = self.node 
		length = len(value) 
		for i in range(length): 
		    index = self.getIndex(value[i])
		    if index < 0 or index > 25: raise OutOfRange(value)
		    if not curr.children[index]: return False
		    curr = curr.children[index] 
		return curr != None and curr.end