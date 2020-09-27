from tkinter import *

win = Tk()
win.title("Graphical_palindrome_checker")
win.resizable(width = False, height = False)

def reloadit():


	label1 = Label(win, text = "Input:")
	label1.grid(row = 0, column = 0, padx = 5, pady = 5)

	label2 = Label(win, text = "Output:")
	label2.grid(row = 1, column = 0, padx = 5)

	label1_entry = Entry(win, width = 50)
	label1_entry.grid(row = 0, column = 1, padx = (0,5))

	label2_entry = Entry(win, width = 50)
	label2_entry.grid(row = 1, column = 1, padx = (0,5))

	label0 = Label(win, text = "                            	                                             ")
	label0.grid(row = 2, column = 1)

	def clicked():

		# Palindrome main code \/

		input_str = label1_entry.get()
		rev = input_str[::-1] # reversing the string

		if input_str == rev:
			label0 = Label(win, text = "Yes, it's a palindrome")
			label0.grid(row = 2, column = 1)
			label2_entry.insert(0, rev)
		else:
			label0 = Label(win, text = "No, it's not a palindrome")
			label0.grid(row = 2, column = 1)
			label2_entry.insert(0, rev)

		# Palindrome main code /\

	answer = Label(win, text = "Result:")
	answer.grid(row = 2, column = 0, padx = 5, pady = (0,5))

	button = Button(win, text = "Check", command = clicked)
	button.grid(row = 3, column = 0, columnspan = 2, pady = 5, sticky = W, padx = 5)

	b2 = Button(win, text = "Reload", command = reloadit)
	b2.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = E)

b2 = Button(win, text = "Open", command = reloadit)
b2.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = E)

win.mainloop()