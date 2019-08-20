#!/usr/bin/env python
#
#This program demonstrates use of argparse
# argparse is a standard library which makes interpreting commandline arguments
# lot of fun, with very little coding on dev end .Behind the scene it makes use
# of argv only, however it has lot of error handling, documentation and 
# standardization, so that dev has to spend less time building!

import argparse

parser = argparse.ArgumentParser(description="The program reverses the text")
parser.add_argument("filename",help="input file for reading data  ")
parser.add_argument("--limit","-l", type=int, help="The number of lines to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 0.1")

args=parser.parse_args()
#print(args)
with open(args.filename) as file:   # open the file
    lines = file.readlines()        # reading file content into lines
    
    if args.limit:		    # if a limit is given by user, stick to only that many lines
       lines=lines[:args.limit]

    for line in lines:
       print(line.strip()[::-1])    # remove the whitespace and read
