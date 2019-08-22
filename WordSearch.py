from Trie import Trie
from File import File
from SaveReload import SaveReload
from OutOfRange import OutOfRange
class WordSearch:
	def __init__(self):
		self.trie = Trie()
	def read(self):
		print('Enter the input file location. eg: C:/Users/Ajay/Desktop/ph.txt')
		inp =  str(input())
		try:
			f = File(inp)
		except Exception:
			print('Enter a valid file name')
			return
		words = f.getWordsLazy()
		for word in words:
			try:
				self.trie.insert(word)
			except OutOfRange as err:
				print(err.value + ' is not a valid word')
				#pass
		print('READ COMPLETED')
	def search(self):
		print('Enter the word to be searched')
		inp = str(input())
		res = False
		try:
			res = self.trie.search(inp)
		except OutOfRange as err:
			pass
		if res:
			print('Word ' + str(inp) + ' is present')
		else:
			print('Word ' + str(inp) + ' is NOT present')
	def save(self):
		print('Enter the input file location where the words have to be stored. eg: C:/Users/Ajay/Desktop/pic.dat')
		inp = str(input())
		try:
			save = SaveReload(inp)
			save.save(self.trie)
		except:
			print('Exception occured during save')
		print('SAVE COMPLETED')
	def load(self):
		print('Enter the input file location to load the words. eg: C:/Users/Ajay/Desktop/pic.dat')
		inp = str(input())
		save = SaveReload(inp)
		self.trie = save.read()
		#print('Exception occured during load')
		print('LOAD COMPLETED')
	def main(self):
		while True:
			print('Menu')
			print('1. Enter the input file with location')
			print('2. Enter the word to be searched')
			print('3. Save the resource into a location')
			print('4. Load the resource file')
			print('5. Exit')
			inp = str(input())
			if inp == '1':
				self.read()
			elif inp == '2':
				self.search()
			elif inp == '3':
				self.save()
			elif inp == '4':
				self.load()
			elif inp == '5':
				return
			else:
				continue
if __name__ == '__main__':
	w = WordSearch()
	w.main()

