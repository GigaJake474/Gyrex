# Variables
item = "item"
you_see = "A temple"

# Functions
def get():
    print("You picked up " + item + ".")

def look():
    print("You see " + you_see + ".")

def quit():
    input("Are you sure you want to quit? y=1 n=2")
    if input == 1:
        quit()
    else:
        end()
