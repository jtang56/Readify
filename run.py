from parse_html import parse_html
from print_words import print_words

#Main method for running application
if __name__ == '__main__':
	words = parse_html()
	num_words = input("Please input the number of words at a time: ")
	speed = input("Please input the delay between lines: ")
	print_words(words, int(num_words), float(speed))

