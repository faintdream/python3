#! /usr/bin/env python
## A simple program to show usage of user input and displaying back same on the terminal

first_name = raw_input("First Name ? ")
last_name = raw_input(" Last Name ? ")
birthdate = raw_input("birthdate please  ")
age = int(raw_input("Your age " ))
print("My name is " + first_name + " " + last_name)
print("I was born on " + birthdate + ", " + "and I'm %d years old." %age)
