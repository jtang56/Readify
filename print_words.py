import time

#function to print the list at a given speed, and a certain number of words per line
#word_list: list of words
#num_words: number of words per line
#speed: delay between line prints
def print_words(word_list, num_words, speed):
	for i in range(0, len(word_list), num_words):
		for j in range(0, min(num_words, len(word_list) - i)):
			print word_list[i + j],
		print ''
		time.sleep(speed)
