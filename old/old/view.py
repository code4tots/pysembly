#!/usr/bin/python

# Set up Tkinter and other relevant setup for this view.
from Tkinter import *
root = Tk()

frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

info = Text(frame) # Info bar
info.pack(side=RIGHT, fill=BOTH, expand=1)
info.config(state=DISABLED) # Make info read-only.

canvas = Canvas(frame)
canvas.pack(side=RIGHT, fill=BOTH, expand=1)

# Methods for getting information from the outside world.
IO = {} # All io variables will be nested here.
IO['infoText'] = '' # Text to be displayed by 'info'
IO['boxes'] = [] # List of boxes that needed to be displayed (only their names are on it).
IO['arrows'] = [] # List of box name pairs (srcBoxName, destBoxName).
IO['loc'] = {} # Location of all the 'boxes'; lookup by name.
IO['selected'] = ''

def setInfoText(infoText):
	IO['infoText'] = infoText
	draw()
	print 'draw was called.'
	print IO['infoText']
def newBox(name):
	IO['boxes'].append(name)
	draw()
def newArrow(src,dest):
	IO['arrows'].append( (src,dest) )
	draw()

# Draw. This should be called after anything gets updated.
def draw():
	# Set the text for info.
	info.delete(1.0, END)
	# temporarily enable info to write to it, write to it, then make it read-only again.
	info.config(state=NORMAL)
	info.insert(INSERT,IO['infoText'])
	info.config(state=DISABLED)
	
	# Draw the boxes.
	for boxName in IO['boxes']:
		if not (boxName in IO['loc']):
			IO['loc'][boxName] = ( int(canvas.cget("width")) / 2, int(canvas.cget("height")) / 2 )
		t = canvas.create_text(IO['loc'][boxName][1],IO['loc'][boxName][1],boxName)
		b = canvas.create_rectangle(canvas.bbox(t), fill="#%02x%02x%02x" % (0, 255, 0))
		canvas.tag_lower(b,t)

# Callbacks. Stuff to do when we interact with the program.
def selectBox(event):
	for name in IO['boxes']:
		IO['loc'][

# Register the callbacks.
#canvas.bind('<


# Some test.
newBox("Some box.")
setInfoText('Hello world.')

def run():
	mainloop()
	
if __name__ == '__main__':
	run()
