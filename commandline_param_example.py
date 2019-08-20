#!/usr/bin/env python
#
#This program demonstrate use of commandline params 

import sys

print("First commandline argument : " + sys.argv[0] )
#print("Second commandline argument : " + sys.argv[1] )
#print("Third commandline argument : " + sys.argv[2] )


print("Slicing /printing a list")
print( sys.argv[1:])
print("0th arg: " + sys.argv[0])

