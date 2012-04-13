#!/usr/bin/python
# 4.11.2012
# builder.py
# 
# Takes a a file (*.pysemble) describing the connection between all the components, and builds the desired program.

# pysemble files have the following format::
# OBJECTS
# (lists objects)
# <object type> <object name>
# CONNECTIONS
# (lists connections between objects)
# <src object> :: <source_port name> -> <dest object> :: <connection/dest_port name>
def run(filename,engine):
    # Read file and do some cleanup
    lines = open(filename).readlines()
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    # If the file doesn't start with OBJECT declarations, then raise an error.
    if lines[0] != 'OBJECTS':
        print('pysembly file must start with single line "OBJECTS".')
        return None
    # Look for 'CONNECTIONS'
    cur = 1
    while cur < len(lines) and lines[cur] != 'CONNECTIONS':
        cur += 1
    # If there is no line with just CONNECTIONS, then raise an erorr.
    if cur >= len(lines):
        print('"CONNECTIONS" line not found.')
        return None
    # Now split the chunks of input
    objectDeclarations = lines[1:cur]
    connectionDeclarations = lines[cur+1:]
    
    
    # parse and process all the object declarations.
    for objectDeclaration in objectDeclarations:
        objectDeclaration = objectDeclaration.split()
        type = objectDeclaration[0]
        name = objectDeclaration[1]
        # Now tell it to the engine
        engine.newObject(type, name)
    
    # now parse and process all the connections.
    for conn in connectionDeclarations:
        # split across '->'
        src , dest = [ x.strip() for x in conn.split('->') ]
        # split across '::'
        srcObj , srcPort = [ x.strip() for x in src.split('::') ]
        destObj, destPort = [x.strip() for x in dest.split('::') ]
        # Now tell it to the engine
        engine.newConnection(srcObj, srcPort, destObj, destPort)
        
    engine.run()
    
from engine import Engine
engine = Engine()
run('x.pysemble', engine)