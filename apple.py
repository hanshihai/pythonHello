def apple():
	def banana():
		def orange():
			print("orange is here")
		print("banana is here")
		orange()
	print("apple is here")
	banana()
apple()
