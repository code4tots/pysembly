#!/usr/bin/python
# 4.13.2012
# view.py
# View for pysembly.
#
# I currently redraw the entire screen everytime there is an update.
# But later, I may redesign it so that the screen update info is split up
# into each update method. That way, when there is an update, only the 
# part that needs to be updated will be updated.

# Setup Tkinter stuff.
from Tkinter import *
root = Tk()
frame = Frame(root)
info = Text(frame)
canvas = Canvas(frame)

frame.pack(fill=BOTH, expand=1)
info.pack(side=RIGHT, fill=BOTH, expand=1)
info.config(state=DISABLED) # Make info read-only.
canvas.pack(side=RIGHT, fill=BOTH, expand=1)

# Internal representation.
X = {} # All global variables will be saved here.
X['box'] = {} # name of box -> (x,y) (location of box)
X['bbox'] = {}
X['arr'] = [] # List of (src,dest) pairs.
X['inf'] = '' # info Text.
X['x0'] = 0 # Upper Lefthand Corner (x0 -> 0)
X['y0'] = 0 # Upper Lefthand Corder (y0 -> 0)
X['s1'] = 1 # Scale
X['doubleCur'] = None

# Draw the screen.
def draw():
	# Clear screen.
	info.delete(1.0, END)
	canvas.delete(ALL)
	# Draw each box.
	for name in X['box']:
		x, y = X['box'][name]
		t = canvas.create_text((x-X['x0'])/X['s1'],(y-X['y0'])/X['s1'],text=name)
		
		X['bbox'][name] = canvas.bbox(t)
		b = None
		if X['doubleCur'] == name:
			b = canvas.create_rectangle(canvas.bbox(t), fill="#%02x%02x%02x" % (255, 0, 0))
		else:
			b = canvas.create_rectangle(canvas.bbox(t), fill="#%02x%02x%02x" % (0, 255, 0))
		canvas.tag_lower(b,t)
	# Draw the connections.
	for src, dest in X['arr']:
		canvas.create_line(*(X['box'][src] + X['box'][dest]) )

# View API
#- For get information about current state of graph
def getConnections():
	# dict comprehension requires python 2.7+
	return {x:X['con'][x] for x in X['con']}
def getBoxes():
	return [x for x in X['box'] ]
#- For graph
def addBox(name):
	# Place the box in the center of the viewable screen.
	X['box'][name] = ( X['x0'] + (X['s1']*int(canvas.cget('width'))/2), X['y0'] + (X['s1']*int(canvas.cget('height'))/2))
	draw()
def connect(name1, name2):
	X['con'][name1] = name2
	draw()
def moveBox(name, (x,y) ):
	X['box'][name] = (x,y)
	draw()
def moveView(x,y):
	X['x0'] = x
	X['y0'] = y
	draw()
def setScale(scale):
	X['s1'] = scale
	draw()
#- For Text/info
def setInfo(text):
	X['inf'] = text
	draw()
def getInfo():
	return X['inf']


# Callbacks.
S = {} # Temporary save variables.
S['cur'] = None
def inside( (x,y), (x1,y1,x2,y2) ):
	return (x1 < x and x < x2) and (y1 < y and y < y2)
def pickBox(event):
	GL = {}
	GL['ret'] = None
	for name in X['bbox']:
		if inside((event.x,event.y), X['bbox'][name]):
			GL['ret'] = name
	return GL['ret']
def click1(event):
	canvas.focus_set()
	S['event.x'] = event.x
	S['event.y'] = event.y
	S['box.x'] , S['box.y'] = 0 , 0
	# find the box to move.
	name = pickBox(event)
	if name != None:
		S['cur'] = name
		S['box.x'] , S['box.y'] = X['box'][name]
def click1hold(event):
	if S['cur'] != None:
		moveBox(S['cur'], (S['box.x']+(event.x-S['event.x']), S['box.y']+(event.y-S['event.y'])))
		draw()
def click1release(event):
	S['cur'] = None
def click1double(event):
	if pickBox(event) == None:
		X['doubleCur'] = None
	elif X['doubleCur'] == None:
		X['doubleCur'] = pickBox(event)
	else:
		dest = pickBox(event)
		X['con'][ X['doubleCur'] ] = dest
		X['doubleCur'] = None
	draw()
	
S['ss'] = 0
def key(event):
	print 'key called'
	if event.char == 'n':
		print 'n pressed'
		addBox('X' + str(S['ss']))
		S['ss'] += 1
	
# Register callbacks.
canvas.bind('<Button-1>', click1)
canvas.bind('<B1-Motion>',click1hold)
canvas.bind('<ButtonRelease-1>',click1release)
canvas.bind('<Double-Button-1>',click1double)
canvas.bind('<Key>',key)

# 
def run():
	mainloop()
if __name__ == '__main__':
	run()
