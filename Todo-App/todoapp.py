import sys
import datetime

def help():

    sa = """Usage :-
$ ./todo add <todo item>  # Add a new todo item
$ ./todo ls               # Show remaining todo items
$ ./todo del NUMBER       # Delete a todo item
$ ./todo done NUMBER      # Complete a todo item
$ ./todo help             # Help menu
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

def add(i):

    file = open("todoapp.txt", "a")

    file.write(i)

    file.write("\n")

    file.close()

    s = '"'+s+'"'

    print(f"Added task: {s}")

def ls():

    pass
