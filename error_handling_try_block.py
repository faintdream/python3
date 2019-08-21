#!/usr/bin/env python
#
# We are also demonstrateing use of try..except..finally block
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
try: 
    file = open(args.filename)      # open the file
    limit = args.limit
except IOError as err:
    print("Error:: " + str(err))
except :
    print("Runtime Error:: We don't know what went wrong  " )
else:
    with file:                      # loops through file object content 
        lines = file.readlines()        # reading file content into lines
    
        if args.limit:		    # if a limit is given by user, stick to only that many lines
            lines=lines[:limit]

        for line in lines:
            print(line.strip()[::-1])    # remove the whitespace and read
finally:
#this is the best place to keep code that has to run irrespective of situation ( an exceptin r no exception)
# example , may be we want to close a file or a db connection 
    print("No matter waht this section will be called")


