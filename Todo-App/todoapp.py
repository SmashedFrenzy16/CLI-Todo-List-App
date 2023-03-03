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
