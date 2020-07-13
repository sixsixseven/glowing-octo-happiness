import random as r
from os import name, system

def clear():
	""" Clears the display buffer. """
	# for windows 
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix') 
	else:
		_ = system('clear')

def isogramer(i):
	""" Returns 10 random isograms of the requested length. """
	clear()
	candidates = list()
	letter_count = dict()
	finals = list()
	#	Select words of correct length.
	for word in lst:
		if len(word) == i:
			candidates.append(word)
	#	Count each letter in the word.
	for word in candidates:
		for letter in word:
			if letter in letter_count:
				letter_count[letter] = letter_count[letter] + 1
			else:
				letter_count[letter] = 1

		if len(letter_count) == len(word):
			finals.append(word)
		letter_count = dict()

	try:
		choice = r.choices(finals, k = 10)
	except:
		print("There were no isograms for the length you specified.")
		return
	else:
		print("Total available words this set:", len(finals))
		return choice



#	#	#
web2 = open("/usr/share/dict/words", "r")
lst = list()

for item in web2:
	lst.append(item.rstrip().lower())

while True:
	try:
		isograms = isogramer(int(input("Isogram length (integer): ")))
	except KeyboardInterrupt:
		print("\nOk, bye :(\n")
		raise SystemExit
	except:
		clear()
		print("Try again. Maybe you didn't input an integer?")
		continue
	
	if isograms:
		for word in isograms:
			print("\n",word,"\n")
