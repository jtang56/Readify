from bs4 import BeautifulSoup
from geturl import queryURL

#Either given the html source as an argument, or queries from user
#Uses BeautifulSoup to look for tags <p>
#Iterates through all <p> tags, gets information and removes whitespace
#Returns a final list of words of information in <p> tags
#parameter html: html code passed through, default queries user for URL
def parse_html(html):
	soup = BeautifulSoup(html, 'html.parser')
	paragraphs = soup.find_all('p')

	combined_word = []
	final_paragraph = []

	for val in paragraphs:
		word_list = val.text.split()
		for word in word_list:
			combined_word.append(word)

	for i in range(len(combined_word)):
		final_paragraph.append(combined_word[i].strip('\n'))

	return final_paragraph


