#! /usr/bin/env python

#A program to read values from a dict object and utilizing if/else

user = { 'admin' : False, 'active' : False, 'name' : 'baburao' } 

if user['admin'] == True and  user['active'] == True:
    print("ACTIVE - (ADMIN) " + user['name'])
elif user['admin'] == True and  user['active'] ==False:
    print("(ADMIN) " + user['name'])
elif user['admin'] == False and  user['active'] == True:
    print("ACTIVE " + user['name'])
else:
    print("Inactive user - " + user['name'])
