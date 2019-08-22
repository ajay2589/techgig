class SaveReload:
	def __init__(self, loc):
		self.loc = self.correctedLoc(loc)
	def correctedLoc(self, l):
		return "/".join(l.split("\\"))
	def openforsave(self):
		f = open(self.loc, 'wb')
		self.handle = f
	def close(self):
		self.handle.close()
	def openforread(self):
		f = open(self.loc, 'rb')
		self.handle = f
	def save(self, obj):
		self.openforsave()
		from pickle import dump
		dump(obj, self.handle)
		self.close()
	def read(self):
		self.openforread()
		from pickle import load
		obj = load(self.handle)
		self.close()
		return obj