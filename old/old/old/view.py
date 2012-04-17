#!/usr/bin/python

# Set up Tkinter and other global variables.
from Tkinter import *
root = Tk()
canvas = Canvas(root)
# For now model is just going to be a simple dict.
model = {	'boxes':[ 	['hello world', (20, 20)],
						['Reall really long text', (100, 100)],
						['Another', (200, 200)],
					],
			'arrows':[	['hello world', 'Another'],
					],
			'ULC':(0,0),
			'scale':1 ,
			'selected':None
}
view = {	'text': {},
			'box' : {},
			'lastpos':None
}

def draw(model):
	boxesAndLocations = model['boxes'] # Boxes are all just text.
	arrows = model['arrows']
	ULC = model['ULC'] # Upper Left Corner of visible screen.
	scale = model['scale'] # How the image should be scaled.
	
	# Clear the canvas.
	canvas.delete("all")
	
	# Draw the boxes.
	for text, (x,y) in boxesAndLocations:
		view['text'][text] = textObj = canvas.create_text(x,y,text=text)
		view['box'][text] = canvas.bbox(textObj)
		textBox = canvas.create_rectangle(canvas.bbox(textObj), fill="#%02x%02x%02x" % (0, 255, 0))
		canvas.tag_lower(textBox, textObj)
		
	# Draw the arrows.
	loc = {}
	for text, (x,y) in boxesAndLocations:
		loc[text] = (x,y)
	for arrow in arrows:
		canvas.create_line(*(loc[arrow[0]]+loc[arrow[1]]) )
	
# Callbacks
def insideBox( (x,y) , (x1, y1, x2, y2) ):
	return (x1 < x and x < x2) and (y1 < y and y < y2)
def selectBox(event):
	# Initialize.
	model['selected'] = None
	view['lastpos'] = (event.x, event.y)
	# Loop through each box and see if the click landed on any of the boxes.
	# If multiple boxes occupy a spot, pick the one on the top.
	for box in model['boxes']:
		text , _ = box
		if insideBox( (event.x, event.y) , view['box'][text] ):
			model['selected'] = box
	# Put the selected box on the top so that it gets drawn on top.
	for i in range(len(model['boxes'])):
		if id(model['boxes'][i]) == id(model['selected']):
			model['boxes'] = model['boxes'][:i] + model['boxes'][i+1:] + [ model['selected'] ]
			draw(model)
			break
		
def releaseBox(event):
	model['selected'] = None
	
def movingBox(event):
	if model['selected'] != None:
		x, y = model['selected'][1]
		model['selected'][1] = (x + (event.x-view['lastpos'][0]),y + (event.y-view['lastpos'][1]))
		view['lastpos'] = event.x , event.y
		draw(model)
		
# Bind the callbacks.
canvas.bind("<B1-Motion>", movingBox)
canvas.bind("<Button-1>", selectBox)
canvas.bind("<ButtonRelease-1>", releaseBox)

def run():
	# Do the first draw
	draw(model)
	# Show and run the program.
	canvas.pack(fill=BOTH, expand=1)
	mainloop()
	
if __name__ == '__main__':
	run()
