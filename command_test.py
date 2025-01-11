#Modules
import commands

# This is here to test get function
item = "a key."
user_input = input("test get")
if user_input == "get":
    commands.get()

#This is here to test the look function
you_see = "a door"
user_input = input("test look")
if user_input == "look":
    commands.look()

#This is here to test the quit function
user_input = input("test quit")
if user_input == "quit":
    commands.quit()