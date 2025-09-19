import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import word_count, char_dict, sorted_dict

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def report(sorted_char,total_words):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	for letter in sorted_char:
		if letter["char"].isalpha():
			print(f"{letter["char"]}: {letter["num"]}")
	print("============= END ===============")

def main():

	text = get_book_text(sys.argv[1])
	total_words = word_count(text)
	total_char = char_dict(text)
	sorted_char = sorted_dict(total_char)
	report(sorted_char,total_words)


main()
