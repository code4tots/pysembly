#!/usr/bin/python
# 4.11.2012
# engine.py
# 
# pysembly runtime engine


class Engine:
    def __init__(self):
        self.types = { 'int':int }
        self.objects = {}
        self.connections = {}
        
    def registerType(self, type):
        self.types[type.__name__] = type
        
    def newObject(self, typeName, objectName):
        self.objects[objectName] = self.types[typeName]
        
    def newConnection(self, srcObj, srcPort, destObj, destPort):
        self.connections[(srcObj, srcPort)] = (destObj, destPort)
    
    def run(self):
        print(self.types)
        print(self.objects)
        print(self.connections)