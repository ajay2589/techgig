class File:
	def __init__(self, loc):
		self.loc = self.correctedLoc(loc)
	def correctedLoc(self, l):
		return "/".join(l.split("\\"))
	def open(self):
		f = open(self.loc, 'r')
		self.handle = f
	def readLinesLazy(self):
		data = self.handle.readlines()
		return data
	def reset(self):
		self.handle.seek(0)
	def close(self):
		self.handle.close()
	def getWordsLazy(self):
		self.open()
		from re import findall, compile
		words = set()
		for line in self.readLinesLazy():
			for word in compile('\w+').findall(line):
				words.add(word)
		self.close()
		return words