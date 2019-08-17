#! /usr/bin/env python

#A program to read values from a dict object which is inside a list and utilizing if/elif/else

users = [
{ 'admin' : False, 'active' : False, 'name' : 'baburao' },
{ 'admin' : True, 'active' : False, 'name' : 'baburao_ka_beta' },
{ 'admin' : False, 'active' : True, 'name' : 'baburao_ki_amma' },
{ 'admin' : True, 'active' : True, 'name' : 'baburao_ki_beti' },
] 
for user in users:
    if user['admin'] and  user['active']:
        print("ACTIVE - (ADMIN) " + user['name'])
    elif user['admin'] and  user['active'] ==False:
        print("(ADMIN) " + user['name'])
    elif user['admin'] == False and  user['active']:
        print("ACTIVE " + user['name'])
    else:
        print("Inactive user - " + user['name'])
