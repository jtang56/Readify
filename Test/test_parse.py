import unittest
import sys
import os
from parse_html import parse_html
from print_words import print_words

#Test the parser
class ParserTest(unittest.TestCase):
	#Testing that it parses into words
	def test_basic(self):
		word_list = parse_html("<p>hello world</p>")
		self.assertEquals(word_list[0], "hello")
		self.assertEquals(word_list[1], "world")

	#Testing that it does not return <div> tags
	def test_empty(self):
		word_list = parse_html("<div>asdfasafadf</div>")
		self.assertFalse(word_list)

	#Testing that info inside brackets is not included
	def test_things_inside_p(self):
		word_list = parse_html("<p class = blah>hello world</p>")
		self.assertEquals(word_list[0], "hello")
		self.assertEquals(word_list[1], "world")

#Test the printer
class PrintTest(unittest.TestCase):
	#Ensure that only three words are printed per line
	def test_print_three_words(self):
		word_list = parse_html("<p> hello hello hello hello hello hello </p>")
		sys.stdout = open("test.txt", "w")
		print_words(word_list, 3, 0)
		sys.stdout.close()
		f = open("test.txt", "r")
		lines = f.readlines()
		self.assertEquals(lines[0], "hello hello hello \n")
		f.close()
		os.remove("test.txt")

	#Ensure that only two words are printed per line
	def test_print_two_words(self):
		word_list = parse_html("<p> hello hello hello hello hello hello </p>")
		sys.stdout = open("test.txt", "w")
		print_words(word_list, 2, 0)
		sys.stdout.close()
		f = open("test.txt", "r")
		lines = f.readlines()
		self.assertEquals(lines[0], "hello hello \n")
		f.close()
		os.remove("test.txt")
