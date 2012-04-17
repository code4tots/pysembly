#!/usr/bin/python
# 4.12.2012
# Pysembly runtime.
#
# Component requirements.
#	- run(self, msgs)
#		msgs are a list of (port, messages)

# Runtime.
class Runtime:
	def __init__(self):
		self.components = []
		self.running = False
		
	def registerComponent(self, component):
		self.components.append(component)
		
	def run(self):
		self.running = True
		while self.running:
			self.running = self.cycle()
		
	def cycle(self):
		for component in self.components:
			self.running = component.run()
			if not self.running:
				break
		return self.running
