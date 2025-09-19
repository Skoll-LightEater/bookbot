def letter_count(file_contents):
	all_characters = {}
	for letter in file_contents.lower():
		if letter not in all_characters:
			all_characters[letter] = 1
		else:
			all_characters[letter] += 1
	return(all_characters)

def word_count(file_contents):
	num_words = 0
	for word in file_contents.split():
		num_words += 1
	print(f"{num_words} words found in the document")
	all_characters = letter_count(file_contents)
	return(all_characters)
