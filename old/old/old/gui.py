#!/usr/bin/python

# Set up Tkinter.
from Tkinter import *
root = Tk()
canvas = Canvas(root)
model = lambda: None # functions can have arbitrary attributes.
model.boxes = [ (50, 25, 150, 75) , (-50, -50, 50, 50), (100, 100, 110, 110) ]
model.arrows = None
model.ULC = (0, 0)
model.scale = 2

# redrawing the window given a model.
def draw(model):
	boxes = model.boxes
	arrows = model.arrows
	ULC = model.ULC # Upper Left Corner of visible screen.
	scale = model.scale # The scale.
	
	# Clear the canvas.
	canvas.delete("all")
	
	# Draw the boxes.
	for box in boxes:
		box = (box[0] - ULC[0], box[1] - ULC[1], box[2] - ULC[0] , box[3] - ULC[1])
		b = [scale * x for x in box]
		canvas.create_rectangle(*b, fill="#%02x%02x%02x" % (0, 255, 0))
		
	
		
		
# callbacks
def key(event):
	print "pressed", repr(event.char)
	model = lambda: None # functions can have arbitrary attributes.
	model.boxes = [ (50, 25, 150, 75) , (-50, -50, 50, 50), (100, 100, 110, 110) ]
	model.arrows = None
	model.ULC = (0, 0)
	model.scale = 2
	draw(model)
	# canvas.create_rectangle(50, 25, 150, 75, fill="blue")
	#canvas.create_rectangle(*p, fill="blue")

	
def button(event):
	canvas.focus_set()
	print "clicked at", event.x, event.y
	
def 
	
# Bind the callbacks.
canvas.bind("<Button>", button)
canvas.bind("<Key>", key)

def run()
	# Show and run the program.
	canvas.pack(fill=BOTH, expand=1)
	mainloop()
	
if __name__ == '__main__':
	run()
