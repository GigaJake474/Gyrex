# Variables
item = "item"

# Functions
def get():
    print("You picked up " + item)

# This is here to test get function
item = "a key."
user_input = input("test get")
if user_input == "get":
    get()
