#!/usr/bin/env python3
import os
import sys
import ftplib
import argparse
from F2Bpackages import ftpMain, dirMain


# Parses arguments and flags
def main():
    parser = argparse.ArgumentParser(
       # description="Main Interface",
        prog="Force2Brute",
        usage="Force2Brute [mode]",
        add_help=False
    )

# Creates a custom grp named modesGrp    
    modesGrp = parser.add_argument_group("Available modes")

# Adds args to modesGrp group
    modesGrp.add_argument("ftp", help="ftp bruteforcing")
    modesGrp.add_argument("ssh", help="ssh bruteforcing")
    modesGrp.add_argument("http", help="http bruteforcing")

# Creating helpGrp to move Options to the bottom of the help interface
    helpGrp = parser.add_argument_group("Options")
    helpGrp.add_argument('-h', '--help', action='help', help='show this help message and exit')


# Prints the help menu if no flags are passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    arg = parser.parse_args()

#ftpMain()

if __name__ == "__main__":
    main()
