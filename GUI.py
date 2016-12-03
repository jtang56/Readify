from Tkinter import *
import os.path
import os
import geturl
import print_words
import parse_html
import parse_file
import time
from functools import partial

highlight_colors = [
	"red",
	"blue",
	"cyan",
	"yellow",
	"green"
]

#destroys everything in the window
def destroy_widgets():
	for widget in root.winfo_children():
		widget.destroy()

#method to sleep for 3 seconds to pause ouput
def pause():
	time.sleep(3)

#saves the current output to file to resume later
def save(words):
	f = open("continue_text.txt", "w")
	for word in words:
		f.write(word + "\n")
	f.close()

	#calls function to return to menu
	setup_screen()

#print words to screen
def print_words(word_list, num_words, speed, color):
	for i in range(0, len(word_list), num_words):
		sentence = ''
		temp_list = []
		for j in range(0, min(num_words, len(word_list) - i)):
			sentence += word_list[i + j] + " "
			temp_list.append(word_list[i + j])
		pos_end = 1.0

		for j in range(len(temp_list)):
			text = Text(root, height = 5, width = 25)
			text.tag_config("highlight", background = color)
			text.configure(font = ("Courier New", 40, "bold"))
			text.insert(1.0, sentence)
			text.pack()
			pos_start = text.search(temp_list[j], pos_end, END)
			offset = '+%dc' % len(temp_list[j])
			pos_end = pos_start + offset
			text.tag_add("highlight", pos_start, pos_end)

			#setup buttons for commands during print
			save_file_action = partial(save, word_list[i:])
			b1 = Button(root, text = 'Cancel', command = setup_screen)
			b2 = Button(root, text = 'Pause 3 sec', command = pause)
			b3 = Button(root, text = 'Save to file', command = save_file_action)

			b2.pack()
			b1.pack()
			b3.pack()
			root.update_idletasks()
			root.update()
			time.sleep(speed / len(temp_list))
			destroy_widgets()

	time.sleep(2)

	option_screen()

#handles submission of file
def submit_file(event = None):
	which_file = e0.get()
	num_words = e1.get()
	speed = e2.get() / 10.0
	color = drop.get()

	words = parse_file.parse_file(which_file)
	destroy_widgets()

	print_words(words, int(num_words), float(speed), color)

#handles submission of file when the file is being resumed
def submit_file_resume(event = None):
	#this will always be the 'resume' file and it will always be the one that is saved to
	which_file = "continue_text.txt"

	num_words = e1.get()
	speed = e2.get() / 10.0
	color = drop.get()

	words = parse_file.parse_file(which_file)
	#remove the file so we can save to it later on if we choose to
	os.remove("continue_text.txt")
	destroy_widgets()

	print_words(words, int(num_words), float(speed), color)

#handles submission of webpage html
def submit_webpage(event = None):
	url = e0.get()
	num_words = e1.get()
	speed = e2.get() / 10.0
	color = drop.get()

	data = geturl.queryURL(url)
	words = parse_html.parse_html(data)
	destroy_widgets()

	print_words(words, int(num_words), float(speed), color)

#handles when file is chosen
def file_handle():
	global e0, e1, e2, drop
	destroy_widgets()
	root.bind("<Return>", submit_file)
	Label(root, text = "Enter File Name").grid(row = 0)
	Label(root, text = "Enter Num of Words").grid(row = 1)
	Label(root, text = "Enter Speed").grid(row = 2)
	Label(root, text = "Highlight color").grid(row = 3)

	#setup entry for file name
	e0 = Entry(root)
	e0.grid(row = 0, column = 1)
	e0.insert(10, "temp.txt")

	#setup entry for number of words per line
	e1 = Scale(root, from_= 1, to = 10, orient = HORIZONTAL)
	e1.set(3)
	e1.grid(row = 1, column = 1)

	#setup entry for speed
	e2 = Scale(root, from_= 1, to = 20, orient = HORIZONTAL)
	e2.set(7)
	e2.grid(row = 2, column = 1)

	drop = StringVar()
	dropdown = OptionMenu(root, drop, *highlight_colors)
	dropdown.grid(row = 3, column = 1)

	#setup submit button
	Button(root, text = 'Submit', command = submit_file).grid(row = 4, column = 0, sticky = W)
	#setup back button
	Button(root, text = 'Back', command = option_screen).grid(row = 4, column = 2, sticky = W)

	root.mainloop()

#handles when webpage is chosen
def webpage_handle():
	global e0, e1, e2, drop
	destroy_widgets()
	#setup input boxes
	root.bind("<Return>", submit_webpage)
	Label(root, text = "Enter URL").grid(row = 0)
	Label(root, text = "Enter Num of Words").grid(row = 1)
	Label(root, text = "Enter Speed").grid(row = 2)
	Label(root, text = "Highlight color").grid(row = 3)

	#setup entry for webpage name
	e0 = Entry(root)
	e0.grid(row = 0, column = 1)
	e0.insert(10, "https://www.facebook.com")

	#setup entry for number of words per line
	e1 = Scale(root, from_= 1, to = 10, orient = HORIZONTAL)
	e1.set(3)
	e1.grid(row = 1, column = 1)

	#setup entry for speed
	e2 = Scale(root, from_= 1, to = 20, orient = HORIZONTAL)
	e2.set(7)
	e2.grid(row = 2, column = 1)

	drop = StringVar()
	dropdown = OptionMenu(root, drop, *highlight_colors)
	dropdown.grid(row = 3, column = 1)

	#setup submit button
	Button(root, text = 'Submit', command = submit_webpage).grid(row = 4, column = 0, sticky = W)

	#setup back button
	Button(root, text = 'Back', command = option_screen).grid(row = 4, column = 2, sticky = W)

	root.mainloop()

#handles when resume file is chosen
def resume_file():
	global e1, e2, drop
	destroy_widgets()
	root.bind("<Return>", submit_file)
	Label(root, text = "Enter Num of Words").grid(row = 1)
	Label(root, text = "Enter Speed").grid(row = 2)
	Label(root, text = "Highlight color").grid(row = 3)

	#setup entry for number of words per line
	e1 = Scale(root, from_= 1, to = 10, orient = HORIZONTAL)
	e1.set(3)
	e1.grid(row = 1, column = 1)

	#setup entry for speed
	e2 = Scale(root, from_= 1, to = 20, orient = HORIZONTAL)
	e2.set(7)
	e2.grid(row = 2, column = 1)

	drop = StringVar()
	dropdown = OptionMenu(root, drop, *highlight_colors)
	dropdown.grid(row = 3, column = 1)

	#setup submit button
	Button(root, text = 'Submit', command = submit_file_resume).grid(row = 4, column = 0, sticky = W)
	#setup back button
	Button(root, text = 'Back', command = option_screen).grid(row = 4, column = 2, sticky = W)

	root.mainloop()

#option screen after the first page
def option_screen():
	destroy_widgets()
	#if there is no restart file
	if not os.path.isfile("continue_text.txt"):
		Label(root, text = "Read .txt file or webpage?").place(relx = 0.5, rely = 0.4, anchor = CENTER)

		Button(root, text = 'File', command = file_handle).place(relx = 0.3, rely = 0.5, anchor = CENTER)
		Button(root, text = 'Webpage', command = webpage_handle).place(relx = 0.7, rely = 0.5, anchor = CENTER)

	#if there is a restart file, need to add some more options
	else:
		Label(root, text = "Read .txt file or webpage or resume saved file?").place(relx = 0.5, rely = 0.4, anchor = CENTER)

		Button(root, text = 'File', command = file_handle).place(relx = 0.2, rely = 0.5, anchor = CENTER)
		Button(root, text = 'Webpage', command = webpage_handle).place(relx = 0.5, rely = 0.5, anchor = CENTER)
		Button(root, text = 'Resume', command = resume_file).place(relx = 0.8, rely = 0.5, anchor = CENTER)

	root.update()

#first page to user
def setup_screen():
	destroy_widgets()
	root.title("Readify")
	root.geometry("500x500")

	l1 = Label(root, text = "Welcome!")
	l1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
	l1.config(font=("Courier New", 45))
	l2 = Label(root, text = "Jeremy Tang")
	l2.place(relx = 0.5, rely = 0.9, anchor = CENTER)
	l2.config(font=("Courier New", 15))

	Button(root, text = 'Start!', command = option_screen).place(relx = 0.5, rely = 0.5, anchor = CENTER)
	root.mainloop()

if __name__ == "__main__":
	#create a new window, go to main title page
	root = Tk()
	setup_screen()
