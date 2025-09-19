def key_type(a):
	return a["num"]

def sorted_dict(all_characters):
	dict_list = []
	for a, b in all_characters.items():
		temp_dict = {"char": a, "num": b}
		dict_list.append(temp_dict)
	dict_list.sort(reverse=True, key=key_type)
	return(dict_list)


def char_dict(file_contents):
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
	return(num_words)

