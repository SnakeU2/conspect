#!/usr/bin/env python

def main():
    database.connect()

if __name__ == "__main__" :
    import curses
    import database
    main()

else:
    print("This is executable program file.\nDo not use this file as module.")
